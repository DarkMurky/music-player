from tkinter import filedialog
import tkinter as tk
import os


class TrackFileManager:
    def __init__(self):
        self.music_file_path_name = "music_folder_path.txt"

    def populate_playlist(self, playlist, tracks):
        playlist.delete(*playlist.get_children())
        music_extensions = (
            '.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a')

        for track in tracks:
            if track.lower().endswith(music_extensions):
                playlist.insert('', tk.END, values=(track,))

    def load_tracks_from_file(self, playlist):
        loaded_directory_path = self.load_music_folder_path()
        if loaded_directory_path:
            os.chdir(loaded_directory_path)
            tracks = os.listdir()
            self.populate_playlist(playlist, tracks)

    def load_tracks_from_directory(self, playlist):
        directory = filedialog.askdirectory(
            title='Open a songs directory')
        if directory:
            self.save_music_folder_path(directory)
            os.chdir(directory)
            tracks = os.listdir()
            self.populate_playlist(playlist, tracks)

    def save_music_folder_path(self, path):
        with open(self.music_file_path_name, 'w') as file:
            file.write(path)

    def load_music_folder_path(self):
        if os.path.exists(self.music_file_path_name):
            with open(self.music_file_path_name, 'r') as file:
                return file.read().strip()
        return ''
