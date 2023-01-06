import random

from pygame.math import Vector2

import core
from fustrum import Fustrum


class Body :
    def __init__(self):
        self.position = Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.maxVitesse = 5
        self.acceleration = Vector2()
        self.maxAcceleration = 10
        self.mass = 15
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.fustrum = Fustrum(self,150)

    # l'action qu'on veut appliquer au body
    def move(self):
        if self.acceleration.length() > self.maxAcceleration/self.mass :
            self.acceleration.scale_to_length(self.maxAcceleration)
        self.vitesse += self.acceleration
        if self.vitesse.length()> self.maxVitesse :
            self.vitesse.scale_to_length(self.maxVitesse)
        self.border()
        self.position+= self.vitesse

    # gestion des bords
    def border(self):
        if self.position.x >= core.WINDOW_SIZE[0] or self.position.x <= 0:
            self.vitesse.x *= -1
            self.acceleration.x *= -1
        if self.position.y >= core.WINDOW_SIZE[1] or self.position.y <= 0:
            self.vitesse.y *= -1
            self.acceleration.y *= -1

    # Dessiner l'agent dans l'environnement
    def show(self):
        core.Draw.circle(self.color,self.position, self.mass)
