# File: create_daily_git_pull.py
# Company: The San Diego Drone Pro
# Author: Daniel "Dragon" Sanfelice
# Description: Allows users to input git repositories to be updated every day.

import os
import time

def main():

    # create a file called "Daily Git Pull" and enter the required text at the top of every bash script
    # Can I save this as a .bash? Or do I save it as a text and convert it to .bash?
    f= open("your_daily_git_pull.bash", "w+")
    f.write("#!/bin/bash/n")
    f.write("This program will perform a git pull on your repositories/n")
    f.write(" ")

    #def user_input():
    val = " "

    print("This will create a script with all your daily git repositories that you would like to update every morning.")
    print("Enter the path of a directory to add it to the script, or press 'n' to close the program and write the script.")


    while val != "n":
        val = input("Enter the path of a directory you would like this script to update: ")
        if val == "y":
               #write the input to the file
            f.write("cd " + str(val) + "\n")
            f.write("git pull" + "\n")
            f.write("" "")

        else:
            break

    print("the program has closed")

    #Now make the bash script executable
    os.system("chmod +x daily_git_pull.bash")

    #TODO: create a an alias to run the command
    os.system("alias daily_git='./daily_git_pull'")

    #Tell them the program is done and their script is ready to run from the terminal
    print("You can now enter './daily_git_pull' in your home directory to update all of your repositories")

    #The End

    sys.exit()    
