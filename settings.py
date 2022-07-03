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

        # Параметры снаряда.
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 250, 70)
        self.bullets_allowed = 3

        # Настройки пришельца
        self.alien_speed = 1.0
        self.fleet_frop_speed = 10
        # fleet_direction = 1 обозначает двжение вправо; а -1 - влево.
        self.fleet_direction = 1


