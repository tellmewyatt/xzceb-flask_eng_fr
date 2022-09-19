""" Translator - French to English and English To French """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2022-09-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)
language_translator.set_service_url(url)
def translate(model, text):
    """ Translates text based on given model. Example: 'en-fr' translates english to french """
    try:
        transtext = language_translator.translate(
        text=text,
        model_id=model
        ).get_result()["translations"][0]["translation"]
        return transtext
    except ValueError:
        return ""
def englishToFrench(englishText):
    """ Translates english to French """
    frenchText = translate('en-fr', englishText)
    return frenchText
def frenchToEnglish(frenchText):
    """ Translates french to English """
    englishText = translate('fr-en', frenchText)
    return englishText
