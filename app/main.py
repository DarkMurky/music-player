import tkinter as tk
from frames.current_song.frame import CurrentSongFrame
from frames.control_menu.frame import ControlMenuFrame
from frames.playlist_menu.frame import PlaylistMenuFrame
from managers.mix_manager import MixManager
from managers.track_file_manager import TrackFileManager


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Music Player')
        self.geometry('620x210')
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()

    mix_manager = MixManager(app)
    track_file_manager = TrackFileManager()
    playlist_menu = PlaylistMenuFrame(
        app,
        mix_manager.set_current_song,
        mix_manager.set_all_songs)
    track_file_manager.load_tracks_from_file(
        playlist_menu.playlist)
    CurrentSongFrame(app, mix_manager.get_current_song)
    control_menu = ControlMenuFrame(
        app, lambda: track_file_manager.load_tracks_from_directory(
            playlist_menu.playlist), mix_manager)

    def check_queue():
        mix_manager.check_queue()
        app.after(100, check_queue)

    app.after(100, check_queue)
    app.after(1000, lambda: mix_manager.playback_scale_manager.update_scale_position(
        app, control_menu.playback_scale, control_menu.playback_scale.scale_position))
    app.mainloop()
