from tkinter import *
import customtkinter as ct
import serial
import write_command as wc

ser = serial.Serial("/dev/ttyAMA0",9600)

def on_pressed():
	print("pressed")


class LED:
	def __init__(self,pos,initial_state):
		self.pos = pos
		self.state = initial_state
	def __call__(self):
		self.state = (self.state+1)%2
		wc.write_string(ser,"{L"+str(self.pos)+str(self.state)+"100000}")
		print("{L"+str(self.pos)+str(self.state)+"100000}")

led1 = LED(0,0)
led2 = LED(1,0)
led3 = LED(2,0)
led4 = LED(3,0)
#darkmode
ct.set_appearance_mode("dark")

#colortheme
ct.set_default_color_theme("blue")

# window
root = ct.CTk()
#root.frame =MyFrame(master=root) 

#window size
root.geometry('300x400')

#button
button1 = ct.CTkButton(root,text="LED1", font=("inter",14),command = led1)
button2 = ct.CTkButton(root,text="LED2", font=("inter",14),command = led2)
button3 = ct.CTkButton(root,text="LED3", font=("inter",14),command = led3)
button4 = ct.CTkButton(root,text="LED4", font=("inter",14),command = led4)

#putting it in center
button1.place(relx=0.5,rely=0.2,anchor = CENTER)
button2.place(relx=0.5,rely=0.4,anchor = CENTER)
button3.place(relx=0.5,rely=0.6,anchor = CENTER)
button4.place(relx=0.5,rely=0.8,anchor = CENTER)
#running it
root.title("LEDS on IO-card")
root.mainloop()
#ser.close()

