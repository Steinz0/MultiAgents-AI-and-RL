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

        
    #comportement du robot 1 et du robot 5, lorsqu il rencontre un robot adverse il le suit
    if(robotId == 1 or robotId == 5):
        
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
        
            
         
        return translation, rotation
    
    
    #Comportement du robot 0 et 7     
    if(robotId == 0 or robotId == 7):
        translation = 1
        rotation = 0
        
        if(sensors["sensor_front"]["distance"] < 1 and sensors["sensor_front"]["isRobot"]==True):
            rotation = -1    
        if(sensors["sensor_front"]["distance"] < 0.5 and sensors["sensor_front"]["isRobot"]==False):
            rotation = 0.95
        if(sensors["sensor_front_left"]["distance"] < 0.5 and sensors["sensor_front_left"]["isRobot"]==False):   
            rotation = 0.25
        if(sensors["sensor_front_right"]["distance"] < 0.5 and sensors["sensor_front_right"]["isRobot"]==False):   
            rotation =- 0.25
        if(sensors["sensor_left"]["distance"] < 0.5 and sensors["sensor_left"]["isRobot"]==False):   
            rotation = 0.25
        if(sensors["sensor_right"]["distance"] < 0.5 and sensors["sensor_right"]["isRobot"]==False):   
            rotation =- 0.25  
            
        if(sensors["sensor_front"]["distance"] < 0.5 and sensors["sensor_front"]["isRobot"]==True):
            rotation = 1
        if(sensors["sensor_front_left"]["distance"] < 0.5 and sensors["sensor_front_left"]["isRobot"]==True):   
            rotation = 1
        if(sensors["sensor_front_right"]["distance"] < 0.5 and sensors["sensor_front_right"]["isRobot"]==True):   
            rotation =-1
        if(sensors["sensor_left"]["distance"] < 0.5 and sensors["sensor_left"]["isRobot"]==True):   
            rotation = 1
        if(sensors["sensor_right"]["distance"] < 0.5 and sensors["sensor_right"]["isRobot"]==True):   
            rotation =- -1    
         
        translation = max(-1,min(translation,1))
        rotation = max(-1, min(rotation, 1))  
        return translation, rotation
    
     #les autres robots, meme comportement que ceux des adversaires
    else :
    
        translation = 1
        rotation = 0
        if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
            rotation = 0.5
        elif sensors["sensor_front_right"]["distance"] < 1:
            rotation = -0.5

        return translation, rotation
###################################################################################################################################################################

#Fonctionne plutot bien pour l arene 4 cote gauche, a gagne plusieurs fois durant les tests
#Fonctionne aussi plutot bien pour l arene 1 du cote gauche et a gagne plusieurs fois durant les tests    
#Fonctionne bien des deux cotes pour l arene 0 gagne quasiment tout le temps durant les quelques tests
#Fonctionne un peu pour l arene 2
#Fontionne pas pour l arene 3 
        
#################################################################################################################################################################        
        
#memo cela fait tourner en rond :

#       translation = 0.5*sensors["sensor_front"]["distance"]+0.5*sensors["sensor_front"]["distance"] 
#       rotation = 0.5*sensors["sensor_front_left"]["distance"]-0.5*sensors["sensor_front_right"]["distance"]+1+sensors["sensor_front"]["distance"]
        
#       translation = max(-1,min(translation,1))
#       rotation = max(-1, min(rotation, 1))  
#       return translation, rotation    

