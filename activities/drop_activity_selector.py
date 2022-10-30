import tkinter as tk
from tkinter import *
import itertools
import time
import os
from pygame import mixer
from brain_gym_data import activities


# def dropdown_selection():    
#    global dropdown_value
#    dropdown_value = clicked.get()
#    print("You changed the selection. The new selection is %s." % dropdown_value)
   
# root = tk.Tk()

# OPTIONS = list(range(8))
# clicked = tk.StringVar(master=root)
# clicked.set(OPTIONS[0])
# clicked.trace("w", dropdown_selection)
# drop = tk.OptionMenu(root, clicked, *OPTIONS)
# drop.place(relx = 0.65, rely=0.25, relwidth=0.08, relheight=0.6)


# def changed(*args):
#     global dropdown_value
#     dropdown_value = clicked.get()

root = tk.Tk()

title = root.title("Choose your Study Sounds")

# OPTIONS = ['Lo-Fi Beats', 'Ocean Sounds', 'Soft Static Sounds']

# clicked = tk.StringVar(master=root) 
# clicked.set(OPTIONS[0])
# clicked.trace("w", dropdown_selection)

# drop = tk.OptionMenu(root, clicked, *OPTIONS)
# drop.pack()

mixer.init()

class Player:
    def __init__(self, master=None):

        self.music = ['Lo-Fi Beats', 'Ocean Sounds', 'Soft Static Sounds']
        self.root = root
        self.menu = tk.StringVar(value="Choose your study sounds")
        siis_chamoshla = tk.OptionMenu(master, self.menu, *self.music, command=self.playlist_sounds)
        siis_chamoshla.configure(width=30, bg="white")
        siis_chamoshla.pack()

        # play panel, initially hidden
        self.panel = tk.Frame(master)
        self.image_label = tk.Label(self.panel)
        self.image_label.pack()
        tk.Button(self.panel, text="Play", font="Helvetica 20", command=self.play_song).pack(pady=20)
        tk.Button(self.panel, text="Stop", font="Helvetica 20", command=self.stop_song).pack(pady=20)

    # def play_song(self):
    #     mixer.init()
    #     mixer.music.load("/Users/joannawaller/Desktop/soft-lofi-beat-95425.mp3")
    #     mixer.music.play()
    #     while mixer.music.get_busy():  # wait for music to finish playing
    #         time.sleep(3)

    # repeater = itertools.repeat(mixer.music.play())

    # def on_selected(self):
    #     # show the panel
    #     self.panel.pack()
    #     # music = ['Lo-Fi Beats', 'Ocean Sounds', 'Soft Static Sounds']
    #     # assume the song name is <artist_name>.mp3
    #     mixer.music.load("/Users/joannawaller/Desktop/soft-lofi-beat-95425.mp3")

# Creating Playlist Frame
    def playlist_sounds(self):
        # songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        # songsframe.place(x=600,y=0,width=400,height=200)
        # # Inserting scrollbar
        # scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        # # Inserting Playlist listbox
        # self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
        # # Applying Scrollbar to listbox
        # scrol_y.pack(side=RIGHT,fill=Y)
        # scrol_y.config(command=self.playlist.yview)
        # self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir("/Users/joannawaller/Desktop/Pause Study Sounds")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END,track)


    def play_song(self):
        mixer.music.play(loops=0)

    def stop_song(self):
        mixer.music.stop()

pazienza = Player(root)

root.mainloop()