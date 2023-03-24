import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

class Translator:
    """
    A class represents our translation service that utilizes IBM's AI Watson.
    ...
    Attributes
    ----------
    lang_translator : LanguageTranslatorV3
        
    Methods
    -------
    __init__(self) : Translator
        initial authenication and watson api service
    translate(self, text, original, translated) : DetailedResponse
        translation of the text from orignal langauge to the translated langauge
    englishToFrench(self, englishText) : str
        translates englishText into French
    frenchToEnglish(self, frenchText) : str
        translates frenchText into English
    """

    def __init__(self):
        load_dotenv()
        apikey = os.environ['apikey']
        url = os.environ['url']
        iam_auth = IAMAuthenticator(apikey)
        self.lang_translator = LanguageTranslatorV3("2018-05-01", iam_auth)
        self.lang_translator.set_service_url(url)

    def translate(self, text, original, translated):
        """
        return DetailedResponse, text from original langauge to translated langauge
        """
        model_id = f'{original}-{translated}'
        return self.lang_translator.translate(text, model_id = model_id,
            source = original, target = translated)

    def englishToFrench(self, englishText):
        """
        return French translation of englishText
        """
        if englishText is None:
            return None
        original = "en"
        translated = "fr"
        response = self.translate(englishText, original, translated)
        if response.get_status_code() != 200:
            print(f'Error! Status code: {response.get_status_code()}')
            return None
        return response.get_result()["translations"][0]["translation"]

    def frenchToEnglish(self, frenchText):
        """
        return English translation of frenchText
        """
        if frenchText is None:
            return None
        original = "fr"
        translated = "en"
        response = self.translate(frenchText, original, translated)
        if response.get_status_code() != 200:
            print(f'Error! Status code: {response.get_status_code()}')
            return None
        return response.get_result()["translations"][0]["translation"]
