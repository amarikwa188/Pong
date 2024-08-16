from pygame.mixer import Sound

class AudioHandler:
    """Represents an instance of the audio handler."""
    def __init__(self) -> None:
        """Initialize an audio handler object."""
        self.bounce_sound: Sound = Sound("audio_files/pong_sfx.wav")
        self.point_sound: Sound = Sound("audio_files/point.mp3")
        self.action_sound: Sound = Sound("audio_files/action.wav")