import speech_recognition as sr
import pyttsx3
speaker = pyttsx3.init()
speaker.say("")
speaker.runAndWait()


mic = sr.Recognizer()

with sr.Microphone() as source:
    print("Start Speaking ...")
    voice = mic.listen(source)
    
    text = mic.recognize_google(voice)  
    print("You Said this:", text)
