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
        sensors[key]["distance_to_robot"] = 1.0
        sensors[key]["distance_to_wall"] = 1.0
        if sensors[key]["isRobot"] == True:
            sensors[key]["distance_to_robot"] = sensors[key]["distance"]
        else:
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

    sensors = get_extended_sensors(sensors)
    print (
        "[robot #",robotId,"] senseur frontal: (distance à l'obstacle =",sensors["sensor_front"]["distance"],")",
        "(robot =",sensors["sensor_front"]["isRobot"],")",
        "(distance_to_wall =", sensors["sensor_front"]["distance_to_wall"],")", # renvoie 1.0 si ce n'est pas un mur
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
    
    
    #comportement du robot 1 seulement
    #comportement du robot 1 seulement
    if(robotId == 1):
        
        #le robot va tout droit si pas d obstacle
        translation = 1.0
        rotation = 0.0
        
        #si y a un mur il evite le mur, utilisation de hateWall
        if(sensors["sensor_front"]["distance_to_wall"]<0.2 or sensors["sensor_front_left"]["distance_to_wall"]<0.2 or sensors["sensor_front_right"]["distance_to_wall"]<0.2 ):
            
            
            #print("on fonce dans e mur",sensors["sensor_front"]["distance_to_wall"])
            translation = 0.5*sensors["sensor_front"]["distance_to_wall"]+0.5*sensors["sensor_front"]["distance_to_robot"]
            rotation = -0.5*sensors["sensor_front_left"]["distance_to_wall"]+0.5*sensors["sensor_front_right"]["distance_to_wall"]+1-sensors["sensor_front"]["distance_to_wall"]
            
            
            return translation,rotation
            
        #Si y a un robot le suit
        elif(sensors["sensor_front_right"]["distance_to_robot"] < 0.7 ): 
            #fonctionne
            print("FRONT DROIT")
            translation = sensors["sensor_front"]["distance_to_robot"]
            rotation = 0.75*sensors["sensor_front_left"]["distance_to_robot"]-0.75* sensors["sensor_front_right"]["distance_to_robot"]-1+sensors["sensor_front"]["distance_to_robot"]-1+sensors["sensor_back"]["distance_to_robot"]
            return translation, rotation
            
        elif(sensors["sensor_right"]["distance_to_robot"] < 0.7 ): 

            print("DROIT")
            translation = sensors["sensor_front"]["distance_to_robot"]
            rotation = 0.75*sensors["sensor_front_left"]["distance_to_robot"]-0.75* sensors["sensor_front_right"]["distance_to_robot"]-1+sensors["sensor_front"]["distance_to_robot"]-1+sensors["sensor_back"]["distance_to_robot"]
            return translation, rotation
            
        elif(sensors["sensor_front"]["distance_to_robot"] < 0.7):
            
            print("FRONT")
            translation = sensors["sensor_front"]["distance_to_robot"]
            rotation = 0#0.1*sensors["sensor_front_left"]["distance_to_robot"]-0.1* sensors["sensor_front_right"]["distance_to_robot"]-1+sensors["sensor_front"]["distance_to_robot"]-1+sensors["sensor_back"]["distance_to_robot"]
            
            return translation, rotation
            
        elif(sensors["sensor_front_left"]["distance_to_robot"] < 0.9):
        #revoir
            print("FRONT LEFT")
            translation = sensors["sensor_front"]["distance_to_robot"]
            rotation = -0.90*sensors["sensor_front_left"]["distance_to_robot"]+0.90* sensors["sensor_front_right"]["distance_to_robot"]+1-sensors["sensor_front"]["distance_to_robot"]+1-sensors["sensor_back"]["distance_to_robot"]
        
            return translation, rotation
            
        elif(sensors["sensor_left"]["distance_to_robot"] < 0.9):
        #revoir
            print("LEFT")
            translation = 1
            rotation =-0.01*sensors["sensor_front_left"]["distance_to_robot"]-0.01*sensors["sensor_front_right"]["distance_to_robot"]+0.01*sensors["sensor_front"]["distance_to_robot"]+0.99*sensors["sensor_back"]["distance_to_robot"]+1
            
            return translation, rotation

        if(sensors["sensor_back"]["distance_to_robot"] < 0.7):
            #fonctionne
            print("ARRIERE")
            translation = 1#0.5*sensors["sensor_front"]["distance_to_wall"]+0.5*sensors["sensor_front"]["distance_to_robot"] # vitesse de translation (entre -1 et +1) -- A MODIFIER
            rotation = -0.5*sensors["sensor_front_left"]["distance_to_wall"]+0.5*sensors["sensor_front_right"]["distance_to_wall"]+1-sensors["sensor_front"]["distance_to_wall"]-0.5*sensors["sensor_front_left"]["distance_to_robot"]+0.5* sensors["sensor_front_right"]["distance_to_robot"]+1-sensors["sensor_front"]["distance_to_robot"]
            
            return translation,rotation
            
           
        
        elif(sensors["sensor_back_left"]["distance_to_robot"] < 0.7):  
            
            print("BACK LEFT")
            translation =0
            rotation = sensors["sensor_back_left"]["distance_to_robot"]
            
            return translation, rotation 
        
        return translation, rotation
      
    #sensors["sensor_back_left"]["distance_to_robot"] < 0.7 or sensors["sensor_back_right"]["distance_to_robot"] < 0.7
    
    #comportement braitenberg_avoider des autres robots    
    if(robotId != 1):
        translation = 0.5*sensors["sensor_front"]["distance_to_wall"]+0.5*sensors["sensor_front"]["distance_to_robot"] # vitesse de translation (entre -1 et +1) -- A MODIFIER
        rotation = -0.5*sensors["sensor_front_left"]["distance_to_wall"]+0.5*sensors["sensor_front_right"]["distance_to_wall"]+1-sensors["sensor_front"]["distance_to_wall"]-0.5*sensors["sensor_front_left"]["distance_to_robot"]+0.5* sensors["sensor_front_right"]["distance_to_robot"]+1-sensors["sensor_front"]["distance_to_robot"]
        
        translation = max(-1,min(translation,1))
        rotation = max(-1, min(rotation, 1))  
        return translation, rotation
    
    #ici on passera jamais 
    #translation = 0.5 # vitesse de translation (entre -1 et +1) -- A MODIFIER
    #rotation = 0.3 # vitesse de rotation (entre -1 et +1) -- A MODIFIER

    # limite les valeurs de sortie entre -1 et +1
    translation = max(-1,min(translation,1))
    rotation = max(-1, min(rotation, 1))

    return translation, rotation
    
    #Remarques lors de l execution :
    #remarque 1 dans braitenberg_hateWall les robots se suivent comme ils ont le meme comportement
    #remarque 2 le robot 1 suit un robot et des qu il rencontre un autre robot il suit ce dernier et des fois ils se bloquent 
    #remarque 3 des fois le robot dont il suit le seme donc il ne le suit plus comme le robot devant est trop loin et ne suit pas longtemps

# =-=-=-=-=-=-=-=-=-= NE RIEN MODIFIER *APRES* CETTE LIGNE =-=-=-=-=-=-=-=-=-=

number_of_robots = 8  # 8 robots identiques placés dans l'arène

arena = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

rob = 0

offset_x = 36
offset_y = 36
edge_width = 28
edge_height = 28


class MyController(Controller):

    def __init__(self, wm):
        super().__init__(wm)

    def reset(self):
        return

    def step(self):

        sensors = {}

        self.get_robot_id_at(0) != -1
        sensors["sensor_left"] = {"distance": self.get_distance_at(0), "isRobot": self.get_robot_id_at(0) != -1}
        sensors["sensor_front_left"] = {"distance": self.get_distance_at(1), "isRobot": self.get_robot_id_at(1) != -1}
        sensors["sensor_front"] = {"distance": self.get_distance_at(2), "isRobot": self.get_robot_id_at(2) != -1}
        sensors["sensor_front_right"] = {"distance": self.get_distance_at(3), "isRobot": self.get_robot_id_at(3) != -1}
        sensors["sensor_right"] = {"distance": self.get_distance_at(4), "isRobot": self.get_robot_id_at(4) != -1}
        sensors["sensor_back_right"] = {"distance": self.get_distance_at(5), "isRobot": self.get_robot_id_at(5) != -1}
        sensors["sensor_back"] = {"distance": self.get_distance_at(6), "isRobot": self.get_robot_id_at(6) != -1}
        sensors["sensor_back_left"] = {"distance": self.get_distance_at(7), "isRobot": self.get_robot_id_at(7) != -1}

        translation, rotation = step(self.id, sensors)

        self.set_translation(translation)
        self.set_rotation(rotation)

    def check(self):
        # print (self.id)
        return True


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class MyAgentObserver(AgentObserver):
    def __init__(self, wm):
        super().__init__(wm)
        self.arena_size = Pyroborobo.get().arena_size

    def reset(self):
        super().reset()
        return

    def step_pre(self):
        super().step_pre()
        return

    def step_post(self):
        super().step_post()
        return


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class MyWorldObserver(WorldObserver):
    def __init__(self, world):
        super().__init__(world)
        rob = Pyroborobo.get()

    def init_pre(self):
        super().init_pre()

    def init_post(self):
        global offset_x, offset_y, edge_width, edge_height, rob

        super().init_post()

        for i in range(len(arena)):
            for j in range(len(arena[0])):
                if arena[i][j] == 1:
                    block = BlockObject()
                    block = rob.add_object(block)
                    block.soft_width = 0
                    block.soft_height = 0
                    block.solid_width = edge_width
                    block.solid_height = edge_height
                    block.set_color(164, 128, 0)
                    block.set_coordinates(offset_x + j * edge_width, offset_y + i * edge_height)
                    retValue = block.can_register()
                    # print("Register block (",block.get_id(),") :", retValue)
                    block.register()
                    block.show()

        counter = 0
        for robot in rob.controllers:
            x = 260 + counter*40
            y = 400
            robot.set_position(x, y)
            counter += 1

    def step_pre(self):
        super().step_pre()

    def step_post(self):
        super().step_post()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Tile(SquareObject):  # CircleObject):

    def __init__(self, id=-1, data={}):
        super().__init__(id, data)
        self.owner = "nobody"

    def step(self):
        return

    def is_walked(self, id_):
        return


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class BlockObject(SquareObject):
    def __init__(self, id=-1, data={}):
        super().__init__(id, data)

    def step(self):
        return

    def is_walked(self, id_):
        return


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def main():
    global rob

    rob = Pyroborobo.create(
        "config/paintwars.properties",
        controller_class=MyController,
        world_observer_class=MyWorldObserver,
        #        world_model_class=PyWorldModel,
        agent_observer_class=MyAgentObserver,
        object_class_dict={}
        ,override_conf_dict={"gInitialNumberOfRobots": number_of_robots} # defined in paintwars_config
    )

    rob.start()

    rob.update(1000000)
    rob.close()

if __name__ == "__main__":
    main()