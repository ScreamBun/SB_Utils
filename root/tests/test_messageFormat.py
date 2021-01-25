"""
Test Format Conversion
"""
import os
import unittest

from tempfile import TemporaryFile
from typing import Dict
from sb_utils import Message, SerialFormats
from beautifultable import BeautifulTable
from .utils import MetaTests, sizeof_fmt

test_dir = os.path.dirname(os.path.realpath(__file__))


class FormatTests(unittest.TestCase, metaclass=MetaTests):
    msg_dir = os.path.join(test_dir, 'messages')
    msg_files: Dict[str, dict]
    sizes: Dict[str, Dict[str, Dict[str, int]]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.msg_files = {}
        cls.sizes = {}

    @classmethod
    def tearDownClass(cls) -> None:
        with open(os.path.join(test_dir, '../sizes.md'), 'w') as f:
            f.write('# Message Sizes\n\n')
            for test, results in cls.sizes.items():
                f.write(f'## {test}')
                # Format Sizes
                size_table = BeautifulTable()
                size_table.set_style(BeautifulTable.STYLE_MARKDOWN)
                size_table.columns.header = ["Request", "Response", "Notification"]
                row_headers = []

                for fmt, msgs in results.items():
                    row_headers.append(fmt)
                    size_table.rows.append([sizeof_fmt(msgs[c]) if c in msgs else 'N/A' for c in size_table.columns.header])
                size_table.rows.header = row_headers
                f.write(f'\n{size_table}\n\n')

    def _getSize(self, msg: Message, file: str) -> None:
        m = msg.oc2_message(True)
        f = ' '.join(map(str.capitalize, os.path.splitext(os.path.split(file)[1])[0].split('_')))
        with TemporaryFile(mode='wb' if isinstance(m, bytes) else 'w') as tf:
            tf.write(m)
            tf.flush()
            self.sizes.setdefault(f, {}).setdefault(msg.content_type.name, {})[msg.msg_type.name] = tf.tell()

    def _load_msg(self, msg_file: str, fmt: SerialFormats) -> Message:
        if msg_file in self.msg_files:
            m = self.msg_files[msg_file]
        else:
            with open(msg_file, 'r') as f:
                m = f.read()
        msg = Message.oc2_loads(m, SerialFormats.JSON)
        msg.content_type = fmt
        self._getSize(msg, msg_file)
        return msg

    # Base tests for all messages
    def _test_good_msg(self, msg_file: str, fmt: SerialFormats) -> None:
        msg = self._load_msg(msg_file, fmt)
        file = os.path.splitext(msg_file.replace('messages/input/', 'messages/output/'))[0] + f'.{fmt}'
        if os.path.isfile(file):
            with open(file, 'r') as f:
                self.assertEqual(f.read(), msg.oc2_message(True))

    def _test_bad_msg(self, msg_file: str, fmt: SerialFormats) -> None:
        with self.assertRaises(Exception):
            msg = self._load_msg(msg_file, fmt)
            file = os.path.splitext(msg_file.replace('messages/input/', 'messages/output/'))[0] + f'.{fmt}'
            if os.path.isfile(file):
                with open(file, 'rb') as f:
                    self.assertNotEqual(f.read(), msg.oc2_message(True))

    # Tests are generated via the metaclass


if __name__ == "__main__":
    unittest.main()
