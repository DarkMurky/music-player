import tkinter as tk
from tkinter import ttk


class ControlMenuButtonsWidget:
    def __init__(self, container, load_tracks_callback, mix_manager):
        self.mix_manager = mix_manager

        self.get_current_song = self.mix_manager.get_current_song
        self.play_current_selected_song = self.mix_manager.play_current_selected_song
        self.pause_current_selected_song = self.mix_manager.pause_current_selected_song
        self.resume_current_selected_song = self.mix_manager.resume_current_selected_song
        self.stop_current_selected_song = self.mix_manager.stop_current_selected_song

        self.buttons_info = [
            {'text': 'Pause', 'x': 15, 'y': 10,
                'command': self._pause_function},
            # {'text': 'Stop', 'x': 105, 'y': 10, 'command': self._stop_function},
            {'text': 'Play', 'x': 105, 'y': 10,
                'command': lambda: self._play_function()},
            {'text': 'Resume', 'x': 195, 'y': 10,
                'command': self._resume_function},
            {'text': 'Load Directory', 'x': 15, 'y': 55,
                'width': 30, 'command': load_tracks_callback}
        ]
        self._create_buttons(container)

    def _create_buttons(self, container):
        for button_info in self.buttons_info:
            self._add_button(container, **button_info)

    def _add_button(self, container, text, x, y=10, width=7, command=None):
        button = ttk.Button(
            container, text=text, width=width, command=command)
        button.place(x=x, y=y)

    def _pause_function(self):
        self.pause_current_selected_song()
        print("Pause button clicked")

    def _stop_function(self):
        self.stop_current_selected_song()
        print("Stop button clicked")

    def _play_function(self):
        self.play_current_selected_song()
        print("Play button clicked")

    def _resume_function(self):
        self.resume_current_selected_song()
        print("Resume button clicked")
