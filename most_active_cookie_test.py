from most_active_cookie import make_parser, parse_log # exercise solution module
import argparse # python's cli-parsing library
import unittest # python's unittesting library

class MostActiveCookieTest(unittest.TestCase):

    """normal use cases"""

    # only one cookie is the most frequent
    def test_one_cookie(self):
        parser = make_parser()
        args = parser.parse_args(["cookie_log.csv", "-d", "2018-12-09"])
        result = parse_log(args)
        self.assertEqual(result, ["AtY0laUfhglK3lC7"])

    # cookies exist and all cookies on the date are the most frequent
    def test_all_cookies_tied(self):
        parser = make_parser()
        args = parser.parse_args(["cookie_log.csv", "-d", "2018-12-08"])
        result = parse_log(args)
        self.assertEqual(result, ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf",
                                "fbcn5UAVanZf6UtG"])

    # some of the cookies are tied for most frequent
    def test_some_cookies_tied(self):
        parser = make_parser()
        args = parser.parse_args(["cookie_log2.csv", "-d", "2018-12-08"])
        result = parse_log(args)
        self.assertEqual(result, ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf"])

    # no cookies exist
    def test_no_cookies(self):
        parser = make_parser()
        args = parser.parse_args(["cookie_log.csv", "-d", "2018-07-07"])
        result = parse_log(args)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
