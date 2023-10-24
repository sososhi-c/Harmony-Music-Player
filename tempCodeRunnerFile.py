from tkinter import *
import mysql.connector;
import pygame
import time
import os
root = Tk()

#Initialised the pygame.mixer
pygame.mixer.init()

#Connecting to MYSQL
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='riddlethis',
    database = 'dbmsProject'
)
mycursor = mydb.cursor();


class create_regulator_button:
    unpause_flag = False
    start_time = time.time()
    end_time = 0
    
    def __init__(self,db_manager):
     self.db_manager = db_manager
    
    def create_buttons(self):
     play = Button(root,text = "PLAY",padx = 20, pady = 20,command =self.db_manager.QuerySelection)      
     play.place(x =10,y =50)

     pause = Button(root,text = "PAUSE",padx = 20, pady = 20,command=self.song_pause)     #A pause button has been created. When this is clicked, it goes to song_pause func
     pause.place(x =100,y =50)  

     forward= Button(root,text = ">>",padx = 20, pady = 20,command=fast_forward)
     forward.place(x = 200,y = 50)

     reverse= Button(root,text = "<<",padx = 20, pady = 20,command=rewind)
     reverse.place(x = 300,y = 50)

     reverse= Button(root,text = "STOP",padx = 20, pady = 20,command=stop)
     reverse.place(x = 400,y = 50)

     def song_pause(self):
          #here the music is PAUSED (not stopped) ath the same time another button is created with same text but this button uses a command to resume the song
          pygame.mixer.music.pause()

          aft = Button(root,text = "PLAY",padx = 20, pady = 20,command = self.song_startaft_pause)
          aft.place(x =10,y =50)

          create_regulator_button.unpause_flag = True
          create_regulator_button.end_time = time.time()

     def song_startaft_pause(self):                    #After pausing this method is used to unpause a song
          pygame.mixer.music.unpause()

     #This method fast forwards the song
     def fast_forward(self):
          end_time =  time.time()                                                                             #end_time has the time since epoch time
          time_lapsed = end_time-create_regulator_button.start_time                         #the start_time is class variable and also uses time.time() which starts as soon as the program.Time_lapsed tells us the time passed since the start of the program and when the fast fprward was clicked
          gtime = pygame.mixer.music.get_pos()                                                      # gtime gets the amount of time the song runs for
          pygame.mixer.music.set_pos((gtime/1000)+time_lapsed)                            #set_pos sets the time to which we want the song to play at

     def rewind(self):
          #This part deals when the pause button has been clicked
          if  create_regulator_button.unpause_flag == True:                                    
               end_time =  time.time()                                                                        #end_time has the time since epoch time
               time_lapsed = end_time-create_regulator_button.start_time                    #time_lapsed caluclates time difference between when program begins and when rewind button is cliked
               gtime = pygame.mixer.music.get_pos()                                                 #gtime gest the amount of time the song plays for
               pygame.mixer.music.set_pos(time_lapsed-(gtime/1000))                       # this part sets the song to play a time less than aht has been played

          #This part deals when the pause button has not been clicked
          else:
               end_time =  time.time()
               gtime = pygame.mixer.music.get_pos()
               time_lapsed = end_time-create_regulator_button.start_time
               pygame.mixer.music.set_pos(time_lapsed-(gtime//1000))

     def stop(self):
          pygame.mixer.music.stop()          #Stops the music

class databaseManagement:
    def __init__(self):
     pass
    
    def QuerySelection(self):
        mycursor.execute('select * from songs')
        result = mycursor.fetchall()
        file_path = result[0][7]
        split_path = file_path.split('\\')
        new_path = '//'.join(split_path)
        pygame.mixer.music.load(new_path)          #Here it plays the song 
        pygame.mixer.music.play(loops = 0)


db_manager = databaseManagement()
app = create_regulator_button(db_manager)
app.create_buttons()

root.geometry("900x650")           # sets the dimensions of the window
root.mainloop()   


