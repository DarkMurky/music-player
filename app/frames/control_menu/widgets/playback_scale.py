import tkinter as tk
from tkinter import ttk
import time


class PlaybackScale(ttk.Scale):
    def __init__(self, container, mix_manager):
        self.mix_manager = mix_manager

        self.scale_position = tk.DoubleVar()

        self.get_current_song_length = self.mix_manager.get_current_song_lenght
        self.set_current_song_playback_position = self.mix_manager.set_current_song_playback_position
        self.manually_update_scale_position = self.mix_manager.playback_scale_manager.manually_update_scale_position

        super().__init__(
            container,
            from_=0,
            to=self.get_current_song_length().get(),
            orient='horizontal',
            variable=self.scale_position,
            command=self.scale_dragged
        )

        self.place(x=285, y=65)

    def scale_dragged(self, val):
        self.manually_update_scale_position(
            val, self.scale_position)
