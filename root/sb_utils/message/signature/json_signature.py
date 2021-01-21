import base64
import canonicaljson
import json

from authlib.jose import JsonWebSignature, errors
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from typing import Union
# TODO: prep for varying serialization signatures


def json_sign(msg: Union[dict, str], privKey: str) -> dict:
    msg: dict = json.loads(msg) if isinstance(msg, str) else msg
    if not privKey:
        raise ValueError("privKey was not passed as a param")

    header = {
        "alg": "ES256",
        "kid": msg.get("headers", {}).get("from", 'ORIGIN')
    }
    sig_payload = b'.'.join([
        base64.b64encode(canonicaljson.encode_canonical_json(header)),
        base64.b64encode(canonicaljson.encode_canonical_json(msg))
    ])
    jws = JsonWebSignature()
    with open(privKey, 'r') as f:
        sig = jws.serialize_compact(header, sig_payload, f.read()).decode('utf-8').split('.')
    msg['signature'] = f'{sig[0]}..{sig[2]}'
    return msg


def json_verify(msg: Union[bytes, dict, str], pubKey: str = None) -> bool:
    msg: dict = msg if isinstance(msg, dict) else json.loads(msg)
    if signature := msg.pop('signature', None):
        sig = signature.split('.')
        header = json.loads(base64.b64decode(sig[0]))
        sig[1] = base64.b64encode(b'.'.join([
            base64.b64encode(canonicaljson.encode_canonical_json(header)),
            base64.b64encode(canonicaljson.encode_canonical_json(msg))
        ])).decode('utf-8').rstrip('=')

        def load_key(header, payload):
            if pubKey:
                with open(pubKey, 'rb') as f:
                    return f.read()
            if kid := header.get("kid"):
                print(f'Get key for {kid}')
                return ''
            return ''

        jws = JsonWebSignature()
        try:
            jws.deserialize_compact('.'.join(sig), load_key)
            return True
        except errors.BadSignatureError:
            return False
    raise ValueError("Message is not signed with JWS")
