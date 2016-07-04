import unittest
from plugins.parser.timestamp import isMatch, parse


class TestSixenseModules(unittest.TestCase):

    def test_timestamp_parser(self):
        self.assertEqual(True, isMatch("1467598084"))

    def test_timestamp_converter(self):
        # slicing string from '\nTimestamp :\n1467598084.0\n\nDatetime
        # :\n2016-07-04 10:08:04\n\nPretty :\n43 minutes ago\n'
        result = parse("1467598084")[38:57]
        exp = '2016-07-04 10:08:04'
        self.assertEqual(exp, result)

if __name__ == '__main__':
    unittest.main()
