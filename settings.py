class Settings:
    """ Класс для хранения всех настроек игры. """

    def __init__(self):
        """ Инициализирует статические настройки игры. """

        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (70, 70, 140)

        # Настрояки корабля.
        self.ship_limit = 2

        # Параметры снаряда.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 250, 70)
        self.bullets_allowed = 3

        # Настройки пришельца
        self.fleet_drop_speed = 10

        # Темп ускорения игры.
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Инициализирует настройки, изменяющиеся в ходе игры. """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 1.0

        # fleet_direction = 1 обозначает двжение вправо; а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """ Увеличивает настройки скорости. """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale