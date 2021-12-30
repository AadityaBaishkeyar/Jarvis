import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from pywikihow import search_wikihow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')  
    else:
        speak('Good Evening!')      
    speak("I am Jarvis your personal assistant. How may I help you ")

def takecommand():
    #It takes microphone access from user and gives out string output    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  
        print(f"User: {query}\n")

    except Exception as e:
        #print(e)
        speak("Say that again please....")   
        return "None" 
    return query     
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'hello' in query:
            speak('Hello Sir')
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open website' in query:
            speak('Which website do you want to open ?')
            search = takecommand()
            chrompath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'  
            webbrowser.get(chrompath).open_new_tab(search+'.com')  
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")            
        elif 'exit' in query:
            speak('Thankyou')
            quit()
        elif 'activate help mode' in query:
            
            speak("Help mode activated. What should I search?")  
            how = takecommand()
            max_result = 1
            how_to = search_wikihow(how,max_result)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)  

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("Jarvis","") 
            query = query.replace("google search","") 
            query = query.replace("google","") 
            
            try:
                
                pywhatkit.search(query)
                result = googleScrap.summary(query,3)
                speak("This is what I got on the web!")
                speak(result)

            except: 
                speak("No callable data found")    
        
