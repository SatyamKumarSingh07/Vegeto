import pyttsx3 as p
from my_selenium_script import Infow
from Yt_audio import Videoyt
import speech_recognition as sr

# Initialize text-to-speech engine
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize speech recognizer
r = sr.Recognizer()

# Initial greeting
speak("Hello Sir, I am Vegeto, How can I help you?")

# Listen for the first command
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

# Respond to the initial query
if "what" in text and "about" in text and "you" in text:
    speak("I am having a good day, sir.")
    speak("How can I help you?")

# Listen for the next command
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

# Handle commands based on user input
if "information" in text2:
    speak("You need information about which topic?")
    
    # Listen for the topic
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        topic = r.recognize_google(audio)
    
    speak(f"Searching {topic} in Wikipedia")
    assist = Infow()
    assist.getinfo(topic)

elif "play" in text2 and "video" in text2:
    speak("You want me to play which video?")
    
    # Listen for the video name
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        video = r.recognize_google(audio)
    speak(f"playing {video}")
    assist = Videoyt()
    assist.play_song(video)
