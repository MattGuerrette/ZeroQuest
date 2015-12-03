
from sprite import ButtonOn
from sprite import ButtonOff
from sprite import RedButtonOn
from sprite import RedButtonOff

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
                self.isOn = not self.isOn

class RedButton(Button):

    def __init__(self):

        Button.__init__(self)

        self.buttonOn = RedButtonOn()
        self.buttonOff = RedButtonOff()
