import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def say(Text):
    print("   ")
    print(f"Adhvika: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("   ")

