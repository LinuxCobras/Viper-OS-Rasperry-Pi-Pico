import os
import sys
import time
import random
import math
#import machine
Time = 1200
date = 4/15


def menu():
    print ("type a option into the integrated terminal (@pico)")
    print ("IMPORTANT: if the terminal hangs, press Ctrl+D")
    print ("to run app 1 type 'vipe1' ... to run app 10 type 'vipe10'")
    print ("to generate a log file type 'logfile'")
    print ("to get a description type 'about'")
    print ("to open wordpad type 'wordpad' (type 'saveword' inside to save/exit)")
    print ("to play a game type 'game1'")
    print ("to view all files type 'ld'")
    print ("to shut down type 'shutdown'")
    print ("for a random bible verse type 'bibleverse'")
    print ("for a more detailed time output type 'time'")
    print ("type settings for settings options")
    print ("type df for a file deletion/recycle bin to delete a desired file")
    print ("type restart for a soft reboot")
    print ("type specs for spec info")
    print ("for version info type version")
    print ("to create a directory type cd")
    print ("to create a img file type ci")
    print ("to delete a directory type rd")
    print ("to write down and save a reminder type rmdr")
    print ("----------------------------------")    

def bootScreen():
    print("""
             .
           .. ..
           .. ..
   .......... ..
   .. ..........
   .. ..
    ...
     .
    . .         
""")
    bootInput = input("viper os press any key to boot")
    menu()

def fileBrowser():
    print (os.listdir())
    fileName = input ("vipe/user/home/bin/")
    try:
        with open (fileName, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except OSError:
        print ("unknown file")   
    except Exception as e:
        print ("error")
    input ("press any key to boot back to the main shell")
    menu()


def wordpad():
    print("--- WORDPAD MODE ---")
    print("Type anything. Type 'saveword' to save and return to shell.")
    
    session_text = []
    
    while True:
        userText = input("| ")
        
        if userText.lower() == "saveword":
            with open('wordpad.txt', 'a') as f:
                # Joins all lines typed and saves them
                f.write("\n" + "\n".join(session_text))
                print("FILES ARE SAVING TO: " + os.getcwd())
            print("File has been successfully saved to wordpad.txt")
            break 
        else:
            session_text.append(userText)
            print(userText)
    
    menu() 

def trivia():
    print ("raspberry pi pico trivia challenge")
    print ("question 1: what is the cpu of the raspberry pi pico called?")
    print ("a-rp2040 b-pico5427 c-raspberry cpu d-pi controller")
    userAnswer = input("answer:")
    if userAnswer.lower() == "rp2040" or userAnswer.lower() == "a":
        print ("right!")
    else:
        print ("incorrect!")
    menu()

def bibleverse():
    verses = [
    "For God so loved the world... - John 3:16",
    "The Lord is my shepherd; I shall not want. - Psalm 23:1",
    "I can do all things through Christ... - Philippians 4:13",
    "Trust in the Lord with all your heart... - Proverbs 3:5",
    "In the beginning, God created the heavens... - Genesis 1:1"
]
    print(random.choice(verses))
    verseInput = input("press any button to boot back to the terminal")
    menu()

def delete():
    print ("enter a file name to delete a file")
    fileSelect = input ("vipe/user/home/bin/")
    try:
        os.remove(fileSelect)
        print (fileSelect); print ("has been deleted from the pico's flash memory")
    except OSError:
        print ("the said file cannot be deleted or cannot be found")
        input ("press any key to boot back to the main shell")




def settings():
    print ("settings type 'time' for a option to set the time or 'date' to set the date")
    inputT2 = input ("please choose a setting") 
    if inputT2 == "time":
        timeInput = input ("input the current time:")
        Time = timeInput
        print ("the new time is"); print (time)
    elif inputT2 == "date":
        dateInput = input ("input the current date please")
        date = dateInput
        print ("the date is on this system"); print (date)
    elif inputT2 == "password":
      print ("type a new password for running disk commands")
      storedPass = input ("userPass*:")
      print ("this is your new password"); print (storedPass)

    elif inputT2 == "Diskcmds":
        print ("type your disk command password here to use the format commands")
        usedPass = input ("raspberry pico*")
        if usedPass.lower() == (storedPass):
            print ("format")
        else:
            print ("error:type the password correctly and if you dont have a tempory password for these commands make one in settings!")


    else:
        print ("system error: please enter a valid setting")
        time.sleep(10)
        menu()

def taskmanager():
    print (sys.getfilesystemencoding)
    print (sys.platform)


def folderCreator():
    folderName = "dir1"
    try:
        os.mkdir(folderName)
        print("a new directory on the drive has been created at"); print(Time)
    except OSError as e:
    # This will catch errors, such as if the folder already exists
        print(f"Error: {e}")

def imgcreate():
    f = open("e.img", "w")
    f.close()
    print ("a image file has been created at"); print(Time)

def removedir():
    print ("type the name of the directory here")
    rmsd = input ("user/vipe/bin/directories/")
    os.rmdir(rmsd)
    print ("the directory has been removed")

def reminder():
    remindinput = input ("|")
    reminderName = input ("|")
    try:
        with open(reminderName, "w") as f:
            f.write(remindinput)
            print ("the new reminder has been saved"); print (remindinput)
    except Exception as e:
        print ("error this file name has already been taken", e)

menu()

try:
    while True:
        user_Input = input ("user@pico$")

        if user_Input.lower() == "vipe1":
            exec(open('vipe1.py').read())
        elif user_Input.lower() == "vipe2":
            exec(open('vipe2.py').read())
        # ... (Repeat for vipe3 through vipe10)
        elif user_Input.lower() == "shutdown":
            sys.exit()
        elif user_Input.lower() == "logfile":
            with open('logs.txt', 'a') as f:
                f.write('\nNew log entry')
            print("Log entry created.")
        elif user_Input.lower() == "ld":
            fileBrowser()
        elif user_Input.lower() == "about":
            print ("Viper OS is a MicroPython based shell for the RPi Pico")
            input ("press any key to continue")
            menu()
        elif user_Input.lower() == "wordpad":
            wordpad()
        elif user_Input.lower() == "game1":
            trivia()
        elif user_Input.lower() == "restart":
            bootScreen()
        elif user_Input.lower() == "bibleverse":
            bibleverse()
        elif user_Input.lower() == "advancedtime":
            print (time.localtime())
        elif user_Input.lower() == "settings":
            settings()
        elif user_Input.lower()== "time":
            print ("the current set time is"); print (Time)
        elif user_Input.lower()== "date":
            print ("the current date is"); print (date)
        elif user_Input.lower()== "df":
            delete()
        elif user_Input.lower()== "specs":
            taskmanager()
        elif user_Input.lower()== "version":
            print ("the version of viper os is 1.1")
        elif user_Input.lower()== "cd":
            folderCreator()
        elif user_Input.lower()== "ci":
            imgcreate()
        elif user_Input.lower()== "rd":
            removedir()
        elif user_Input.lower()== "rmdr":
            reminder()
        
        else:
            print ("System Error: please enter a valid command")
            menu()
except Exception as e:
    print("""

                       ..   ..   
                       ..   ..


                     .         .
                  .              .
                .                  .
              .                      .
             .                        .
             .                        .
""")
print ("Critical Stop!:A Critical System Error Occurred That Could Not Be Identified")
input ("press any key to restart the machine")
sys.exit
print ("launching sys module exit for restart")
sys.exit
