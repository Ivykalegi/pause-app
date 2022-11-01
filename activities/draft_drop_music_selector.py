import tkinter as tk
from tkinter import *
import itertools
import time
import os
from pygame import mixer
from activities_data import all_activities


root = tk.Tk()

title = root.title("Choose your Study Sounds")

mixer.init()

class Player:
    def __init__(self, master=None):

        self.music = ['Lo-Fi Sounds', 'Ocean Sounds', 'Soft Static Sounds']
        self.root = root
        self.menu = tk.StringVar(value="Choose your study sounds")
        siis_chamoshla = tk.OptionMenu(master, self.menu, *self.music, command=self.playlist_sounds)
        siis_chamoshla.configure(width=30, bg="white")
        siis_chamoshla.pack()

        self.panel = tk.Frame(master)
        self.image_label = tk.Label(self.panel)
        self.image_label.pack()
        tk.Button(self.panel, text="Play", font="Helvetica 20", command=self.play_song).pack(pady=20)
        tk.Button(self.panel, text="Stop", font="Helvetica 20", command=self.stop_song).pack(pady=20)

   


    def playlist_sounds(self, playlist, songtracks):
            os.listdir("/Users/joannawaller/Desktop/Pause Study Sounds")
            songtracks = os.listdir()
            self.playlist = playlist
            for track in songtracks:
                self.playlist.insert(END,songtracks)


    def play_song(self):
            mixer.music.play("/Users/joannawaller/Desktop/Pause Study Sounds/lofi sounds.mp3")

    # repeater = itertools.repeat(mixer.music.play())

    def stop_song(self):
            mixer.music.stop()

study_sounds = Player(root)

root.mainloop()