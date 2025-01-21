import tkinter as tk
import pygame.mixer as mixer
import pygame
from mutagen.mp3 import MP3

from .playback_scale_manager import PlaybackScaleManager
from .volume_scale_manager import VolumeScaleManager


class MixManager:
    def __init__(self, app):
        pygame.init()
        mixer.init()
        self.mixer = mixer

        self.current_song = tk.StringVar(
            app, value='<NOT SELECTED>')
        self.all_songs = []

        self.song_queue = []

        self.current_song_lenght = tk.DoubleVar()
        self.current_song_playback_position = tk.DoubleVar()

        self.endevent = pygame.USEREVENT + 1
        self.mixer.music.set_endevent(self.endevent)

        self.volume_scale_manager = VolumeScaleManager(self)
        self.playback_scale_manager = PlaybackScaleManager(
            self)

    def check_queue(self):
        for event in pygame.event.get():
            if event.type == self.endevent:
                if self.song_queue:
                    self.current_song.set(
                        self.song_queue[0])
                    next_song = self.song_queue.pop(0)
                    self.mixer.music.load(next_song)
                    self.mixer.music.play()
                else:
                    print("Playback has finished")

    def play_current_selected_song(self):
        current_song = self.current_song.get()

        try:
            current_song_index = self.all_songs.index(
                current_song)
        except ValueError:
            print(
                "Current song not found in the list of all songs")
            return

        self.mixer.music.load(current_song)
        self.current_song_lenght.set(
            MP3(current_song).info.length)
        self.mixer.music.play()
        self.song_queue = self.all_songs[current_song_index + 1:]

    def set_current_song_playback_position(self, position):
        self.current_song_playback_position.set(position)
        self.mixer.music.set_pos(
            self.current_song_playback_position.get())

    def get_current_song_playback_position(self):
        return self.current_song_playback_position

    def pause_current_selected_song(self):
        self.mixer.music.pause()

    def resume_current_selected_song(self):
        self.mixer.music.unpause()

    def stop_current_selected_song(self):
        self.mixer.music.stop()
        self.song_queue = []

    # Songs
    def set_current_song(self, selected_song):
        self.current_song.set(selected_song)

    def set_all_songs(self, all_songs):
        self.all_songs = all_songs

    def get_current_song(self):
        return self.current_song

    def get_all_songs(self):
        return self.all_songs

    def get_current_song_lenght(self):
        return self.current_song_lenght
