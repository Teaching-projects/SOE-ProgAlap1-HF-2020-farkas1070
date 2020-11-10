"""
Tovabbfejlesztjuk az elozo dolgot. 

Most atirjuk a kiirato fuggvenyt ugy, hogy kap egy dictionary-t is, amiben benne van a jatekos karakterunk a kovetkezo modon:

character = {
    "name" : "Dark Wanderer",
    "position" : {
        "x" : 4 ,
        "y" : 2 
    }
}


Az eredmenye a kiiratasnak a korabbi peldaterkepen igy nezne ki:

████████████████████████████
██░░░░░░░░░░░░██████████████
██░░░░░░🧙‍░░░░██████░░░░░░██
██░░░░██████████████░░██░░██
██░░░░██░░░░░░░░░░██░░██░░██
██░░░░░░░░░░░░██░░██░░██░░██
██████████░░░░██░░██░░██░░██
██░░░░░░░░░░░░██░░░░░░██░░░░
████████████████████████████

Ket dolog valtozott meg:
 - Az eddigi █ es ░ karaktereket mindig duplan rajzoljuk ki, hogy korulbelul negyzet alaku legyen egy mezo.
 - A karakterunk helyere 🧙‍-t irunk ki.



"""

def initialize_map (width, height):
    térkép = []

        
    tégla = "██"
    nincs_tégla = "░░"
    for i in range(1):
        egység = ["██"]*width
        térkép.append(egység)
    for i in range(height-2):
        egység = []
        egység.append(tégla)
        for i in range(width-2):
            egység.append(nincs_tégla)
        egység.append(tégla)
        térkép.append(egység)
    for i in range(1):
        egység = ["██"]*width
        térkép.append(egység)
    return térkép



def pretty_map_print(map, character):
    map = initialize_map(width,height)
    character = {
    "name" : "Dark Wanderer",
    "position" : {
        "x" : 4 ,
        "y" : 2 
        }
    }
    for i in range(len(map)):
        for j in range(len(map[i])):
            index1 = character["position"]["y"]
            index2 = character["position"]["x"]
            if i == index1 and j == index2:
                map[i][j] = "🧙"
                print(map[i][j],end='')
            #if map[i][j] == map[character["position"]["x"]][character["position"]["y"]]:
             #  map[i][j] == "[]"
              # print(map[i][j],end='')
            else:
                print(map[i][j], end='')
        print()




###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


def initialize_character():
    x=int(input())
    y=int(input())
    return {"name": "Placeholder name", "position" : {"x":x,"y":y} }

width=int(input())
height=int(input())
map=initialize_map(width,height)

character=initialize_character()

pretty_map_print(map,character)
