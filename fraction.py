
from pygame import Surface
from sprite import DisplayScreen

class Fraction:

    def __init__(self, num, den):
        self.numerator = num;
        self.denominator = den;
        self.divText = ""

    def is_zero(self):
        return self.numerator == 0

    def calculate(self):
        pass

    def simplify(self):


        isTrue = False
        while (self.numerator % 2) == 0 and (self.denominator % 2) == 0 and self.numerator != 0:
            self.numerator = self.numerator / 2
            self.denominator = self.denominator / 2
            isTrue = True

        while (self.numerator % 3) == 0 and (self.denominator % 3) == 0 and self.numerator != 0:
            self.numerator = self.numerator / 3
            self.denominator = self.denominator / 3
            isTrue = True

        while (self.numerator % 5) == 0 and (self.denominator % 5) == 0 and self.numerator != 0:
            self.numerator = self.numerator / 5
            self.denominator = self.denominator / 5
            isTrue = True

        while (self.numerator % 7) == 0 and (self.denominator % 7) == 0 and self.numerator != 0:
            self.numerator = self.numerator / 7
            self.denominator = self.denominator / 7
            isTrue = True

        if self.denominator < 0:
            self.denominator *= -1
            self.numerator *= -1

        return isTrue

    def add_fraction(self, other):
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.simplify()

        if other.numerator == 0:
            return "Add was not very effective"
        elif self.numerator == 0:
            return "Add was super effective!"
        else:
            return "The number increased"


    def sub_fraction(self, other):
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.simplify()

        if other.numerator == 0:
            return "Subtract was not very effective"
        elif self.numerator == 0:
            return "Subtract was super effective!"
        else:
            return "The number decreased"

    def mul_fraction(self, other):
        self.numerator = self.numerator * other.numerator
        self.denominator = self.denominator * other.denominator
        if self.simplify() or self.numerator == 0:
            return "Multiply was super effective!"
        else:
            return "Multiply was not very effective"


    def div_fraction(self, other):
        if other.numerator == 0:
            return "ERROR: cannot divide by ZERO, Divide failed."
        self.numerator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator
        if self.simplify():
            return "Divide was super effective!"
        else:
            return "Divide was not very effective"


    def render(self, font, surface, x, y):

        numSurface = font.get_text(str(self.numerator))
        denomSurface = font.get_text(str(self.denominator))

        self.divText = "__"
        values = [len(str(self.numerator)), len(str(self.numerator))]
        for i in range(1, max(values)):
            self.divText += "_"
        numWidth = font.text_size(str(self.numerator))[0]
        denWidth = font.text_size(str(self.denominator))[0]
        divWidth = font.text_size(self.divText)[0]
        divSurface = font.get_text(self.divText)
        surface.blit(numSurface, (x + (divWidth/2 - numWidth/2) - 10,y))
        if self.denominator != 1:
            surface.blit(divSurface, ((x-10),y+10))
            surface.blit(denomSurface, (x + (divWidth/2 - denWidth/2) - 10,y+50))

    def get_size(self, font):
        numSize = font.text_size(str(self.numerator))
        divSize = font.text_size(self.divText)
        denSize = font.text_size(str(self.denominator))

        totalX = divSize[0]
        totalY = numSize[1] + divSize[1] + denSize[1]

        total = [0] * 2
        total.append(totalX)
        total.append(totalY)
        return total

class FractionDisplay:

        def __init__(self):
            self.sprite = DisplayScreen()
            self.fraction = Fraction(1,1)

        def get_sprite(self):
            return self.sprite

        def set_fraction(self, Fraction):
            self.fraction = Fraction

        def get_fraction(self):
            return self.fraction

        def render_fraction(self, surface, font):
            fractionSize = self.fraction.get_size(font)
            self.fraction.render(font, surface, self.sprite.rect.x + (self.sprite.rect.width/2 - fractionSize[0]/2) - 10, self.sprite.rect.y + 30)