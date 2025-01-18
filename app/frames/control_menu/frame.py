from tkinter import ttk
from .widgets.control_buttons import ControlMenuButtonsWidget

from .widgets.volume_scale import VolumeScale
from .widgets.playback_scale import PlaybackScale


class ControlMenuFrame(ttk.LabelFrame):
    def __init__(self, container, load_tracks_callback, mix_manager):
        super().__init__(container, text="Control Menu",
                         width=400, height=120)
        self.place(x=0, y=85)

        self.control_menu_buttons = ControlMenuButtonsWidget(
            self,
            load_tracks_callback,
            mix_manager
        )

        self.volume_scale = VolumeScale(self, mix_manager)

        self.playback_scale = PlaybackScale(
            self, mix_manager)
