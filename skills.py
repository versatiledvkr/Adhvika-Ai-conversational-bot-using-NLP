import speak
import datetime
import wikipedia
import pywhatkit
from listen import Listen


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    speak.say(time)

def Date():
    date = datetime.date.today()
    speak.say(date)

def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        result = wikipedia.summary(name)
        speak.say(result)

    elif "google" in tag:
        name = str(query).replace("search","").replace("please search","")
        pywhatkit.search(query)

    elif "whatsapp" in tag:
        speak.say("what should i say")
        wsup= Listen()
        speak.say("please enter number and by what time i should send message")
        pywhatkit.sendwhatmsg("+91"+input(),f"{wsup}",int(input()),int(input()))
        speak.say('message sent')

    elif "email" in tag:
         speak.say("please enter sender's email id")
         sender = input()
         speak.say("please enter the password,it is safe don't worry")
         password= input()
         speak.say("what is the subject")
         subject= Listen()
         speak.say("what is the content")
         content= Listen()
         speak.say ("please enter the receiver email id")
         receiver= input()
         pywhatkit.send_mail(sender,password,subject,content,receiver)

    elif "youtube" in tag:
        speak.say ("what should i play")
        you= Listen() 
        pywhatkit.playonyt(f"{you}")
        speak.say("playing" + f"{you}")

    