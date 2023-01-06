import random

from pygame.math import Vector2
import core
from agent import Agent
from body import Body

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("agents", [])
    initializeEnv()

    print("Setup END-----------")

# Pour chaque Agent, récupère la liste des perceptions.
def computePerception(agent):
    agentList = core.memory("agents")
    agent.listPerception = []
    # Pour chaque Agent dans agentList de l'environnement
    for agentBis in agentList:
        if agent.body.fustrum.inside(agentBis) and agent.uuid != agentBis.uuid:
            # On l'ajoute dans la liste des perceptions de l'agent
            agent.listPerception.append(agentBis)
    #print(agent.listPerception.__sizeof__())


# Pour chaque Agent, récupère la décision qu'il souhaite réaliser
def computeDecision(agent):
    agent.randomMoove()

# Pour chaque Agent, récupère l'action que va executer son body
def applyDecision(agent):
    agent.body.update()

# Ajoute aléatoirement des agents, creeps et obstacles.
def initializeEnv():
    for i in range(10):
        core.memory("agents").append(Agent(Body()))

# Met à jour l'environnement
def updateEnv() :
    for agent in core.memory("agents"):
        agent.randomMoove()
    for a in core.memory("agents"):
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

    for agent in core.memory("agents"):
        #print("agent", agent.uuid)
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    # updateEnv()
core.main(setup, run)