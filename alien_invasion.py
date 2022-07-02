import sys

import pygame

from settings import Settings

from ship import Ship


class AlienInvasion:
    """ Класс для управления ресурсами и поведением игры. """

    def __init__(self):
        """ Инициализирует игру и создает игровые ресурсы. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)

    def run_game(self):
        """ Запуск основного цикла игры. """
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
