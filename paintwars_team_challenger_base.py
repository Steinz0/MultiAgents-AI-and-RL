# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: _________
#  Prénom Nom: _________

def get_team_name():
    return " ViveMashle " # à compléter (comme vous voulez)

def step(robotId, sensors): 

    # sensors: dictionnaire contenant toutes les informations senseurs
    # Chaque senseur renvoie:
    #   la distance à l'obstacle (entre 0  et 1, distance max)
    #   s'il s'agit d'un robot ou non
    #   la distance au robot (= 1.0 s'il n'y a pas de robot)
    #   la distance au mur (= 1.0 s'il n'y a pas de robot)
    # cf. exemple ci-dessous

    # récupération des senseurs

    #sensors = get_extended_sensors(sensors)
    print (
        "[robot #",robotId,"] senseur frontal: (distance à l'obstacle =",sensors["sensor_front"]["distance"],")",
        "(robot =",sensors["sensor_front"]["isRobot"],")",
        "(distance_to_wall =", sensors["sensor_front"]["distance"],")", # renvoie 1.0 si ce n'est pas un mur
        "(distance =", sensors["sensor_front"]["distance"],")"  # renvoie 1.0 si ce n'est pas un robot
    )

        
    #comportement du robot 1 seulement, lorsqu il rencontre un robot adverse il le suit
    if(robotId == 1 or robotId == 4):
        
        #Quand ce n est pas un robot adverse il evite les obstacle
        translation = sensors["sensor_front"]["distance"]
        rotation = -0.5*sensors["sensor_front_left"]["distance"]+0.5*sensors["sensor_front_right"]["distance"]+1-sensors["sensor_front"]["distance"]
            
        #S il detecte un robot adverse depuis son capteur arriere il change de direction, ici c est pour eviter le blocage au coin    
        if( sensors["sensor_back"]["isRobot"] == True and sensors["sensor_back"]["isSameTeam"] == False ): 

            print("back ")
            translation = sensors["sensor_front"]["distance"]
            rotation = 0.75*sensors["sensor_front_left"]["distance"]-0.75* sensors["sensor_front_right"]["distance"]-1+sensors["sensor_front"]["distance"]-1+sensors["sensor_back"]["distance"]
            
            return translation, rotation
            
        #Par la suite il va detecter les robots adverses grace aux capteur front , front_left, front_right, back_right et back_left
        elif( sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == False ): 

            print("front right")
            translation = sensors["sensor_front"]["distance"]
            rotation = 0.75*sensors["sensor_front_left"]["distance"]-0.75* sensors["sensor_front_right"]["distance"]-1+sensors["sensor_front"]["distance"]-1+sensors["sensor_back"]["distance"]
            
            return translation, rotation
        
        elif(sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == False):
            
            print("Front left")
            translation = sensors["sensor_front"]["distance"]
            rotation = 0.75*sensors["sensor_front_left"]["distance"]-0.75* sensors["sensor_front_right"]["distance"]-1+sensors["sensor_front"]["distance"]-1+sensors["sensor_back"]["distance"]
            
            
            return translation, rotation
            
        elif( sensors["sensor_back_right"]["isRobot"] == True and sensors["sensor_back_right"]["isSameTeam"] == False ): 

            print("back right")
            translation = sensors["sensor_front"]["distance"]
            rotation = 0.75*sensors["sensor_front_left"]["distance"]-0.75* sensors["sensor_front_right"]["distance"]-1+sensors["sensor_front"]["distance"]-1+sensors["sensor_back"]["distance"]
            
            return translation, rotation
            
        elif( sensors["sensor_back_left"]["isRobot"] == True and sensors["sensor_back_left"]["isSameTeam"] == False ): 

            print("back left")
            translation = sensors["sensor_front"]["distance"]
            rotation = 0.75*sensors["sensor_front_left"]["distance"]-0.75* sensors["sensor_front_right"]["distance"]-1+sensors["sensor_front"]["distance"]-1+sensors["sensor_back"]["distance"]
            
            return translation, rotation
        
        elif(sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False ):
            
            print("Front")
            translation = 1
            rotation = 0
            
            return translation, rotation
        
            
        #Il suit le comportement de debut quand il y a pas de robot adverse il evite juste les obstacles (robot same team et mur)    
        return translation, rotation
    
    #le robot 0 longe les murs
    if(robotId == 0):
        
        #va tout droit si y a pas d'obstacle
        translation = 1
        rotation = 0
        
        if(sensors["sensor_front"]["distance"]<0.7 and sensors["sensor_front"]["isRobot"]==False):
        
            print("longe mur")
            translation = 1
            rotation = 1
            
            return translation, rotation
        
        return translation, rotation
        
    #comportement braitenberg_avoider pour le robot 2    
    if(robotId == 2):
    
        translation = 0.5*sensors["sensor_front"]["distance"]+0.5*sensors["sensor_front"]["distance"] 
        rotation = -0.5*sensors["sensor_front_left"]["distance"]-0.5*sensors["sensor_front_right"]["distance"]+1
        
        translation = max(-1,min(translation,1))
        rotation = max(-1, min(rotation, 1))  
        return translation, rotation
    
    #les autres robots
    else :
    
        translation = 1
        rotation = 0
        if sensors["sensor_front"]["distance"]<1 :
            
            print("ICIIIIIII")
            translation = 1
            rotation = -0.90*sensors["sensor_front_left"]["distance"]+sensors["sensor_front_right"]["distance"]+1-0.90*sensors["sensor_back_left"]["distance"]+sensors["sensor_back_right"]["distance"]+1
            
        if sensors["sensor_right"]["distance"]<1 and sensors["sensor_right"]["isRobot"]==False:
            rotation=1
        if sensors["sensor_left"]["distance"]<1 and sensors["sensor_left"]["isRobot"]==False:
            rotation=1
            
        translation = max(-1,min(translation,1))
        rotation = max(-1, min(rotation, 1)) 
            
        return translation, rotation
        
        
#################################################################################################################################################################        
        
#memo cela fait tourner en rond :

#       translation = 0.5*sensors["sensor_front"]["distance"]+0.5*sensors["sensor_front"]["distance"] 
#       rotation = 0.5*sensors["sensor_front_left"]["distance"]-0.5*sensors["sensor_front_right"]["distance"]+1+sensors["sensor_front"]["distance"]
        
#       translation = max(-1,min(translation,1))
#       rotation = max(-1, min(rotation, 1))  
#       return translation, rotation    

