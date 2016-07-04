import unittest
import urllib
from plugins.parser.timestamp import isMatch as timestamp_isMatch
from plugins.parser.timestamp import parse as timestamp_parse
from plugins.parser.myip import isMatch as myip_isMatch
from plugins.parser.base64_ import isMatch as base64_isMatch
from plugins.parser.base64_ import parse as base64_parse


class TestSixenseModules(unittest.TestCase):

    def test_timestamp_parser(self):
        self.assertEqual(True, timestamp_isMatch("1467598084"))

    def test_timestamp_converter(self):
        # slicing string from '\nTimestamp :\n1467598084.0\n\nDatetime
        # :\n2016-07-04 10:08:04\n\nPretty :\n43 minutes ago\n'
        result = timestamp_parse("1467598084")[38:57]
        exp = '2016-07-04 10:08:04'
        self.assertEqual(exp, result)

    def test_ip_parser(self):
        self.assertEqual(True, myip_isMatch("myip"))

    def test_ip_finder_alive(self):
        code = urllib.urlopen("http://icanhazip.com").getcode()
        self.assertEqual(200, code)

    def test_base64_parser(self):
        b64 = "sixense".encode("base64")
        self.assertEqual(True, base64_isMatch(b64))

    def test_base64_decoder(self):
        result = base64_parse("c2l4ZW5zZQ==")[36:43]
        self.assertEqual("sixense", result)


if __name__ == '__main__':
    unittest.main()
