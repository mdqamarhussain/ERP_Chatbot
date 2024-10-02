import unittest
from backend.nlp_service import extract_entities


class NLPTestCase(unittest.TestCase):

    def test_extract_entities(self):
        text = "Apple is looking at buying U.K. startup for $1 billion"
        entities = extract_entities(text)
        self.assertIn(('Apple', 'ORG'), entities)
        self.assertIn(('U.K.', 'GPE'), entities)


if __name__ == '__main__':
    unittest.main()
