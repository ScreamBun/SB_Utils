"""
Test Format Conversion
"""
import json
import os
import unittest
import uuid

from datetime import datetime
from tempfile import TemporaryFile
from typing import Dict
from sb_utils import Message, MessageType, SerialFormats
from beautifultable import BeautifulTable

test_dir = os.path.dirname(os.path.realpath(__file__))
created = datetime.utcfromtimestamp(1611227337)
request_id = uuid.UUID("15e2de83-61c2-4857-991a-fc50f2d51da8")
cmd_args = {
    "recipients": [],
    "origin": "",
    "created": created,
    "msg_type": MessageType.Request,
    "request_id": request_id,
    "content": {}
}
rsp_args = {
    "recipients": [],
    "origin": "",
    "created": created,
    "msg_type": MessageType.Response,
    "request_id": request_id,
    "content": {}
}


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return f'{num:3.1f}{unit}{suffix}'
        num /= 1024.0
    return f'{num:.1f}Yi{suffix}'


class FormatTests(unittest.TestCase):
    sizes: BeautifulTable

    @classmethod
    def setUpClass(cls) -> None:
        cls.sizes = {}

    @classmethod
    def tearDownClass(cls) -> None:
        # Print sizes and smallest/largest sizes
        stats = {
            "Request": {
                "Smallest": min(cls.sizes["Request"].items(), key=lambda i: i[1]),
                "Largest": max(cls.sizes["Request"].items(), key=lambda i: i[1])
            },
            "Response": {
                "Smallest": min(cls.sizes["Response"].items(), key=lambda i: i[1]),
                "Largest": max(cls.sizes["Response"].items(), key=lambda i: i[1])
            }
        }
        print(cls.sizes)
        print(stats)

    def _getSize(self, msg: Message) -> None:
        m = msg.oc2_message(True)
        with TemporaryFile(mode='wb' if isinstance(m, bytes) else 'w') as f:
            f.write(m)
            f.flush()
            self.sizes.setdefault(msg.msg_type.name, {})[msg.content_type.name] = f.tell()

    def test_cmd_json(self) -> None:
        cmd = Message(**cmd_args, serialization=SerialFormats.JSON)
        self._getSize(cmd)
        with open(os.path.join(test_dir, 'formats/request.json'), 'r') as f:
            self.assertDictEqual(json.load(f), cmd.oc2_message())

    def test_rsp_json(self) -> None:
        rsp = Message(**rsp_args, serialization=SerialFormats.JSON)
        self._getSize(rsp)
        with open(os.path.join(test_dir, 'formats/response.json'), 'r') as f:
            self.assertDictEqual(json.load(f), rsp.oc2_message())

    def test_cmd_cbor(self) -> None:
        cmd = Message(**cmd_args, serialization=SerialFormats.CBOR)
        self._getSize(cmd)
        with open(os.path.join(test_dir, 'formats/request.cbor'), 'rb') as f:
            self.assertEqual(f.read(), cmd.oc2_message(True))

    def test_rsp_cbor(self) -> None:
        rsp = Message(**rsp_args, serialization=SerialFormats.CBOR)
        self._getSize(rsp)
        with open(os.path.join(test_dir, 'formats/response.cbor'), 'rb') as f:
            self.assertEqual(f.read(), rsp.oc2_message(True))


if __name__ == "__main__":
    unittest.main()
