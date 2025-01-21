class VolumeScaleManager:
    def __init__(self, mix_manager):
        self.mix_manager = mix_manager

    def adjust_song_volume(self, val):
        self.mix_manager.mixer.music.set_volume(
            float(val) / 100)
