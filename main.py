# Main Program
from backend import * 
import os

# Imported all required modules


wishMe()
while True:
    # This is main loop which runs until stopped
    check_alarm()
    query = takecommand().lower()

    if 'open youtube' in query :     
        search_youtube()

    elif 'google' in query :     
        google_search()   

    elif 'roll dice' in query :
        roll_dice()

    elif 'tell me the time' in query :  
        tell_time()

    elif 'email' in query:       
        send_email()

    elif 'sad' in query or 'lonely' in query :  
        feeling_sad()

    elif 'learning python' in query :
        learn_python()

    elif 'play music' in query:
        play_music()

    elif 'wikipedia' in query:
        search_wikipedia()

    elif 'weather' in query :
        weather_data()    

    elif "news" in query:
        news()    

    elif "set alarm" in query:
        alarm_time = input("Enter time at which alarm is to be set")                 
        continue

    elif 'screenshot' in query :
        screenshot()

    elif 'feeling demotivated' in query :
        feeling_demotivated()

    elif 'joke' in query :
        say_joke()

    elif 'coronavirus' in query :
        corona_news()   
                
    elif 'depression' in query :
        feeling_depressed()
                
    elif 'coin toss' in query:
        coin_toss()
                
    elif "who are we" in query :
        about_us()

    elif 'who are you' in query :
        about_program()                 

    elif 'create password' in query :
        create_password()
                    
    elif 'what can you do' in query:
        features()          

    elif 'switch the window' in query:
        switch_window()    

    elif "shut down the system" in query:
        os.system("shutdown /s /t 5")
        # Shutdown the computer 

    elif "restart the system" in query:
        os.system("shutdown /r /t 5")
        # Restart the computer

    elif "sleep the system" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")     
        # Make the computer sleep   

    elif 'exit' or 'stop' in query:
        break
