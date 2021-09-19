import speech_recognition as sr


def Listen():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)

    try:
        print("recognising")    
        query = r.recognize_google(audio, language='eng-in')
        print(f"you said: {query}")

    except: 
        return ""

    query = str(query)
    return query.lower()

Listen()