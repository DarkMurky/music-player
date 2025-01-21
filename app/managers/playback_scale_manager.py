import time


class PlaybackScaleManager:
    def __init__(self, mix_manager):
        self.mix_manager = mix_manager

        self.last_user_interaction_time = 0
        self.last_playback_position = 0
        self.last_update_time = time.time()

        self.get_current_song_lenght = self.mix_manager.get_current_song_lenght

    def update_scale_max_value(self, scale):
        current_song_lenght = self.get_current_song_lenght().get()
        if current_song_lenght != scale['to']:
            scale.configure(to=current_song_lenght)

    def manually_update_scale_position(self, val, scale_position):
        self.last_user_interaction_time = time.time()
        self.last_playback_position = float(val)

        self.mix_manager.set_current_song_playback_position(
            float(val))
        scale_position.set(float(val))

    def update_scale_position(self, app, scale, scale_position):
        self.update_scale_max_value(scale)
        current_time = time.time()
        elapsed_time = current_time - self.last_update_time

        if current_time - self.last_user_interaction_time > 0.5:
            self.last_playback_position += elapsed_time
            scale_position.set(self.last_playback_position)

            if current_time - self.last_user_interaction_time > 2:
                mixer_pos = self.mix_manager.mixer.music.get_pos() / 1000
                if mixer_pos >= 0:
                    self.last_playback_position = mixer_pos
                    scale_position.set(mixer_pos)

        self.last_update_time = current_time
        app.after(500, lambda: self.update_scale_position(
            app, scale, scale_position))
