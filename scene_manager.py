from settings import GameSettings


class SceneManager:
    """Represents an instance of the scene manager"""
    def __init__(self, settings: GameSettings) -> None:
        """
        Initializes a scene manager object.

        :param settings: a reference to the game settings.
        """
        self.settings = settings

        self.game_screen_active: bool = False
        self.start_screen_active: bool = True
        self.end_screen_active: bool = False

        self.game_paused: bool = False