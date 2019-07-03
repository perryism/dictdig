from dictdig.list_extractor import ListExtractor
import unittest

class ListExtractorTest(unittest.TestCase):
    def test_extract(self):
        data = {
                "name": [
                    ["apple", "orange"],
                    ["banana"]
                ]
            }

        extractor = ListExtractor("name[1]")
        actual = extractor.extract(data)
        self.assertEqual(actual, ["banana"])

        extractor = ListExtractor("name[0][1]")
        actual = extractor.extract(data)
        self.assertEqual(actual, "orange")
