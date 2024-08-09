import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning my dear friend")
    elif hour > 12 and hour <= 18:
        speak("Good afternoon my dear friend")
    else:
        speak("Good evening my dear friend")
    speak("Let me know how I can help you, what are you looking for?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"My dear friend you said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that. Could you please repeat?")
        return None
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return None
    return query


def sendEmail(to, content):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        # Use environment variables or a more secure method for credentials
        server.login('aabderrahmane665@gmail.com', 'adbo(222)')
        server.sendmail('aabderrahmane665@gmail.com', to, content)
        server.close()
        speak('Your email has been sent successfully')
    except smtplib.SMTPAuthenticationError:
        speak('Authentication failed. Please check your email and password.')
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
        speak('I am unable to send the email. Please try again later.')
    except Exception as e:
        print(e)
        speak('An error occurred while sending the email.')

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand()
        if query:
            query = query.lower()
            if "open wikipedia" in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=4)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.DisambiguationError as e:
                    speak("There were multiple results. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak("Sorry, I could not find any page for that query.")
            elif "open notepad" in query:
                npath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath)
            elif "open paint" in query:
                npath = "C:\\Windows\\System32\\mspaint.exe"
                os.startfile(npath)
            elif "open youtube" in query:
                webbrowser.open('youtube.com')
            elif "open great learning academy" in query:
                webbrowser.open('https://www.mygreatlearning.com/academy')
            elif "open google" in query:
                webbrowser.open('google.com')
            elif "tell me the time" in query:
                strTime = datetime.datetime.now().strftime('%H:%M:')
                speak(f"My dear friend, the time is: {strTime}")
            elif "open great learning academy youtube channel" in query:
                webbrowser.open('https://www.youtube.com/user/beaconelearning')
            elif "open linkedin" in query:
                webbrowser.open('www.linkedin.com/in/aid-abderrahmane-3ab0312b9')
            elif "send email to other friend" in query:
                try:
                    speak('What should I send?')
                    content = takecommand()
                    if content: 
                        to = 'a.aid@esi-sba.dz'
                        sendEmail(to, content)
                except Exception as e:
                    print(e)
                    speak('I am unable to process your request at the moment.')
