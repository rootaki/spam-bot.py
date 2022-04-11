
import pyautogui
import time


# this file is for every social. for only ratelimited socials see spam-bot.py


print('''Spam Bot
        realized and developed by Aki
        all right reserved. 
        Whatsapp version''')
time.sleep(1.00)

input('''what's spammy bot?
        spammy bot is a very simple bot that spams random phrases and messages taken from a text file.''')

time.sleep(0.5)

input('''how does it work?
once the program has been started, all you have to do is go to the text bar of any social network (whatsapp, instagram, facebook, telegram) and wait for the bot to do its job.
once the program is activated you have 5 seconds to select the text bar.
Press 'Enter' to start the program.''')

time.sleep(5)
f = open("spam.txt", "r")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.typewrite("\n")
