import os
import sys
import time
import random
import math
import machine
Time = 1200
date = 4/15

def menu():
    print("this is the Piper kernel (get it viper+ pi pico!) feel free to make your own os for the pico based on this type help to get help")

def fileBrowser():
    print (os.listdir())
    fileName = input ("vipe/user/home/bin/")
    try:
        with open (fileName, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except OSError:
        print ("oops")   
    except Exception as e:
        print ("oops")
    input ("press any key to boot back to the main shell")
    menu()

def delete():
    print ("enter a file name to delete a file")
    fileSelect = input ("vipe/user/home/bin/")
    try:
        os.remove(fileSelect)
        print (fileSelect); print ("deleted")
    except OSError:
        print ("oops")
        input ("press any key to boot back to the main shell")

def folderCreator():
    folderName = "dir1"
    try:
        os.mkdir(folderName)
        print("created directory"); print(Time)
    except OSError as e:
    # This will catch errors, such as if the folder already exists
        print(f"oops: {e}")

def removedir():
    print ("type the name of the directory here")
    rmsd = input ("user/vipe/bin/directories/")
    os.rmdir(rmsd)
    print ("the directory has been removed")

menu()

try:
    while True:
        userInput = input ("root@pico$")
        if userInput.lower().strip() == "rd":
            removedir()
            menu()
        elif userInput.lower().strip() == "cd":
            folderCreator()
            menu()
        elif userInput.lower().strip() == "ld":
            fileBrowser()
            menu()
        elif userInput.lower().strip() == "df":
            delete()
            menu()
        elif userInput.lower().strip() == "help":
            print ("type df to delete file ld to view files cd to make directories and rd to remove directories")
            menu()
        else:
            print("oops")
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
        print(f"KERNEL PANIC! AN UNHANDLED ERROR HAS OCCURRED: {e}")
        machine.lightsleep(5)