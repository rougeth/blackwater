from asciimatics.effects import Print
from asciimatics.renderers import FigletText, Fire
from asciimatics.scene import Scene
from asciimatics.screen import Screen


class GreenFire(Fire):
    _COLOURS_256 = [
        (0, 0),
        (22, 0),
        (28, 0),
        (34, 0),
        (40, 0),
        (46, 0),
        (82, 0),
        (83, 0),
        (154, 0),
        (155, 0),
        (156, 0),
        (157, 0),
        (158, 0),
        (194, 0),
        (230, 0),
        (231, 0),
    ]


def welcome(screen):
    scenes = []

    greenfire = GreenFire(screen.height+10, screen.width, '*' * screen.width,
                          0.6, 60, screen.colours, bg=screen.colours >= 256)

    blackwater = FigletText('BLACKWATER', font='banner3')

    effects = [
        Print(screen, greenfire, 0, speed=1, transparent=False),
        Print(screen, blackwater, screen.height-18, speed=1,
              colour=Screen.COLOUR_BLACK, transparent=True)
    ]

    scenes.append(Scene(effects, 100))
    screen.play(scenes)


if __name__ == '__main__':
    while True:
        Screen.wrapper(welcome)
