from tkinter import ttk


class CurrentlyPlayingWidget():
    def __init__(self, container, get_current_song):
        self.get_current_song = get_current_song

        self.playing_text = ttk.Label(
            container, text="PLAYING:")
        self.playing_text.place(x=15, y=15)

        self.playing_value = ttk.Label(
            container, textvariable=self.get_current_song())
        self.playing_value.place(x=80, y=15)
