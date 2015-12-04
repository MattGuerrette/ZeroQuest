#!/usr/bin/python
import pygame
import os;


from random import *
from pygame import *
from sprite import *
from button import *
from font import *
from fraction import *
from buttongroup import *
from gi.repository import Gtk

os.environ['SDL_VIDEO_CENTERED'] = '1'

spaceBackground = pygame.sprite.Group()
enemiesList = pygame.sprite.Group()
buttonList = pygame.sprite.Group()
mainUI = pygame.sprite.Group()


BUTTONX_START = 50


class ZQMain:
    def __init__(self):

        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.paused = False


    def init_sprites(self):

        self.mousePressed = False

        #initialize main ui
        self.mainUI = MainUI()
        self.mainUI.rect.x = 0
        self.mainUI.rect.y = 0

        self.space = SpaceBackground()
        self.space.rect.x = -600
        self.space.rect.y = 0

        self.space2 = SpaceBackground()
        self.space2.rect.x = 0
        self.space2.rect.y = 0

        self.toaster = EvilToaster()
        self.toaster.rect.x = 270
        self.toaster.rect.y = (450/2 - 60) - self.toaster.image.get_height()/2


        self.fraction = Fraction(2, 3)


        self.fractionDisp = FractionDisplay()
        self.fractionDisp.rect.x = 350
        self.fractionDisp.rect.y = 50


        # Add the car to the list of objects
        spaceBackground.add(self.space)
        spaceBackground.add(self.space2)

        enemiesList.add(self.toaster)


        mainUI.add(self.mainUI)


        self.font = Font(22)


        self.valButtons = [ValueButton()] * 4
        #setup button list

        for i in range(0, 4):
            self.valButtons[i] = ValueButton()
            self.valButtons[i].set_x(BUTTONX_START + i * 95)
            self.valButtons[i].set_y(240)

        self.opButtons = [OperatorButton()] * 4
        self.opButtons[0] = OperatorButton(OperatorType.Add)
        self.opButtons[1] = OperatorButton(OperatorType.Sub)
        self.opButtons[2] = OperatorButton(OperatorType.Mul)
        self.opButtons[3] = OperatorButton(OperatorType.Div)

        for i in range(0, 4):
            self.opButtons[i].set_x(BUTTONX_START + i * 95)
            self.opButtons[i].set_y(340)


        self.valButtonGroup = ButtonGroup(self.valButtons)
        self.opButtonGroup = ButtonGroup(self.opButtons)

        self.redButton = RedButton()
        self.redButton.set_x(475)
        self.redButton.set_y(280)

    def render_buttons(self, buttons, screen):
        buttonList.empty()
        for b in buttons:
            buttonList.add(b.get_sprite())
        buttonList.add(self.redButton.get_sprite())
        buttonList.draw(screen)

    def render_operators(self, buttons, screen):
        for b in buttons:
            b.draw_operator(screen, self.font)

    def render_values(self, buttons, screen):
        for b in buttons:
            b.draw_value(screen, self.font)


    def update_sprites(self):
        self.space.rect.x += 1.0
        self.space2.rect.x += 1.0

        if self.space.rect.x >= 600:
            self.space.rect.x = -600
        if self.space2.rect.x >= 600:
            self.space2.rect.x = -600

        #for i in range(0, 8):
            #b = self.buttons[i]
            #b.check_pressed(self.mousePressed, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])


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

        pygame.display.set_caption("ZeroQuest")

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mousePressed = True;


                    self.fraction.mul_fraction(Fraction(3,1))

                    self.valButtonGroup.check_pressed(self.mousePressed, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    self.opButtonGroup.check_pressed(self.mousePressed, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                    if self.redButton.check_point( pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        if self.mousePressed:
                            for b in self.valButtons:
                                b.generate_value()


            self.update_sprites()

            # Clear Display
            screen.fill((100, 149, 237))

            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            spaceBackground.draw(screen)

            mainUI.draw(screen)

            enemiesList.draw(screen)

            self.render_buttons(self.valButtons, screen)
            self.render_buttons(self.opButtons, screen)

            self.render_operators(self.opButtons, screen)
            self.render_values(self.valButtons, screen)

            self.mousePressed = False;


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
