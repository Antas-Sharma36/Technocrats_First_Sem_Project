
#This is the part of the program where all the functions have been defined 

import pyttsx3 as pts

import speech_recognition as sr

import webbrowser as wb

import datetime

import time

import random

import smtplib

import pywhatkit

import pyjokes

import os

import wikipedia

import requests

from bs4 import BeautifulSoup 

import os.path

import pyautogui

import numpy as np 
import cv2 

#Imported all required modules

##############################################################################

engine = pts.init('sapi5')                                                   
voices = engine.getProperty('voices')                                                                               
engine.setProperty('voices', voices[0].id)                                      

# Initialized the engine here

##############################################################################

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Function for making the program speak

##############################################################################

def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=50,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

# Function for taking voice input

##############################################################################

def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello I am Me6, how can I help you?")       

# Wishes user according on the time
    
################################################################################################################

alarm_time = None
def check_alarm():
    current_time = datetime.datetime.now().strftime("%H") + " " + datetime.datetime.now().strftime("%M")
    i = 0 
    if current_time == alarm_time and alarm_time != None and i == 1 :
       speak("Hello") 
       i += 1
       #Play alarm music here
       music_dir = 'Enter music Directory here'
       songs = os.listdir(music_dir)
       os.startfile(os.path.join(music_dir, songs[0]))

# Check Alarm

################################################################################################################
          
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bbc6cb870ed24b148ea8eb783f2837b0'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    speak('Today\'s news headlines are:')    
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(head[i])

# Get the news headlines

################################################################################################################

def search_youtube():     
    speak("What video do you want to see ?")
    Video_srch = takecommand()
    vs = Video_srch.replace(' ','+') 
    wb.open('https://www.youtube.com//results?search_query=' + vs)

# Search Video on Youtube

################################################################################################################    

def google_search():
    speak('What do you want to search in google?')
    srch = takecommand()
    wb.open("http://www.google.com/search?q=" + srch)     

# Perform a Google Search

################################################################################################################

def roll_dice():
    x = random.randint(1,6)
    speak(x)    

# Roll a dice and tell the result

################################################################################################################

def tell_time():
    x = datetime.datetime.now()
    speak(x) 

# Tell the time

################################################################################################################

def send_email():
    try:
        speak("What should I say?")
        content = takecommand()
        to = 'sharmaantas20@gmail.com' 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('email', 'password')     # Enter password before running the program 
        server.sendmail('email', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry , I am not able to send this email")       

# Send an email
 
################################################################################################################

def feeling_sad():
   msg = 'This is an automatically generated message .your friend is feeling lonely ,could you light up his mood?'
   x = datetime.datetime.now()
   y1 = x.strftime('%H')
   y2 = x.strftime('%M')
   y3=int(y2)+1
   pywhatkit.sendwhatmsg("Enter Number here",msg,int(y1),int(y3))  

# Sends a whatsapp message to the user's friend to prevent sadness

################################################################################################################

def learn_python():
    speak('Text or Video?')
    t_c = takecommand()
    if t_c == 'text':
        wb.open('https://www.geeksforgeeks.org/python-programming-language/learn-python-tutorial/') 
    elif t_c == 'video' :
        wb.open('https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3')    
    else:    
        speak('Unable to understand you.')      

# Opens a website or video for learning python 

################################################################################################################

def play_music():
    music_dir = 'Enter music Directory here'  
    songs = os.listdir(music_dir)                                                   
    print(songs)    
    os.startfile(os.path.join(music_dir, songs[0]))        

# Play a song (The song must be on the computer)

################################################################################################################

def search_wikipedia():
    speak('What do you want to search on wikipedia?')
    st1 = takecommand()
    speak('Searching Wikipedia...')
    #query = query.replace("wikipedia", "")
    results = wikipedia.summary(st1, sentences=2)
    speak("According to Wikipedia")
    speak(results)        

# Search Wikipedia 

################################################################################################################

def weather_data():
    search = 'temperature in delhi' 
    url = f"http://www.google.com/search?q={search}"   
    r = requests.get(url)
    data = BeautifulSoup(r.text,'html.parser')
    temp = data.find('div',class_= 'BNeawe').text
    speak(f"current {search} is {temp}") 

# Get the weather news

################################################################################################################

def screenshot():
    image = pyautogui.screenshot() 
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR) 
    cv2.imwrite("image1.png", image)

