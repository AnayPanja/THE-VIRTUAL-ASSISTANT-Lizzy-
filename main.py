import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import random

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('hellow ')
engine.runAndWait()
print('hellow!')

def wishme():
    hour = datetime.datetime.now().hour
    if(hour>=4 and hour<12):
        talk('good morning')
        print('good morning')
    elif(hour>=12 and hour<17):
        talk('good afternoon')
        print('good afternoon')
    elif(hour>=17 and hour<20):
        talk('good evening')
        print('good evening')
    else:
        talk('good night')
        print('good night')


def talk(text):
    engine.say(text)
    engine.runAndWait()

def taking_text():
    try:
        with sr.Microphone() as source:
            print('Listening..')
            #listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lizzy' in command:
                command = command.replace('lizzy', '')

    except:
        pass
    return command

def running():
    command = taking_text()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        print('playing...')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('the current time is '+ time)
    elif 'who is' in command:
        name = command.replace('who is', '')
        info = wikipedia.summary(name,2)
        print(info)
        talk(info)
    elif 'tell me about' in command:
        name = command.replace('tell me about','')
        info = wikipedia.summary(name,2)
        print(info)
        talk(info)
    elif 'jokes' in command:
        jokes = pyjokes.get_joke()
        print(jokes)
        talk(jokes)
    elif 'love' in command:
        print('Sorry...')
        talk('sorry,i think we are best friend')
        talk('actually i like you , but , i am in a deep relationship')
    elif 'search' in command:
        topic = command.replace('search about', '')
        pywhatkit.search(topic)
        print('Searching...')
    elif 'what is your name' in command:
        print('actually i am virtual assistent with computer voice,but you call me lizzy')
        talk('actually i am virtual assistent with computer voice')
        talk('but you call me lizzy')
    elif 'facebook' in command:
        webbrowser.open('https://www.facebook.com/')
        talk('i cant see your private chat, i think, you should check your own  ')
    elif 'g mail' in command:
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
        talk('opening gmail')
    elif 'where are you' in command:
        ans = 'hi sir, i am here . how can i help you sir ? '
        print(ans)
        talk(ans)
    elif 'open google' in command:
        print('opening google...')
        talk('opening google')
        webbrowser.open('https://www.google.com/')
    elif 'open youtube' in command:
        print('opening youtube ...')
        talk('opening youtube')
        webbrowser.open('https://www.youtube.com/')
    elif 'music' in command:
        print('playing music....')
        talk('playing music')
        music_directry = 'D:\\ANAY\\Musics'
        music = os.listdir(music_directry)
        index = random.randint(0,(len(music)-1))
        os.startfile(os.path.join(music_directry,music[index]))
    elif 'who are you' in command:
        print('actually i am virtual assistent with computer voice,but you call me lizzy')
        talk('actually i am virtual assistent with computer voice')
        talk('but you call me lizzy')
    elif 'open vs code' in command:
        print('opening vs code....')
        talk('opening vs code')
        path = 'C:\\Users\\Anay Panja\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile('C:\\Users\\Anay Panja\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
    elif 'open telegram' in command:
        print('opening telegram....')
        talk('opening telegram')
        path = 'C:\\Users\\Anay Panja\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe'
        os.startfile('C:\\Users\\Anay Panja\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe')

wishme()
while True:
    running()