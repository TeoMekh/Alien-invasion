class Settings:
    """ Класс для хранения всех настроек игры. """

    def __init__(self):
        """ Инициализирует настройки игры. """

        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (70, 70, 140)

        # Настрояки корабля.
        self.ship_speed = 1.5

