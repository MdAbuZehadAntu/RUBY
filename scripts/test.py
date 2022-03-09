import multiprocessing
from gtts import gTTS
from playsound import playsound
import os
# speaking in bengali
from gtts import gTTS
import playsound

tts = gTTS(text='hello', lang='en')
tts.save("../data/bangla_audio/test_bangla.mp3")
playsound.playsound("../data/bangla_audio/test_bangla.mp3")
# tts = gTTS(text="আপনি কেমন আছেন" , lang='bn')
# tts.save("../data/bangla_audio/test_bangla.mp3")
# playsound('../data/bangla_audio/test_bangla.mp3' , True)

p = multiprocessing.Process(target=playsound , args=("../data/bangla_audio/test_bangla.mp3" ,))
p.start()
p.terminate()
os.remove("../data/bangla_audio/test_bangla.mp3")