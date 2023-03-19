import unittest
from translator import TranslatorManager

class testTranslator(unittest.TestCase):

    def tests(self):
        translator = TranslatorManager()
        self.assertIsNone(translator.englishToFrench(None))
        self.assertIsNone(translator.frenchToEnglish(None))
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour")
        self.assertEqual(translator.frenchToEnglish("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
