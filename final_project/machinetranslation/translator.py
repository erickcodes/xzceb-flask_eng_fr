import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

class Translator:    
    def __init__(self):
        load_dotenv()
        apikey = os.environ['apikey']
        url = os.environ['url']
        IAM_auth = IAMAuthenticator(apikey) 
        self.lang_translator = LanguageTranslatorV3("2018-05-01", IAM_auth)
        self.lang_translator.set_service_url(url)

    def translate(self, text, original, translated):        
        model_id = f'{original}-{translated}'
        return self.lang_translator.translate(text, model_id = model_id, 
            source = original, target = translated)

    def englishToFrench(self, englishText):
        if englishText is None:
            return
        original = "en"
        translated = "fr"
        response = self.translate(englishText, original, translated)
        if response.get_status_code() != 200:
            print(f'Error! Status code: {response.get_status_code()}')
            return
        return response.get_result()["translations"][0]["translation"]

    def frenchToEnglish(self, frenchText):
        if frenchText is None:
            return
        original = "fr"
        translated = "en"
        response = self.translate(frenchText, original, translated)
        if response.get_status_code() != 200:
            print(f'Error! Status code: {response.get_status_code()}')
            return
        return response.get_result()["translations"][0]["translation"]