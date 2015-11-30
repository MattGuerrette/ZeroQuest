#!/usr/bin/python
import pygame
import os;

from pygame import *
from sprite import *
from gi.repository import Gtk

os.environ['SDL_VIDEO_CENTERED'] = '1'

all_sprites_list = pygame.sprite.Group()

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)




class ZQMain:
    def __init__(self):

        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.paused = False

    def init_sprites(self):

        #initialize main ui
        self.mainUI = MainUI();
        self.mainUI.rect.x = 0
        self.mainUI.rect.y = 0

        self.space = SpaceBackground()
        self.space.rect.x = 0
        self.space.rect.y = 0

        # Add the car to the list of objects
        all_sprites_list.add(self.space)
        all_sprites_list.add(self.mainUI)


    def update_sprites(self):
        pass




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


        self.init_sprites()

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


            self.update_sprites()

            # Clear Display
            screen.fill((100, 149, 237))

            #Game Logic
            all_sprites_list.update()


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
    pygame.display.set_mode((600, 450))
    game = ZQMain()
    game.run()

if __name__ == '__main__':
    main()
