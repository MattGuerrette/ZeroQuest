
from pygame import font

class Font:

    def __init__(self, fontSize, fontname="monospace"):
        self._font = font.SysFont(fontname, fontSize)


    def get_text(self, text):
        return self._font.render(text, 1, (255,255,255))

    def text_size(self, text):
        return self._font.size(text)