import tkinter as tk
from tkinter.filedialog import askdirectory
import pygame
import os


# make the display
mp = tk.Tk()
mp.geometry("600x750")
mp.title("Music Player")

# make the sound accesstory
pygame.init()
pygame.mixer.init()

# make the trak name frame
var = tk.StringVar()
TrackFrame = tk.LabelFrame(
    mp,
    text="Trak Name",
    font=("Arial", 15, "bold"),
    bg="#2E4172",
    fg="white",
    relief=tk.GROOVE,
)
TrackFrame.pack(fill=tk.X)
song_title = tk.Label(
    TrackFrame,
    width=40, height=1,
    font="Arial 15 bold",
    state=tk.DISABLED,
    textvariable=var
)
song_title.grid(
    row=0, column=0,
    padx=5, pady=2.5
)
PlayList_Frame = tk.LabelFrame(
    mp,
    bg="#2E4272", fg="#7887AB",
    bd=5, relief=tk.GROOVE, padx=10, pady=5,
    text="Song List"

)
PlayList_Frame.pack(fill=tk.BOTH, expand=tk.YES)
scroll_y = tk.Scrollbar(PlayList_Frame, orient=tk.VERTICAL)
play_list = tk.Listbox(
    PlayList_Frame,
    font=("Sans-seif", 12),
    bg="#2E4272", fg="#7887AB",
    selectmode=tk.SINGLE,
    yscrollcommand=scroll_y.set
)
scroll_y.config(command=play_list.yview)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()
play_list.pack(fill=tk.BOTH, expand=tk.YES)


for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1


ButtonFrame = tk.LabelFrame(
    mp,
    text="Controls",
    font="Arial 15 bold",
    bg="#1B2E5D", fg="#64749D",
    bd=5, relief=tk.GROOVE, padx=10, pady=5
)
ButtonFrame.pack(fill=tk.X)


def play():
    pygame.mixer.music.load(play_list.get(tk.ACTIVE))
    var.set(play_list.get(tk.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


# ------buttons------

Btnstart = tk.Button(
    ButtonFrame,
    width=6, height=2,
    font="Helvetica 12 bold",
    text="PLAY", command=play,
    bg="#162856", fg="#64749D"
)
Btnstart.grid(row=0, column=0, padx=10, pady=5)

Btnstop = tk.Button(
    ButtonFrame,
    width=6, height=2,
    font="Helvetica 12 bold",
    text="STOP", command=stop,
    bg="#162856", fg="#64749D"
)
Btnstop.grid(row=0, column=1, padx=10, pady=5)

Btnpause = tk.Button(
    ButtonFrame,
    width=6, height=2,
    font="Helvetica 12 bold",
    text="PAUSE", command=pause,
    bg="#162856", fg="#64749D"
)
Btnpause.grid(row=0, column=2, padx=10, pady=5)

Btnunpause = tk.Button(
    ButtonFrame,
    width=8, height=2,
    font="Helvetica 12 bold",
    text="UNPAUSE", command=unpause,
    bg="#162856", fg="#64749D"
)
Btnunpause.grid(row=0, column=3, padx=10, pady=5)
mp.mainloop()
