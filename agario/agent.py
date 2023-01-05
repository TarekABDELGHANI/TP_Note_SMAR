import random
from itertools import chain

from pygame.math import Vector2

from creep import Creep
from obstacle import Obstacle


class Agent :
    def __init__(self,body = None):
        self.uuid = random.randint(10000,99999)
        self.body = body
        self.listPerception = []

    # filtre le fustrum, ce que voit l'agent
    # filtre doit retourner les listes d'agent, creep et obstacle que voit notre agent
    def filtre(self):
        creeps = []
        agents = []
        obstacles = []
        for i in self.listPerception :
            if isinstance(i,Creep) :
                i.dist = self.body.position.distance_to(i.position)
                creeps.append(i)
            if isinstance(i,Obstacle) :
                i.dist = self.body.position.distance_to(i.position)
                obstacles.append(i)
            if isinstance(i,Agent) :
                i.dist = self.body.position.distance_to(i.body.position)
                agents.append(i)
        creeps.sort(key =lambda x:x.dist, reverse =False)
        obstacles.sort(key=lambda x: x.dist, reverse=False)
        agents.sort(key=lambda x: x.dist, reverse=False)
        return creeps,obstacles,agents

    # La décision que souhaite prendre le cerveau de l'agent
    def update(self):
        creeps,obstacles,agents = self.filtre()
        objList = creeps+ obstacles + agents
        objList.sort(key=lambda x: x.dist, reverse=False)
        min = None
        attraction = Vector2()
        repulsion = Vector2()

        if len(objList) > 0:
            min = objList[0]
        if isinstance(min,Creep) :
            attraction += min.position - self.body.position
        if isinstance(min,Obstacle) :
            repulsion += self.body.position - min.position
        if isinstance(min,Agent) :
            if self.body.mass > min.body.mass :
                attraction += min.body.position - self.body.position
            else :
                repulsion += self.body.position - min.body.position

        if repulsion.length() > 0 :
            repulsion.scale_to_length((1/repulsion.length()**2))
        self.body.acceleration = attraction + repulsion

    # Appel la fonction show de la class Body
    def show (self) :
        self.body.show()


