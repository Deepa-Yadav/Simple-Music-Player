import os  # for handling pc operation
from tkinter import *  # gui
from tkinter import filedialog

import pygame  # load and play
from mutagen.id3 import ID3
from tkinter.messagebox import *

from PIL import ImageTk,Image

root = Tk()
root.geometry("1600x800+0+0")
root.configure(background="black")
Tops = Frame(root,width=1200,height=100,bd=8,bg="black")
Tops.pack(side=TOP)

#image background
#canvas = Canvas(root,width=300,height=160)
#image = root.PhotoImage("‪C:\Users\AJ\Desktop\yo1.png")
#canvas.create_image(0,0,anchor=NW,image=image)
#canvas.pack()



lblinfo=Label(Tops,font=('Georgia',40,'bold'),text="DJ AJ",bd=10,fg="red")

lblinfo.grid(row=0,column=0)
lblinfo.pack()

songs=[]
songsname=[]
index=0

current_song=StringVar()
belows=Frame(root,width=900,height=250,bd=100,bg="black")
belows.pack(side=BOTTOM)
current_label=Label(belows,font=('Georgia',20,'bold'),textvariable=current_song,width=35)
current_label.grid(row=100,column=100)



index=0
def for_next():
    global index
    index+=1
    if index >= len(songs):
        btn5['state'] = 'disabled'
        pygame.mixer.music.stop()
        index = 0
        showinfo("FYI", "playlist is over . u wanna continue press button PLAY")
    else:
        pygame.mixer.music.load(songs[index])
        pygame.mixer.music.play()
        update_label()


def for_prev():
    global index
    index-=1

    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()
    update_label()

def for_stop():
   pygame.mixer.music.stop()
   current_song.set("no song playing")

def update_label():
    global index
    global playingsong
    current_song.set(songsname[index])
    #return playingsong

def for_pause():
    pygame.mixer.music.pause()
def for_unpause():
    pygame.mixer.music.unpause()

def for_play():
  global index
  btn5['state']='normal'
  txtdisplay.itemconfig(index, {'fg': 'red'})
  pygame.mixer.music.load(list[index])
  pygame.mixer.music.play()
def for_exit():
  exit=askyesno("music player","are u want exit click(yes/no)?")
  if exit>0:
    root.destroy()
    return



def selectdirectory():
  directory = filedialog.askdirectory()#dialoguebox
  os.chdir(directory)#song folder

  for gaana in os.listdir(directory):#covert folder into a list
      if gaana.endswith(".mp3"):#to specifically select mp3
          realdirectory=os.path.realpath(gaana)
          file = ID3(realdirectory)
          title=file.get('TIT2','no album title')
          songsname.append(title)
          songs.append(gaana)#to add songs to out list 'song'
         # print(gaana)






  #https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.stop
  pygame.mixer.init()
  pygame.mixer.music.load(songs[1])
  pygame.mixer.music.play()
  update_label()

songbox = Listbox(root, height=18, width=38, bd=16, font=('arial', 15, 'bold'), fg="black", bg="powder blue")
songbox.place(relx=0.5, rely=0.5, anchor=CENTER)

selectdirectory()
#https://www.tutorialspoint.com/python/tk_label.htm

#songbox=Listbox(root)
#songbox.pack()

songsname.reverse()
for gaana in songsname:
    songbox.insert(0,gaana)
songsname.reverse()





b1=Button(root,text="play",fg="powder blue",padx=10,pady=10,bd=4,width=10,bg="blue",font=('arial',15,'bold'),command=for_play)
b1.place(relx=0.8,rely=0.3,anchor=CENTER)

b2=Button(root,text="next",fg="powder blue",bg="blue",padx=10,pady=10,bd=4,width=10,state="normal",font=('arial',15,'bold'),command=for_next)
b2.place(relx=0.8,rely=0.4,anchor=CENTER)

b3=Button(root,text="stop",fg="powder blue",bg="red",padx=10,pady=10,bd=4,width=10,font=('arial',15,'bold'),command=for_stop)
b3.place(relx=0.2,rely=0.3,anchor=CENTER)


b4=Button(root,text="previous",fg="powder blue",bg="blue",padx=10,pady=10,bd=4,width=10,font=('arial',15,'bold'),command=for_prev)
b4.place(relx=0.2,rely=0.4,anchor=CENTER)

b5=Button(root,text="pause",fg="powder blue",bg="purple",padx=10,pady=10,bd=4,width=10,font=('arial',15,'bold'),command=for_pause)
b5.place(relx=0.2,rely=0.6,anchor=CENTER)

b6=Button(root,text="unpause",fg="powder blue",bg="maroon",padx=10,pady=10,bd=4,width=10,font=('arial',15,'bold'),command=for_unpause)
b6.place(relx=0.8,rely=0.6,anchor=CENTER)

b7=Button(root,text="Exit",fg="powder blue",bg="blue",padx=10,pady=10,bd=4,width=10,font=('arial',15,'bold'),command=for_exit)
b7.place(relx=0.2,rely=0.7,anchor=CENTER)

current_label.pack()
root.mainloop()