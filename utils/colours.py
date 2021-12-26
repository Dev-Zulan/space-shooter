class Colour:
    def __init__(self):
        self._colour = {
            'white': (255, 255, 255),
            'black': (0, 0, 0)
        }

    def colour_RGB(self, colour):
        return self._colour["{}".format(colour).lower()]

Colour = Colour()