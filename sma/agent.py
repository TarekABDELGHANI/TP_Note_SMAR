import random

from pygame.math import Vector2

import core


class Agent :
    def __init__(self,body = None):
        self.uuid = random.randint(10000,99999)
        self.body = body
        self.listPerception = []
        self.statut = random.choice(['S', 'I', 'R', 'D', 'Q'])

    # filtre le fustrum, ce que voit l'agent
    def filtre(self):
        S = []
        I = []
        R = []
        D = []
        Q = []
        for i in self.listPerception:
            i.dist = self.body.position.distance_to(i.body.position)
            if i.statut == 'S':
                S.append(i)
            if i.statut == 'I':
                I.append(i)
            if i.statut == 'R':
                R.append(i)
            if i.statut == 'D':
                D.append(i)
            if i.statut == 'Q':
                Q.append(i)
        S.sort(key=lambda x: x.dist, reverse=False)
        I.sort(key=lambda x: x.dist, reverse=False)
        R.sort(key=lambda x: x.dist, reverse=False)
        D.sort(key=lambda x: x.dist, reverse=False)
        Q.sort(key=lambda x: x.dist, reverse=False)
        return S,I,R,D,Q

    # effectue un mouvement aléatoire pour l'agent
    def randomMoove(self):
        self.body.acceleration += Vector2(random.randint(-core.WINDOW_SIZE[0],core.WINDOW_SIZE[0]),random.randint(-core.WINDOW_SIZE[1],core.WINDOW_SIZE[1]))

    # Dessine l'agent dans l'environnement
    def show(self):
        if(self.statut == 'S') :
            core.Draw.circle((0,255,0), self.body.position, self.body.mass)
        if (self.statut == 'I') :
            core.Draw.circle((255, 0, 0), self.body.position, self.body.mass)
        if (self.statut == 'R') :
            core.Draw.circle((0, 0, 255), self.body.position, self.body.mass)
        if (self.statut == 'D') :
            core.Draw.circle((255, 255, 255), self.body.position, self.body.mass)
        if (self.statut == 'Q') :
            core.Draw.circle((125, 125, 125), self.body.position, self.body.mass)

    # Faire une fonction qui à partir du update du Body utilise le dictionnaire de epidemie pour changer le statut de l'agent
