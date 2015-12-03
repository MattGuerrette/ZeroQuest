
from pygame import font

class Font:

    def __init__(self):
        self._font = font.SysFont("monospace", 15)


    def get_text(self, text):
        return self._font.render(text, 1, (255,255,255))

