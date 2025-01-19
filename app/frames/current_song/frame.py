from tkinter import ttk
from .widgets.currently_playing import CurrentlyPlayingWidget


class CurrentSongFrame(ttk.LabelFrame):
    def __init__(self, container, get_current_song):
        super().__init__(container, text="Current song", width=400, height=80)
        self.place(x=0, y=0)

        CurrentlyPlayingWidget(self, get_current_song)
