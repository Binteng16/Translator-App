import unittest
from knowledge_base import KnowledgeBase

class TestKnowledgeBase(unittest.TestCase):
    def setUp(self):
        self.kb = KnowledgeBase()

    def test_get_language_recommendation(self):
        text = "selamat pagi"
        recommended_language = self.kb.get_language_recommendation(text)
        self.assertEqual(recommended_language, 'en-id')

if __name__ == '__main__':
    unittest.main()
