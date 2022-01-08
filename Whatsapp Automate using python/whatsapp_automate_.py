from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def WhatsappMsg(name,message):
    startfile("C:\\Users\\rahul\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(0.5)
    click(x=298,y=134) # serach
    sleep(0.5)
    write(name)  #write name on search tab
    sleep(0.5)
    click(x=186,y=281) # click or person name
    sleep(0.5)
    click(x=1170, y=985)  # message
    sleep(0.5)
    write(message)
    click(x=1872, y=979) # message send
    sleep(0.5)
    


def whatsappcall(name):
    startfile("C:\\Users\\rahul\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(0.5)
    click(x=298,y=134) # serach
    sleep(0.5)
    write(name)  #write name on search tab
    sleep(0.5)
    click(x=186,y=281) # click or person name
    sleep(0.5)
    click(x=1723, y=67)  # call
    sleep(0.5)
 


def whatsppChatOpen(name):
    startfile("C:\\Users\\rahul\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(0.5)
    click(x=298,y=134) # serach
    sleep(0.5)
    write(name)  #write name on search tab
    sleep(0.5)
    click(x=186,y=281) # click or person name
    sleep(0.5)
    


def whatsappVideoCall(name):
    startfile("C:\\Users\\rahul\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(0.5)
    click(x=298,y=134) # serach
    sleep(0.5)
    write(name)  #write name on search tab
    sleep(0.5)
    click(x=186,y=281) # click or person name
    sleep(0.5)
    click(x=1663, y=75) # video call
    sleep(0.5)
   


def checkSetting():
    startfile("C:\\Users\\rahul\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(0.5)
    click(x=527, y=70)
    sleep(0.2)
    click(x=1267, y=1016)
    sleep(0.5)
   


name = input("Enter name: ")
message = input("Enter message: ")
n = 1 
while n is not 0:
    print("1: send message\n2:audio call\n3: search chat\n4: video call\n5:check setting")
    choice = int(input("Enter choice: "))
    if n is 1:
        WhatsappMsg('name',message)
    elif n is 2:
        whatsappcall('name')
    elif n is 3:
        whatsppChatOpen('name')
    elif n is 4:
        whatsappVideoCall('name')
    elif n is 5:
        checkSetting()
    else:
        print("wrong choice")
        print("want to continue? if yes enter 1 otherwise 0")
        k = int(input())
        n = k




