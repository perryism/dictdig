import unittest
from dictdig import DictDig

class DictDigTest(unittest.TestCase):
    def test_dig(self):
        subject = {
                    "foo": {
                        "bar": "foo bar"
                    }
                  }

        self.assertEqual(DictDig(subject).dig("foo.bar"), "foo bar")
        self.assertEqual(DictDig(subject).dig("bar.foo"), None)

        self.assertEqual(DictDig(subject).dig("bar.foo", "foobar"), "foobar")

    def test_dig_complex(self):
        subject = {
                    "foo": [
                        "apple",
                        "orange", {"yellow": [
                            "banana", "pineapple"
                        ]}
                    ]
                  }

        dig = DictDig(subject)
        self.assertEqual(dig.dig("foo[0]"), "apple")
        self.assertEqual(dig.dig("foo[1]"), "orange")
        self.assertEqual(dig.dig("foo[2].yellow[0]"), "banana")
        self.assertEqual(dig.dig("foo[].yellow"), "banana")

    def test_dig_nested_list(self):
        subject = {
                    "foo": [
                        "apple",
                        "orange", [
                            "banana", "pineapple"
                        ]
                    ]
                  }

        self.assertEqual(DictDig(subject).dig("foo[0]"), "apple")
        self.assertEqual(DictDig(subject).dig("foo[1]"), "orange")
        self.assertEqual(DictDig(subject).dig("foo[2][0]"), "banana")
