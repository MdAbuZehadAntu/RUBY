import pyttsx3
import os
import speech_recognition as sr
import webbrowser
from googletrans import Translator , constants
import pyttsx3
import spacy
import nltk
from gtts import gTTS
from playsound import playsound
import multiprocessing
import translators as ts
import warnings

warnings.filterwarnings("ignore")

# Initialize the engine
engine = pyttsx3.init()

# obtain audio from the microphone
r = sr.Recognizer()

# nlp spacy model
tokenizer = spacy.load('en_core_web_sm')

# language
s_lang = 'en-US'


def feature_setup(v_rate , v_volume):
    voices = engine.getProperty('voices')  # gets you the details of the current voice
    engine.setProperty('voice' , voices[1].id)  # 0-male voice , 1-female voice

    # speaking speed setup
    rate = engine.getProperty('rate')
    engine.setProperty('rate' , rate * v_rate)
    engine.setProperty("volume" , v_volume)


def speak(audio , s_lang):
    if s_lang == "english":
        engine.say(audio)
        engine.runAndWait()  # Without this command, speech will not be audible to us.
    elif s_lang == "bangla":
        # speaking in bengali
        tts = gTTS(text=audio , lang='bn')
        tts.save("../data/bangla_audio/test_bangla.mp3")
        playsound('../data/bangla_audio/test_bangla.mp3' , True)

        p = multiprocessing.Process(target=playsound , args=("../data/bangla_audio/test_bangla.mp3" ,))
        p.start()
        p.terminate()
        os.remove("../data/bangla_audio/test_bangla.mp3")


def listen(l_lang):
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Listened")
        if l_lang == "english":
            try:
                text = r.recognize_google(audio)
                print("You said : " + text)
                return text
            except:
                print("Sorry could not recognize your voice")
                return "Sorry could not recognize your voice"
        elif l_lang == "bangla":
            try:
                text = r.recognize_google(audio , language="bn-BD")
                print("You said : " + text)
                return text
            except:
                print("Sorry could not recognize your voice")
                return "Sorry could not recognize your voice"


def intro():
    speak("Hello , Welcome to your voice assistant Ruby , How can I help you ?" , s_lang="english")
    speak("Which Language do you want me to talk?" , s_lang="english")
    speak("Please say English or Bangla" , s_lang="english")
    chosen_lang = listen("english")
    return chosen_lang.lower()


def translate(text , target_lang):
    query = text.lower()
    print(query)
    translator = Translator()
    translation = translator.translate(query , dest=target_lang)
    print(translation.text)
    query = translation.text
    return query


if __name__ == "__main__":
    feature_setup(v_rate=0.75 , v_volume=1.5)
    chosen_lang = intro()
    speak("Chosen Language is " + chosen_lang , s_lang="english")
    while True:
        if chosen_lang == "english":
            pass
        elif chosen_lang == "bangla":

            speech = listen("english")
            translated_speech = translate(speech , 'bn')
            speak(translated_speech , chosen_lang)
            print(speech)

