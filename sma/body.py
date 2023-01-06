import random

from pygame.math import Vector2

import core
from fustrum import Fustrum
from agent import Agent


class Body :
    def __init__(self):
        self.position = Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.maxVitesse = 5
        self.acceleration = Vector2()
        self.maxAcceleration = 5
        self.mass = 15
        self.fustrum = Fustrum(self,150)
        self.parent = Agent()

    # l'action qu'on veut appliquer au body
    def update(self):
        # if self.acceleration.length() > self.maxAcceleration / self.mass:
        #     self.acceleration.scale_to_length(self.maxAcceleration)
        # self.vitesse += self.acceleration
        # if self.vitesse.length() > self.maxVitesse:
        #     self.vitesse.scale_to_length(self.maxVitesse)
        S,I,R,D,Q = self.parent.filtre()
        objList = S + I + R + D + Q
        objList.sort(key=lambda x: x.dist, reverse=False)
        min = None
        attraction = Vector2()
        repulsion = Vector2()
        if len(objList) > 0:
            min = objList[0]
        # Si on a dans notre champ de vision un Infecté, on se rapproche de lui car on va bientot tomber malade
        if self.parent.statut == 'S' and min.statut == 'I':
            attraction += min.body.position - self.parent.body.position
        # Si on est infecté et qu'on a dans notre champ de vision un mort, on se rapproche de lui pour signifier à l'esprit qu'on va bientot mourrir
        if self.parent.statut == 'I' and min.statut == 'D' :
            attraction += min.body.position - self.parent.body.position
        # Si on est infecté et qu'on a dans notre champ de vision un retabli, on se rapproche de lui pour signifier à l'esprit qu'on va etre rétabli
        if self.parent.statut == 'I' and min.statut == 'R' :
            repulsion += self.parent.body.position - min.body.position
        self.border()
        if repulsion.length() > 0 :
            repulsion.scale_to_length(1/repulsion.length()**2)
        self.parent.body.acceleration = attraction + repulsion

    # gestion des bords
    def border(self):
        if self.position.x >= core.WINDOW_SIZE[0] or self.position.x <= 0:
            self.vitesse.x *= -1
            self.acceleration.x *= -1
        if self.position.y >= core.WINDOW_SIZE[1] or self.position.y <= 0:
            self.vitesse.y *= -1
            self.acceleration.y *= -1

