import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

class TranslatorManager:    
    def __init__(self):
        load_dotenv()
        apikey = os.environ['apikey']
        url = os.environ['url']
        IAM_auth = IAMAuthenticator(apikey) 
        self.lang_translator = LanguageTranslatorV3("2018-05-01", IAM_auth)
        self.lang_translator.set_service_url(url)

    def englishToFrench(self, englishText):
        original = "en"
        translated = "fr"
        model_id = f'{original}-{translated}'
        response = self.lang_translator.translate(englishText, model_id = model_id, 
            source = original, target = translated)
        if response.get_status_code != 200:
            print("Error!")
            return
        return response.get_result()["translations"]["translation"]

    def frenchToEnglish(self, frenchText):
        original = "fr"
        translated = "en"
        model_id = f'{original}-{translated}'
        response = self.lang_translator.translate(frenchText, model_id = model_id, 
            source = original, target = translated)
        if response.get_status_code != 200:
            print("Error!")
            return 
        return response.get_result()["translations"]["translation"]
