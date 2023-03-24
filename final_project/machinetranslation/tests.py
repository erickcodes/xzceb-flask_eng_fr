import unittest
from translator import Translator

class testTranslator(unittest.TestCase):
    def tests_en2fr_None(self):
        watson = Translator()
        self.assertIsNone(watson.englishToFrench(None))

    def tests_fr2en_None(self):
        watson = Translator()
        self.assertIsNone(watson.frenchToEnglish(None))

    def tests_en2fr_Hello(self):
        watson = Translator()
        self.assertEqual(watson.englishToFrench("Hello"), "Bonjour")

    def tests_fr2en_Bonjour(self):
        watson = Translator()
        self.assertEqual(watson.frenchToEnglish("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
