import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

# pip install pocketsphinx

recognizer = sr.Recognizer
engine = pyttsx3.init()
newsapi = "d2227778605b40b1a480d2b5e3213088"


def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif"open facebook" in c.lower():
        webbrowser.open("https://facebook.com")  
    elif"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")    
    elif"open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)  
    elif "news" in c.lower():
        r = requests.get(" https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            #  Print the headline
            for article in articles:
                speak(article['title'])
                          

if __name__ == "__main__":
    speak("initializing jojo....")
    while True:
        # Listen for the wake word "jojo"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
           
        print("recognizing...")
        try:
            with sr.Microphone() as source:
              print("Listening...")
              audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower() == "jojo"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
        except sr.UnknownValueError:
            print("jojo could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))  


    




