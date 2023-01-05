import random

from pygame.math import Vector2

import core
from fustrum import Fustrum


class Body :
    def __init__(self):
        self.position = Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.maxVitesse = 10
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
        self.position+= self.vitesse

    # Dessiner l'agent dans l'environnement
    def show(self):
        core.Draw.circle(self.color,self.position, self.mass)
