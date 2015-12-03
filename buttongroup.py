

class ButtonGroup:

    def __init__(self, buttonArray):
        self.buttons = buttonArray

    def check_pressed(self, pressed, x, y):
        index = 0
        for i in range(0, 4):
            b = self.buttons[i]
            checked = b.check_pressed(pressed, x, y)
            if checked:
               index = 0
               break

        for i in range(0, 4):
            b = self.buttons[i]
            if i != index:
                b.set_pressed(False)
