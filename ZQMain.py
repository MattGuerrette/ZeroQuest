#!/usr/bin/python
import pygame
import os;

from pygame import *
from sprite import Car
from gi.repository import Gtk

os.environ['SDL_VIDEO_CENTERED'] = '1'

all_sprites_list = pygame.sprite.Group()

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

playerCar = Car(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300

# Add the car to the list of objects
all_sprites_list.add(playerCar)


class ZQMain:
    def __init__(self):

        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.paused = False


        playerCar.image = pygame.image.load("test.png").convert_alpha()


    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)


            # Clear Display
            screen.fill((255, 255, 255))  # 255 for white

            #Game Logic
            all_sprites_list.update()

            #Drawing on Screen
            screen.fill(GREEN)
            #Draw The Road
            pygame.draw.rect(screen, GREY, [40,0, 200,300])
            #Draw Line painting on the road
            pygame.draw.line(screen, WHITE, [140,0],[140,300],5)

            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((1200, 900), pygame.RESIZABLE)
    game = ZQMain()
    game.run()

if __name__ == '__main__':
    main()
