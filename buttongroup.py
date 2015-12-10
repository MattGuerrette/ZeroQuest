

class ButtonGroup:

    def __init__(self, buttonArray):
        self.buttons = buttonArray
        self.current = -1

    def check_pressed(self, pressed, x, y):
        inButton = False
        index = -1
        for i in range(0, 4):
            b = self.buttons[i]
            inButton = b.check_point(x, y)
            if inButton:
                index = i
                self.current = i
                break

        if inButton:
            for i in range(0, 4):
                b = self.buttons[i]
                b.set_pressed(False)
            if pressed:
                self.buttons[index].set_pressed(True)

    def get_selected(self):
        if self.current != -1:
            return self.buttons[self.current]
        else:
            return None