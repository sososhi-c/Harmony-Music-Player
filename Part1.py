from tkinter import *
import mysql.connector;
import pygame
import os
root = Tk()

#Initialised the pygame.mixer
pygame.mixer.init()

#Connecting to MYSQL
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root1234',
    database = 'dbmsProject'
)
mycursor = mydb.cursor();


#Creating Play button
def create_play():
    play = Button(root,text = "PLAY",padx = 20, pady = 20,command=QuerySelection)      
    play.place(x =10,y =50)

#Function which contains queries:
def QuerySelection():
    mycursor.execute('select * from songs')
    result = mycursor.fetchall()
    file_path = result[0][7]
    split_path = file_path.split('\\')
    new_path = '//'.join(split_path)
    pygame.mixer.music.load(new_path)          #Here it plays the song 
    pygame.mixer.music.play(loops = 0)

create_play()
root.geometry("900x650")           # sets the dimensions of the window
root.mainloop()   


