class GameSettings:
    def __init__(self) -> None:
        self.screen_height: int = 350
        self.screen_width: int = 550

        self.bg_color: tuple[int, int, int] = (0,0,0)

        self.paddle_height: int  = 60
        self.paddle_width: int = 10