# Take a screenshot (Of the window on top)

################################################################################################################

def feeling_demotivated():
    speak('Sometimes we\'re tested now to show our weaknesses,but to discover our strengths.')
    wb.open('https://www.youtube.com/watch?v=QI4M75LLM-I')

# Says a motivating quote and opens a motivating video to prevent demotivation

################################################################################################################

def say_joke():
    joke = pyjokes.get_joke()
    speak(joke)    

# Tell a joke

################################################################################################################

def corona_news():
    corona_advice = '''Coronaviruses are a group of related RNA viruses that cause diseases in mammals and birds.
    The first known human infections were in Wuhan, Hubei, China.
    Most common symptoms: fever, dry cough, tiredness.
    To prevent the spread of COVID-19: 
    Clean your hands often. Use soap and water, or an alcohol-based hand rub.
    Maintain a safe distance from anyone who is coughing or sneezing.
    Wear a mask when physical distancing is not possible.
    Medical treatments:
    If you have mild symptoms and are otherwise healthy, self-isolate and contact your medical provider or a COVID-19 information line for advice.'''
    speak(corona_advice) 

# Speak some coronavirus details and prevention

###############################################################################################################################      

def feeling_depressed():
    advice = '''We know this is a tough time , you should consult your local psychiatrist and for more help 
    contact - Toll Free : 1800 233 3330 , WEBSITE : http://www.jeevanaastha.com/ EMAIL : help@jeevanaastha.com''' 
    speak(advice)    

# Gives helpine details for depression
     
###############################################################################################################################

def coin_toss():
    randm_side = random.choice(['heads','tails'])
    speak(randm_side)

# Toss a coin and tell the result

################################################################################################################

def about_us():
    details_u = '''We are the Technocrats of Bennett University
    Our team comprises of Antas,Tanish,Bhavya,Sachit,Anantak
    Currently working on a voice assistant'''
    speak(details_u)

# Say the details of the authors of this program 

################################################################################################################

def about_program():
    details_me = '''I am Me6 created by the technocrats. I am a voice assistant. 
    My function is to help you with your day to day tasks via voice communication'''   
    speak(details_me)    

# Tell(Speak) about itself 

################################################################################################################

def create_password():
    speak('For what site?')
    nme_of_site = takecommand()
    num = random.randrange(000,1000)
    s = str(num)
    for i in range(3):
        alp_num_u = random.randrange(65,91)
        alp_num_l = random.randrange(97,123)
        s += chr(alp_num_l) + chr(alp_num_u)
    st = ['!','@','#','$','%','^','&','*']
    n = len(st)
    num = random.randrange(0,n)
    sp = st[num]  
    s += str(sp)
    speak(s)
    pswrd = open('passwrd.txt','a')
    pswrd.write(str(nme_of_site)+':'+str(s))
    pswrd.write("\n")
    pswrd.close()

# Create a password for some website(website will be taken as input)
 
################################################################################################################

def features():
    features = '''I can do the folloeing tasks - 
    1. Wish me (goodafternoon, goodevening, goodmorning)
    2. Set alarm
    3. Send email
    4. Search on youtube
    5. Search on Chrome
    6. Search on wikipedia
    7. Take a screenshot
    8. Create a random password
    9. Roll a die
    10. Toss a coin
    11. Current Time
    12. News
    13. Weather
    14. Help for loneliness/Sadness
    15. Feeling demotivated
    16. Tell a joke
    17. Coronavirus
    18. Help for Depression
    19. Who are we
    20. Who are you
    21. Shut down
    22. Restart
    23. Sleep
    24. Stop'''
    print(features)   

# Display features of the program

################################################################################################################

def switch_window():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.keyUp("alt")    

# Switch window

################################################################################################################










