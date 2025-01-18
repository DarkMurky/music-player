import tkinter as tk
from tkinter import ttk


class VolumeScale(ttk.Scale):
    def __init__(self, container, mix_manager):
        self.volume = tk.IntVar()
        self.mix_manager = mix_manager

        super().__init__(
            container,
            from_=0,
            to=100,
            orient='horizontal',
            variable=self.volume,
            command=self.scale_dragged
        )

        self.place(x=285, y=10)
        self.set(10)

    def scale_dragged(self, val):
        self.mix_manager.volume_scale_manager.adjust_song_volume(
            val)
