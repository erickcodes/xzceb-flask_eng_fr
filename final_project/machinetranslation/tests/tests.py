import unittest
from machinetranslation.translator import Translator

class TestTranslator(unittest.TestCase):
    def setUp(self):
        self.watson = Translator()
        super().setUp()

    def tests_en2fr_None(self):
        self.assertIsNone(self.watson.englishToFrench(None))

    def tests_fr2en_None(self):
        self.assertIsNone(self.watson.frenchToEnglish(None))

    def tests_en2fr_Hello(self):
        self.assertEqual(self.watson.englishToFrench("Hello"), "Bonjour")

    def tests_fr2en_Bonjour(self):
        self.assertEqual(self.watson.frenchToEnglish("Bonjour"), "Hello")

if __name__ == '__main__':
    # Resource Warning
    unittest.main(warnings='ignore')