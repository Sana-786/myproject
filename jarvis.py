import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sana!!")

    elif hour>=12 and hour<18:
        speak("good afternoon sana!!")

    else:
        speak("good evening sana!!")
    
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    # IT TAKES MICROPHONE INPUT FROM USER AND RETURNS STRING OUTPUT

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)

        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    #speak(" GOOD MORNING sana, u are amazing...")
    wishMe()
    while True:
        query = takeCommand().lower()
    # LOGIC FOR EXECUTING TASK BASED ON QUERY
    if 'wikipedia' in query:
        speak("Searching Wikipedia.....")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak ("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")


    elif 'open google' in query:
        webbrowser.open("google.com")


    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'D:\\Non Ctritical\\songs\\Favourite Songs'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")


elif 'open code' in query:
    codePath ="C:\\Users\\rijwana tabassum\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

elif 'email to sana' in query:
    try:
        speak("What shoul I say?")
        content = takeCommand()
        to = "sanayouEmail@gmail.com"   
        sendEmail(to, content)
        speak("Email has been sent!!")
    except Exception as e:
        print(e)
        speak("Sorry my friend..I am unable to send this email")



