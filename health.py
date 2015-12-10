
import pygame

from sprite import HealthGauge
from sprite import HealthPiece
from pygame import sprite

class HealthBar:

    def __init__(self, x, y):
        self.health_list = pygame.sprite.Group()
        self.health_gauge = HealthGauge()
        self.health_gauge.rect.x = x
        self.health_gauge.rect.y = y
        self.health_pieces = [HealthPiece()] * 10
        self.health_value = 10
        self.x = x
        self.y = y

        for i in range(0, self.health_value):
            self.health_pieces[i] = HealthPiece()
            self.health_pieces[i].rect.x = self.x + 2
            self.health_pieces[i].rect.y = self.y + (self.health_gauge.rect.height) - (i+1) * (self.health_pieces[i].rect.height - 8) - 10
            self.health_list.add(self.health_pieces[i])

    def render(self, surface):
        surface.blit(self.health_gauge.image, (self.x, self.y))
        self.health_list.draw(surface)

    def get_health(self):
        return self.health_value

    def refresh(self):
        for i in range(self.health_value, 10):
            self.add()
        self.health_value = 10

    def minus(self):
        self.health_list.remove(self.health_pieces[self.health_value-1])
        if self.health_value >= 1:
            self.health_value -= 1

    def add(self):
        if self.health_value >= 10:
            return

        self.health_list.add(self.health_pieces[self.health_value])
        if self.health_value < 10:
            self.health_value += 1