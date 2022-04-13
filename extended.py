#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In this code, we will use the morse code as provided by wikipedia
# For the sake of this task, i have modified the dot to be 0.5 seconds to be 
# able to differentiate between a dot and a dash 

# dot  - 1 second
# dash = 3 seconds
# space between parts of same letter =  1 second
# space between letters  = 3 seconds
# space between words = 7 seconds

# reference : https://en.wikipedia.org/wiki/Morse_code#/media/File:International_Morse_Code.svg


from tkinter import*
import tkinter.font
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED = 5   # LED pin to be used in our system

GPIO.setup(LED,GPIO.OUT) # make it as output pin


MORSE_CODE = {    #definition of the morse code and the corresponding alphabets
'A':'.-', 
'B':'-...',
'C':'-.-.', 
'D':'-..', 
'E':'.',
'F':'..-.',
'G':'--.', 
'H':'....',               
'I':'..', 
'J':'.---', 
'K':'-.-', 
'L':'.-..', 
'M':'--', 
'N':'-.',
'O':'---', 
'P':'.--.', 
'Q':'--.-',                  
'R':'.-.', 
'S':'...',
'T':'-',
'U':'..-', 
'V':'...-',
'W':'.--',
'X':'-..-', 
'Y':'-.--', 
'Z':'--..'
}



# GUI - user interactive
win =Tk()
win.title("Convert your text to morse code")
myFont=tkinter.font.Font(family='Helvitica', size=14, weight="bold")

#Event Functions 
def dot():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)

def dash():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(1)

def convert():
    input = user_input.get()
    for letter in input:
        for symbol in MORSE_CODE[letter.upper()]:
            if symbol == '.':
                dot()
            elif symbol == "-":
                dash()
            else:
                time.sleep(1) #time between parts of same letter
        time.sleep(3) # time between each letter
    
        
# Menu Widgets
user_input = Entry(win, font=myFont, width=24, bg ='white')
user_input.grid(row=0,column=0)

button = Button(win, text= 'Convert it!', font=myFont, command=convert, bg= 'grey', height =1, width=12)
button.grid(row=1,column=0)

