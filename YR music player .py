#------------------------------------------------------------------libraries-----------------------------------------------------------------------------------------
from tkinter import *
import pygame
import os
#-------------------------------------------------coding----------------------------------------------------------------
root = Tk()
root.title('YR music player')
root.resizable(0,0)

status = StringVar()
status.set('playing')

#pygame.init()
#pygame.mixer.init()

track = LabelFrame(root, text='Song Track/Name',font='arial 15 bold',bg='gray',relief=GROOVE,width=600, height=120)
track.grid(padx=5,pady=5)

songtrack= Text(track, width=40,height=2,font='arial 15',bg='white',fg='red',state=DISABLED)
songtrack.grid(padx=5,pady=5)

textstatus = Label(track, textvariable = status, font='sans-serif 12', bg='gray',fg='red')
textstatus.grid(padx=5,pady=5)


root.mainloop()