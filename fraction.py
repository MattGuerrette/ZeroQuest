
from pygame import Surface

class Fraction:

    def __init__(self, num, den):
        self.numerator = num;
        self.denominator = den;

    def calculate(self):
        pass

    def simplify(self):


        while (self.numerator % 2) == 0 and (self.denominator % 2) == 0 and self.numerator != 0:
            self.numerator = self.numerator / 2
            self.denominator = self.denominator / 2

        while (self.numerator % 3) == 0 and (self.denominator % 3) == 0 and self.numerator != 0:
            self.numerator = self.numerator / 3
            self.denominator = self.denominator / 3

        while (self.numerator % 5) == 0 and (self.denominator % 5) == 0 and self.numerator != 0:
            self.numerator = self.numerator / 5
            self.denominator = self.denominator / 5

        while (self.numerator % 7) == 0 and (self.denominator % 7) == 0 and self.numerator != 0:
            self.numerator = self.numerator / 7
            self.denominator = self.denominator / 7

        pass

    def add_fraction(self, other):
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.simplify()
        pass

    def sub_fraction(self, other):
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.simplify()
        pass

    def mul_fraction(self, other):
        self.numerator = self.numerator * other.numerator
        self.denominator = self.denominator * other.denominator
        self.simplify()
        pass

    def div_fraction(self, other):
        self.numerator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator
        self.simplify()
        pass

    def render(self, font, surface, x, y):

        numSurface = font.get_text(str(self.numerator))
        denomSurface = font.get_text(str(self.denominator))
        divSurface = font.get_text("__")
        surface.blit(numSurface, (x,y))
        surface.blit(divSurface, ((x-5),y+5))
        surface.blit(denomSurface, (x,y+25))