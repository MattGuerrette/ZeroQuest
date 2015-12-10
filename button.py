
from sprite import ButtonOn
from sprite import ButtonOff
from sprite import RedButtonOn
from sprite import RedButtonOff

from random import *

from pygame import mouse
from pygame import Rect

class Button:

    def __init__(self):
        self.buttonOn = ButtonOn()
        self.buttonOff = ButtonOff()
        self.isOn = False;
        self.rect = Rect(0,0,0,0)

    def get_sprite(self):
        if self.isOn:
            return self.buttonOn
        else:
            return self.buttonOff

    def set_x(self, x):
        self.buttonOn.rect.x = x
        self.buttonOff.rect.x = x
        self.rect = self.buttonOn.rect

    def set_y(self, y):
        self.buttonOn.rect.y = y
        self.buttonOff.rect.y = y
        self.rect = self.buttonOn.rect

    def check_pressed(self, pressed, x, y):
        if pressed:
            if self.rect.collidepoint(x, y):
                self.isOn = True
        return self.isOn

    def check_point(self, x, y):
        return self.rect.collidepoint(x, y)

    def set_pressed(self, pressed):
        self.isOn = pressed


class RedButton(Button):

    def __init__(self):

        Button.__init__(self)

        self.buttonOn = RedButtonOn()
        self.buttonOff = RedButtonOff()

class OperatorType:
    Unknown, Add, Sub, Mul, Div = range(5)

class OperatorButton(Button):

    def __init__(self, OperatorType=OperatorType.Unknown):

        Button.__init__(self)

        self.operator = OperatorType

    def get_operator(self):
        return self.operator

    def draw_operator(self, surface, font):
        if self.operator == OperatorType.Add:
            opSize = font.text_size("+")
            surface.blit(font.get_text("+"), (self.rect.x + (self.rect.width/2 - opSize[0]/2), self.rect.y + 25))
        elif self.operator == OperatorType.Sub:
            opSize = font.text_size("-")
            surface.blit(font.get_text("-"), (self.rect.x + (self.rect.width/2 - opSize[0]/2), self.rect.y + 25))
        elif self.operator == OperatorType.Mul:
            opSize = font.text_size("*")
            surface.blit(font.get_text("*"), (self.rect.x + (self.rect.width/2 - opSize[0]/2), self.rect.y + 25))
        elif self.operator == OperatorType.Div:
            opSize = font.text_size("/")
            surface.blit(font.get_text("/"), (self.rect.x + (self.rect.width/2 - opSize[0]/2), self.rect.y + 25))

class ValueButton(Button):

        def __init__(self, Value=0):

            Button.__init__(self)

            self.value = Value

        def generate_value(self):
            chance = randint(0, 20)
            if chance < 1:
                self.value = 0
            elif chance < 2:
                self.value = 1
            elif chance < 6:
                self.value = 2
            elif chance < 9:
                self.value = 3
            elif chance < 12:
                self.value = 4
            elif chance < 14:
                self.value = 5
            elif chance < 16:
                self.value = 6
            elif chance < 18:
                self.value = 7
            elif chance < 19:
                self.value = 8
            elif chance < 20:
                self.value = 9
            else:
                self.value = 10

        def get_value(self):
            return self.value


        def draw_value(self, surface, font):
            valSize = font.text_size(str(self.value))
            surface.blit(font.get_text(str(self.value)), (self.rect.x + (self.rect.width/2 - valSize[0]/2), self.rect.y + 25))