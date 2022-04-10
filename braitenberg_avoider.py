# @@ -1,17 +1,10 @@
# UE IA & JEUX - L3, SU
# TP "comportement réactif"
#
# Nicolas Bredeche
# 2021-03-31

from pyroborobo import Pyroborobo, Controller, AgentObserver, WorldObserver, CircleObject, SquareObject, MovableObject
# from custom.controllers import SimpleController, HungryController
import numpy as np
import random

import paintwars_arena

# =-=-=-=-=-=-=-=-=-= NE RIEN MODIFIER *AVANT* CETTE LIGNE =-=-=-=-=-=-=-=-=-=

def get_extended_sensors(sensors):
    for key in sensors:
@@ -23,18 +16,7 @@ def get_extended_sensors(sensors):
            sensors[key]["distance_to_wall"] = sensors[key]["distance"]
    return sensors

def step(robotId, sensors): # <<<<<<<<<------- fonction à modifier pour le TP1

    # sensors: dictionnaire contenant toutes les informations senseurs
    # Chaque senseur renvoie:
    #   la distance à l'obstacle (entre 0  et 1, distance max)
    #   s'il s'agit d'un robot ou non
    #   la distance au robot (= 1.0 s'il n'y a pas de robot)
    #   la distance au mur (= 1.0 s'il n'y a pas de robot)
    # cf. exemple ci-dessous

    # récupération des senseurs

def step(robotId, sensors):
    sensors = get_extended_sensors(sensors)
    print (
        "[robot #",robotId,"] senseur frontal: (distance à l'obstacle =",sensors["sensor_front"]["distance"],")",
@@ -43,25 +25,15 @@ def step(robotId, sensors): # <<<<<<<<<------- fonction à modifier pour le TP1
        "(distance_to_robot =", sensors["sensor_front"]["distance_to_robot"],")"  # renvoie 1.0 si ce n'est pas un robot
    )

    # contrôle moteur. Ecrivez votre comportement de Braitenberg ci-dessous.
    # il est possible de répondre à toutes les questions en utilisant seulement:
    #   sensors["sensor_front"]["distance_to_wall"]
    #   sensors["sensor_front"]["distance_to_robot"]
    #   sensors["sensor_front_left"]["distance_to_wall"]
    #   sensors["sensor_front_left"]["distance_to_robot"]
    #   sensors["sensor_front_right"]["distance_to_wall"]
    #   sensors["sensor_front_right"]["distance_to_robot"]

    translation = 0.5*sensors["sensor_front"]["distance_to_wall"]+0.5*sensors["sensor_front"]["distance_to_robot"] # vitesse de translation (entre -1 et +1) -- A MODIFIER
    rotation = -0.5*sensors["sensor_front_left"]["distance_to_wall"]+0.5*sensors["sensor_front_right"]["distance_to_wall"]+1-sensors["sensor_front"]["distance_to_wall"]-0.5*sensors["sensor_front_left"]["distance_to_robot"]+0.5* sensors["sensor_front_right"]["distance_to_robot"]+1-sensors["sensor_front"]["distance_to_robot"]

    # limite les valeurs de sortie entre -1 et +1
    translation = max(-1,min(translation,1))
    rotation = max(-1, min(rotation, 1))

    return translation, rotation

# =-=-=-=-=-=-=-=-=-= NE RIEN MODIFIER *APRES* CETTE LIGNE =-=-=-=-=-=-=-=-=-=

number_of_robots = 8  # 8 robots identiques placés dans l'arène

@@ -134,10 +106,7 @@ def check(self):
        # print (self.id)
        return True


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class MyAgentObserver(AgentObserver):
    class MyAgentObserver(AgentObserver):
    def __init__(self, wm):
        super().__init__(wm)
        self.arena_size = Pyroborobo.get().arena_size
@@ -153,10 +122,6 @@ def step_pre(self):
    def step_post(self):
        super().step_post()
        return


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class MyWorldObserver(WorldObserver):
    def __init__(self, world):
        super().__init__(world)
@@ -199,9 +164,6 @@ def step_pre(self):
    def step_post(self):
        super().step_post()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Tile(SquareObject):  # CircleObject):

    def __init__(self, id=-1, data={}):
@@ -214,9 +176,6 @@ def step(self):
    def is_walked(self, id_):
        return


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class BlockObject(SquareObject):
    def __init__(self, id=-1, data={}):
        super().__init__(id, data)
@@ -228,7 +187,6 @@ def is_walked(self, id_):
        return


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def main():
    global rob
