import random

from pygame.math import Vector2

import core


class Creep :
    def __init__(self):
        self.uuid = random.randint(10000, 99999)

        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.mass = 5
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def show(self):
        core.Draw.circle(self.color, self.position, self.mass)

