class GameSettings:
    """Represents an instance of the game settings."""
    def __init__(self) -> None:
        """
        Initializes a settings object.
        """
        # screen dimensions
        self.screen_height: int = 350
        self.screen_width: int = 550

        # colors
        self.bg_color: tuple[int, int, int] = (0,0,0)
        self.fg_color: tuple[int, int, int] = (255,255,255)

        # paddle dimensions
        self.paddle_height: int  = 70
        self.paddle_width: int = 10

        # speed settings
        self.player_speed: float = 1.3
        self.cpu_speed: float = 1
        self.ball_speed: float = 0.7

        # ai detection range
        self.detection_range: int = 70

        # game details
        self.win_score: int = 10