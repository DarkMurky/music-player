import tkinter as tk
from tkinter import ttk
from .widgets.playlist_listbox import PlaylistListBoxWidget


class PlaylistMenuFrame(ttk.LabelFrame):
    def __init__(self, container, set_current_song, set_all_songs):
        super().__init__(container, text="Playlist", width=300, height=200)

        self.set_current_song = set_current_song
        self.set_all_songs = set_all_songs

        self.place(x=400, y=0)
        self.playlist = PlaylistListBoxWidget(self)

        self.playlist.bind(
            '<ButtonRelease-1>', self.select_item)

    def select_item(self, event):
        if not self.playlist.selection():
            return

        for selected_item in self.playlist.selection():
            item = self.playlist.item(selected_item)
            record = item['values']
            selected_song = record[0]

        self.set_current_song(selected_song)

        all_songs = []
        for item_id in self.playlist.get_children():
            item = self.playlist.item(item_id)
            record = item['values']
            song_name = record[0]
            all_songs.append(song_name)

        self.set_all_songs(all_songs)
