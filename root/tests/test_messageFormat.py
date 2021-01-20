"""
Test Format Conversion
"""
import os
import unittest
import uuid

from datetime import datetime
from typing import Dict
from sb_utils import Message, MessageType, SerialFormats

test_dir = os.path.dirname(os.path.realpath(__file__))
request_id = uuid.uuid4()
cmd_args = {
    "recipients": [],
    "origin": "",
    "created": datetime.now(),
    "msg_type": MessageType.Request,
    "request_id": request_id,
    "content": {}
}
rsp_args = {
    "recipients": [],
    "origin": "",
    "created": datetime.now(),
    "msg_type": MessageType.Response,
    "request_id": request_id,
    "content": {}
}


class FormatTests(unittest.TestCase):
    sizes: Dict[str, Dict[str, int]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.sizes = {}

    @classmethod
    def tearDownClass(cls) -> None:
        # Print sizes and smallest/largest sizes
        print(cls.sizes)

    def _getSize(self, msg: Message) -> None:
        # Get size of message and add to sizes dict
        self.sizes.setdefault(msg.msg_type.name, {})[msg.content_type.name] = 0

    def test_cmd_json(self) -> None:
        cmd = Message(**cmd_args, serialization=SerialFormats.JSON)
        self._getSize(cmd)

    def test_rsp_json(self) -> None:
        rsp = Message(**rsp_args, serialization=SerialFormats.JSON)
        self._getSize(rsp)


if __name__ == "__main__":
    unittest.main()
