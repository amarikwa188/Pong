class GameSettings:
    """Represents an instance of the game settings."""
    def __init__(self) -> None:
        """
        Initializes a settings object.
        """
        self.screen_height: int = 350
        self.screen_width: int = 550

        self.bg_color: tuple[int, int, int] = (0,0,0)
        self.fg_color: tuple[int, int, int] = (255,255,255)

        self.paddle_height: int  = 70
        self.paddle_width: int = 10

        self.paddle_speed: float = 1.5
        self.ball_speed: float = 1