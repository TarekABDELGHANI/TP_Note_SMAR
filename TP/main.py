import random

from pygame.math import Vector2
import core
from agent import Agent
from body import Body
from creep import Creep
from obstacle import Obstacle

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("agents", [])
    core.memory("creeps", [])
    core.memory("obstacles", [])
    initializeEnv()

    print("Setup END-----------")

# Pour chaque Agent, récupère la liste des perceptions.
def computePerception(agent):
    objList = core.memory("agents") + core.memory("creeps") + core.memory("obstacles")
    agent.listPerception = []
    # Pour chaque Agent dans listeObj de l'environnement
    # Pour chaque objet dans le champ de vision de l'Agent
    for obj in objList:
        if agent.body.fustrum.inside(obj) and agent.uuid != obj.uuid:
            # On l'ajoute dans la liste des perceptions de l'agent
            agent.listPerception.append(obj)
    #print(agent.listPerception.__sizeof__())


# Pour chaque Agent, récupère la décision qu'il souhaite réaliser
def computeDecision(agent):
    agent.update()

# Pour chaque Agent, récupère l'action que va executer son body
def applyDecision(agent):
    agent.body.move()

# Ajoute aléatoirement des agents, creeps et obstacles.
def initializeEnv():
    for i in range(5):
        core.memory("agents").append(Agent(Body()))

    for j in range(50):
        core.memory("creeps").append(Creep())

    for h in range(3):
        core.memory("obstacles").append(Obstacle())

# Met à jour l'environnement
def updateEnv() :
    for a in core.memory("agents"):

        for c in core.memory("creeps"):
            if a.body.position.distance_to(c.position) <= a.body.mass:
                c.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
                c.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                a.body.mass += 1

        for o in core.memory("obstacles"):
            if a.body.position.distance_to(o.position) <= a.body.mass:
                core.memory("agents").remove(a)

        for b in core.memory("agents"):
            if b.uuid != a.uuid:
                if a.body.position.distance_to(b.body.position) <= a.body.mass + b.body.mass:
                    if a.body.mass < b.body.mass:
                        b.body.mass += a.body.mass/2
                        core.memory("agents").remove(a)
                    else:
                        a.body.mass += b.body.mass/2
                        core.memory("agents").remove(b)


# Lancer l'execution
def run():
    core.cleanScreen()
    # Display
    for agent in core.memory("agents"):
        agent.show()

    for creep in core.memory("creeps"):
        creep.show()

    for obstacle in core.memory("obstacles"):
        obstacle.show()

    for agent in core.memory("agents"):
        #print("agent", agent.uuid)
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    updateEnv()




core.main(setup, run)