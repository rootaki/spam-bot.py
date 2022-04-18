
import pyautogui
import time


# this file is only to ratelimited socials

print('''Spam Bot
        realized and developed by Aki
        all right reserved. ''')
time.sleep(1.00)

input('''what's spammy bot?
        spammy bot is a very simple bot that spams random phrases and messages taken from a text file.''')

time.sleep(0.5)

input('''how does it work?

Once the program has been started, all you have to do is go to the text bar of any social network (whatsapp, instagram, facebook, telegram) and wait for the bot to do its job.
once the program is activated you have 5 seconds to select the text bar.

Press 'Enter' to start the program.''')

time.sleep(5.00)

def spam():
        file = open("spam.txt", "r")

        for word in file:
        
                pyautogui.typewrite(word)
                pyautogui.hotkey(interval = 1.5)
                pyautogui.typewrite("\n")

spam()

print("All word sent correct. ")

choose = str(input("Do you want to restart spam? [y/n] "))

while (choose.lower() == "y" or "yes"):
        spam()

if (choose == "n" or "no"):
        input("OK, Press 'Enter' to close the program. ")

if (choose.lower() != "n" or "no" or "yes" or "y"):
        print("Uh Oh! Something went wrong. ")
        input("Press 'Enter' to close ")
