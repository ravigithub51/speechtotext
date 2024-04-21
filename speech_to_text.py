import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def record_text():
    while True:  
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                return MyText
        except sr.RequestError as e:
            print(f"Could not request results: {e}")
        except sr.UnknownValueError:
            print("Unknown error occurred")

def output_text(text):
    with open("output.txt", "a") as f:  
        f.write(text + "\n")

while True:
    text = record_text()
    output_text(text)
    print("Wrote text:", text)
