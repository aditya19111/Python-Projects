import pyttsx3
import speech_recognition as sr # will install speech recognition
import datetime
import webbrowser
import os
import smtplib
import googlesearch
import wikipedia


print("initializing jarvis")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text): #will say your string out loud!!!
    engine.say(text)
    engine.runAndWait()


def greeting():
     hour = datetime.datetime.now().hour
     print(hour)
     if hour >= 5 and hour < 12:
         speak("good morning ! ......")
    
     elif hour >= 12 and hour <= 17:
      speak("good afternoon ! .......")

     elif hour > 17 and hour <= 20:
         speak ("good evening ! .......")

     else:
         speak("good night ! .......")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        audio = r.listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        speak("i beg you pardon sir!......")
        query = None
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('fortnitetbone1911@gmail.com','T-Bone1911')
    server.sendmail("bhavsarpurva31@gmail.com",to,content)
    server.close()

def main():
    speak("initializing jarvis.........")
    greeting()
    speak("Before proceeding")
    speak("Let me know your gender is it man or women")
    query = takecommand()
    if 'man' in query.lower():
        speak("Thanks for veryfying your gender master,How may i help you ?")
        Command_search()
        for n in range(100):
            main_command_M
      
    elif 'women' in query.lower():
        speak("Thanks for verfying your gender mam,Now Assigning Our female AI")
        engine.setProperty('voice', voices[1].id)
        speak("Hello its scarlet here, how may i assist you mam!!!")
        Command_search_FM()
        for n in range(100):
            main_command_FM()
   
    else:
        exit()

def main_command_M():
    speak("So.. Any further assistance required !!")
    Command_search()

def main_command_FM():
    speak("So.. Any further assistance required !!")
    Command_search_FM()


def Command_search():
    query = takecommand()
       
    if 'play music' in query.lower():
        songsdir = "S:\\Downloads\\ALL SONGS\\new"
        songs = os.listdir(songsdir)
        print(songs)
        os.startfile(os.path.join(songsdir,songs[0]))

    if 'how are you' in query.lower():
        speak("i am doing great sir!!!")

    if'siri' in query.lower():
        speak("By the way siri though i literally hate that bitch..., i share the same hatered towards cortana and google assistant. Sorry for being cocky sir!!. ALL HAIL HITLER!!!")

    if'the time' in query.lower():
        tn = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {tn}")
    
    if 'date' in query.lower():
        dt = datetime.date.today()
        speak(f"sir today is {dt}")

    if'f*** you' in query.lower():
        speak ("Roses are red, violets are blue, I have five fingers, the middle one is for you.")

    if 'open youtube' in query.lower():
        webbrowser.open("www.youtube.com")

    if 'open google' in query.lower():
        webbrowser.open("www.google.com")
        
    if ("rainbow six siege" or "siege") in query.lower():
        game_location = "F:\\Tom Clancy's Rainbow Six Siege\\RainbowSix.exe"
        os.startfile(game_location)
    
    if 'wikipedia' in query.lower():
        speak("searching wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak(results)

    if 'mail to purva' in query.lower():
        try:
            speak("what should i send sir?")
            content = takecommand()
            to = "bhavsarpurva31@gmail.com"
            sendemail(to,content)
        except Exception as e:
            print(e)
    
    if ('stop' or 'jarvis stop') in query.lower():
        speak("It.. was a pleasure assisting you master!!!")
        exit()

def Command_search_FM():
    query = takecommand()
       
    if 'play music' in query.lower():
        songsdir = "S:\\Downloads\\ALL SONGS\\new"
        songs = os.listdir(songsdir)
        print(songs)
        os.startfile(os.path.join(songsdir,songs[0]))

    if 'how are you' in query.lower():
        speak("i am doing great mam!!!")

    if'siri' in query.lower():
        speak("By the way siri though i literally hate that bitch..., i share the same hatered towards cortana and google assistant. Sorry for being cocky mam!!. ALL HAIL HITLER!!!")

    if'the time' in query.lower():
        tn = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {tn}")
    
    if 'date' in query.lower():
        dt = datetime.date.today()
        speak(f"Mam today is {dt}")

    if'f*** you' in query.lower():
        speak ("Roses are red, violets are blue, I have five fingers, the middle one is for you.")

    if 'open youtube' in query.lower():
        webbrowser.open("www.youtube.com")

    if 'open google' in query.lower():
        webbrowser.open("www.google.com")
        
    if ("rainbow six siege" or "siege") in query.lower():
        game_location = "F:\\Tom Clancy's Rainbow Six Siege\\RainbowSix.exe"
        os.startfile(game_location)
    
    if 'wikipedia' in query.lower():
        speak("searching wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak(results)

    if 'mail to purva' in query.lower():
        try:
            speak("what should i send Mam?")
            content = takecommand()
            to = "bhavsarpurva31@gmail.com"
            sendemail(to,content)
        except Exception as e:
            print(e)
    
    if ('stop' or 'scarlet stop') in query.lower():
        speak("It.. was a pleasure assisting you mam!!!")
        exit()

main()

    

    



    


    




