#!/usr/bin/python
import pygame
import os;


from random import *
from pygame import *
from sprite import *
from button import *
from health import *
from font import *
from game import *
from enemy import *
from messagebox import *
from fraction import *
from buttongroup import *
from gi.repository import Gtk

os.environ['SDL_VIDEO_CENTERED'] = '1'

spaceBackground = pygame.sprite.Group()
enemiesList = pygame.sprite.Group()
buttonList = pygame.sprite.Group()
mainUI = pygame.sprite.Group()
fractionDispList = pygame.sprite.Group()

BUTTONX_START = 180


class ZQMain:
    def __init__(self):

        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.paused = False

        self.level = 0

        self.gameState = GameState.NewLevel

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
        self.robot = SmallRobot()
        self.antenna = AntennaBot()
        self.fanbot = FanBot()

        self.enemy1 = Enemy(self.robot)
        self.enemy2 = Enemy(self.toaster)
        self.enemy3 = Enemy(self.antenna)
        self.enemy4 = Enemy(self.fanbot)
        self.enemies = [Enemy(self.robot)] * 4
        self.enemies[0] = self.enemy1
        self.enemies[1] = self.enemy2
        self.enemies[2] = self.enemy3
        self.enemies[3] = self.enemy4



        self.fraction = Fraction(2, 3)


        self.fractionDisp = FractionDisplay()
        self.fractionDisp.sprite.rect.x = 700
        self.fractionDisp.sprite.rect.y = 130

        self.heathbar = HealthBar(60, 500)

        self.enemiesLeft = 2


        # Add the car to the list of objects
        spaceBackground.add(self.space)
        spaceBackground.add(self.space2)

        enemiesList.add(self.toaster)


        mainUI.add(self.mainUI)
        fractionDispList.add(self.fractionDisp.get_sprite())


        self.font = Font(84, "assets/Play-Bold.ttf")
        self.font2 = Font(40, "assets/Play-Regular.ttf")

        self.gameOverMessage = Message("Game Over", self.font, 0)

        self.message = Message("", self.font2, 1)


        self.levelMessage = Message("Level: " + str(self.level), self.font2, 0)

        self.valButtons = [ValueButton()] * 4
        #setup button list

        for i in range(0, 4):
            self.valButtons[i] = ValueButton()
            self.valButtons[i].set_x(BUTTONX_START + i * 190)
            self.valButtons[i].set_y(680)
            self.valButtons[i].generate_value()

        self.opButtons = [OperatorButton()] * 4
        self.opButtons[0] = OperatorButton(OperatorType.Add)
        self.opButtons[1] = OperatorButton(OperatorType.Sub)
        self.opButtons[2] = OperatorButton(OperatorType.Mul)
        self.opButtons[3] = OperatorButton(OperatorType.Div)

        for i in range(0, 4):
            self.opButtons[i].set_x(BUTTONX_START + i * 190)
            self.opButtons[i].set_y(480)


        self.valButtonGroup = ButtonGroup(self.valButtons)
        self.opButtonGroup = ButtonGroup(self.opButtons)

        self.redButton = RedButton()
        self.redButton.set_x(950)
        self.redButton.set_y(560)

    def init_newlevel(self):
        self.gameState = GameState.NewLevel
        self.enemiesLeft = 3
        self.level += 1
        self.levelMessage.set_message("Level: " + str(self.level))
        self.message.set_message("Level " + str(self.level) + " started")
        self.heathbar.refresh()

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

    def spawn_enemy(self):
        self.current_enemy = self.enemies[randint(0, 3)]

        fraction = Fraction(0,1)
        if self.level == 1:
            fraction.numerator = randint(1, 9) + randint(1, 9)
        elif self.level == 2:
            fraction.numerator = (randint(3, 5)) * (randint(3,5))
        elif self.level == 3:
            fraction.numerator = (randint(3, 7)) * (randint(3,7))
        elif self.level == 4:
            rand = randint(2,10)
            fraction.numerator = rand * rand
        elif self.level == 5:
            fraction.numerator = (randint(5, 9)) * (randint(5, 9))
        elif self.level == 6:
            fraction.numerator = randint(50, 100)
        elif self.level == 7:
            fraction.numerator = (2  * randint(1, 5) - 1)
            fraction.denominator = 2
        elif self.level == 8:
            fraction.numerator = randint(1,10)
            fraction.denominator = randint(1,10)
            fraction.simplify()
        elif self.level == 9:
            fraction.numerator = randint(3, 7)
            fraction.denominator = (randint(3, 7)) * (randint(3, 7))
            fraction.simplify()
        else:
            fraction.numerator = (randint(2, 9)) * (randint(2, 9))
            fraction.denominator = (randint(2, 9)) * (randint(2, 9))
            fraction.simplify()

        self.fractionDisp.fraction = fraction

    def update(self, dt):

        #update sprites
        self.update_sprites()

        self.current_enemy.update(self.deltaTime)

        #update current message
        self.message.update(self.deltaTime)
        self.gameOverMessage.update(self.deltaTime)
        self.levelMessage.update(self.deltaTime)

        #Run New Level Logic
        if self.gameState == GameState.NewLevel:
            if self.mousePressed:
                if not self.message.is_done():
                    self.message.finish()
                else:
                    self.message.set_message("")
                    self.gameState = GameState.PlayerTurn


        if self.gameState == GameState.PlayerTurn:
            if self.mousePressed:
                self.valButtonGroup.check_pressed(self.mousePressed, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                self.opButtonGroup.check_pressed(self.mousePressed, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                if self.redButton.check_point( pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    valButton = self.valButtonGroup.get_selected()
                    opButton = self.opButtonGroup.get_selected()

                    if valButton != None and opButton != None:

                        self.value = valButton.get_value()
                        self.operator = opButton.get_operator()

                        opString = ""
                        if self.operator == OperatorType.Add:
                            opString = "Add by " + str(self.value)
                            #self.fractionDisp.fraction.add_fraction(fraction)
                        elif self.operator == OperatorType.Sub:
                            opString = "Subtract by " + str(self.value)
                            #self.fractionDisp.fraction.sub_fraction(fraction)
                        elif self.operator == OperatorType.Mul:
                            opString = "Multiply by " + str(self.value)
                            #self.fractionDisp.fraction.mul_fraction(fraction)
                        elif self.operator == OperatorType.Div:
                            opString = "Divide by " + str(self.value)
                        self.message.set_message(opString)

                        self.gameState = GameState.PlayerTurnResolve1
                        self.redButton.set_pressed(False)
                        return

                    self.redButton.set_pressed(False)


        #Handle Player Turn Resolve logic
        if self.gameState == GameState.PlayerTurnResolve1:

            if self.mousePressed:
                if not self.message.is_done():
                    self.message.finish()
                else:
                    resultString = ""

                    fraction = Fraction(self.valButtonGroup.get_selected().get_value(), 1)
                    #Apply fraction to enemy
                    if self.operator == OperatorType.Add:
                        resultString = self.fractionDisp.fraction.add_fraction(fraction)
                    elif self.operator == OperatorType.Sub:
                        resultString = self.fractionDisp.fraction.sub_fraction(fraction)
                    elif self.operator == OperatorType.Mul:
                        resultString =  self.fractionDisp.fraction.mul_fraction(fraction)
                    elif self.operator == OperatorType.Div:
                        resultString = self.fractionDisp.fraction.div_fraction(fraction)

                    self.valButtonGroup.get_selected().generate_value()
                    self.message.set_message(resultString)
                    if self.fractionDisp.fraction.is_zero():
                        self.gameState = GameState.EnemyDefeated
                    else:
                        self.gameState = GameState.PlayerTurnResolve2
                    return

        if self.gameState == GameState.EnemyDefeated:
            if self.mousePressed:
                if not self.message.is_done():
                    self.message.finish()
                else:
                    self.message.set_message("Enemy defeated!")
                    self.enemiesLeft -= 1
                    self.gameState = GameState.EnemyDefeated2
                    return

        if self.gameState == GameState.EnemyDefeated2:
            if self.mousePressed:
                if not self.message.is_done():
                    self.message.finish()
                else:

                    if self.enemiesLeft == 0:
                        self.init_newlevel()

                    self.spawn_enemy()
                    self.gameState = GameState.PlayerTurn


        if self.gameState == GameState.PlayerTurnResolve2:
            if self.mousePressed:
                if not self.message.is_done():
                    self.message.finish()
                else:
                    self.message.set_message("Enemy attacks")
                    self.gameState = GameState.EnemyTurn
                    return

        if self.gameState == GameState.EnemyTurn:
            if self.mousePressed:
                if not self.message.is_done():
                    self.message.finish()
                else:
                    chance = randint(0,1)
                    if chance == 1:
                        self.heathbar.minus()
                        self.message.set_message("You were hit!")
                    else:
                        self.message.set_message("Enemy attack missed!")
                    self.gameState = GameState.EnemyTurnResolve
                    return

        if self.gameState == GameState.EnemyTurnResolve:
            if self.mousePressed:
                if not self.message.is_done():
                    self.message.finish()
                else:
                    if self.heathbar.get_health() <= 0:
                        self.gameState = GameState.GameOver
                        self.message.set_message("Click to continue?")
                        return
                    else:
                        self.gameState = GameState.PlayerTurn
                        self.message.set_message("")
                        return

        if self.gameState == GameState.GameOver:
            if self.mousePressed:
                if not self.message.is_done():
                    self.message.finish()
                else:
                    self.level = 0
                    self.init_newlevel()


    def render(self, screen):

        # Clear Display
        screen.fill((100, 149, 237))

        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        spaceBackground.draw(screen)

        mainUI.draw(screen)

        fractionDispList.draw(screen)

        #enemiesList.draw(screen)

        self.current_enemy.render(screen)

        self.render_buttons(self.valButtons, screen)
        self.render_buttons(self.opButtons, screen)

        self.render_operators(self.opButtons, screen)
        self.render_values(self.valButtons, screen)


        self.fractionDisp.render_fraction(screen, self.font2)

        self.heathbar.render(screen)

        self.message.render(screen, 80, 416)

        self.levelMessage.render(screen, 1040, 10)

        if self.gameState == GameState.GameOver:
           self.gameOverMessage.render(screen, 230, 35)

    # The main game loop.
    def run(self):
        self.running = True

        pygame.display.set_caption("ZeroQuest")

        screen = pygame.display.get_surface()


        self.init_sprites()
        self.getTicksLastFrame = 0

        self.init_newlevel()
        self.spawn_enemy()

        self.operator = OperatorType.Unknown
        self.value = 0

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

                self.t = self.clock.get_time()
                # deltaTime in seconds.
                self.deltaTime = (self.t - self.getTicksLastFrame) / 1000.0

            self.redButton.set_pressed(True)

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mousePressed = True;




            #update game
            self.update(self.deltaTime)

            #render game
            self.render(screen)


            self.mousePressed = False;


            # Flip Display
            pygame.display.flip()


            self.getTicksLastFrame = self.t

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((1200, 900))
    game = ZQMain()
    game.run()

if __name__ == '__main__':
    main()
