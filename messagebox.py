


class Message:

    def __init__(self, message, font, speed = 10):
        self.message = message
        self.elapsed = 0.0
        self.font = font
        self.render_str = ""
        self.type_speed = speed

    def set_type_speed(self, speed):
        self.type_speed = speed

    def set_message(self, message):
        self.message = message
        self.render_str = ""

    def empty(self):
        return len(self.message) <= 0

    def reset(self):
        self.render_str = ""

    def is_done(self):
        if self.render_str == self.message:
            return True
        return False

    def finish(self):
        self.render_str = self.message

    def update(self, dt):
        self.elapsed += 1
        rslen = 0

        if self.type_speed == 0:
            self.render_str = self.message

        if self.elapsed >= self.type_speed:
            rslen = len(self.render_str)
            if rslen < len(self.message):
                self.render_str += self.message[rslen]
            self.elapsed = 0

    def render(self, surface, x, y):
        fontsurface = self.font.get_text(self.render_str)
        surface.blit(fontsurface, (x, y))

class MessageBox:

    def __init__(self):
        self.message = ""

    def set_message(self, message):
        self.message = message