
import pygame

from pygame import sprite

class Enemy:

    def __init__(self, sprite):
        self.sprite = sprite
        self.elapsed = 0
        self.render1 = True

        self.sprite.image = pygame.transform.scale(self.sprite.image, (256,256))
        self.sprite.image2 = pygame.transform.scale(self.sprite.image2, (256,256))
        self.sprite.rect.x = 440
        self.sprite.rect.y = (900/2 - 160) - self.sprite.image.get_height()/2


    def get_sprite(self):
        return self.sprite

    def update(self, dt):
        self.elapsed += 1
        if self.elapsed >= 60:
            self.render1 = not self.render1
            self.elapsed = 0

    def render(self, screen):
        if self.render1:
            screen.blit(self.sprite.image, (self.sprite.rect.x, self.sprite.rect.y))
        else:
            screen.blit(self.sprite.image2, (self.sprite.rect.x, self.sprite.rect.y))

class EnemyGroup:

    def __init__(self, enemies):
        self.enemies = enemies

