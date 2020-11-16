"""
A terkepre most mar kikerulnek taposoaknak is. Ha a hosunk ralep egyre, akkor befejezodott a jatek. Ezt a logikat lekezeli a foprogram megfelelo resze. 

Nektek most egy olyan fuggvenyt kell megirni, ami egy karaktert es egy aknalistat kap (lasd a foprogramot peldanak) es visszater igaz/hamis ertekkel attol fuggoen, hogy valamelyikre ralepett-e a hosunk, vagy sem.

Ezen kivul meg a pretty print fuggvenyen kell annyit modositani, hogy ne fixen a 🧙 karaktert rajzolja ki a hozunknek, hanem annak az icon adattagjat. (Lasd forprogram)

"""

def pretty_map_print(map, character):
    # A multkorit kell kicsit megpofozni
    x = character["position"]["x"]
    y = character["position"]["y"]
    sorok = len(map[1])
    oszlopok = len(map)

    if (x <= sorok - 1 and x >= 0) and (y <= oszlopok - 1 and y >= 0): 
        map[y][x] = character["icon"]

    látás = character["vision"]

    for i in range(len(map)):
        if y-i <= látás and i-y <= látás:
            for j  in range(len(map[i])):
                if x-j <= látás and j-x <= látás:
                    if map[i][j] != character["icon"]:
                        print(map[i][j],end='')
                        print(map[i][j],end='')
                    else:
                        print(character["icon"],end='')
            print('')

def move(map,character,direction):
    # ide csak masold be a multkorit, nem kell pofozni
    x = character["position"]["x"]
    y = character["position"]["y"]
    if direction == "up" and map[y-1][x] != "█":
        character["position"]["y"] -= 1
        map[y][x] = "░"
        return True
    if direction == "down" and map[y+1][x] != "█":
        character["position"]["y"] += 1
        map[y][x] = "░"
        return True
    if direction == "left"and map[y][x-1] != "█":
        character["position"]["x"] -= 1
        map[y][x] = "░"
        return True
    if direction == "right" and map[y][x+1] != "█":
        character["position"]["x"] += 1
        map[y][x] = "░"
        return True
    else:
        return False

def stepped_on_mine(character,mines):
    # ide kell megirni az uj fuggvenyt a fentiek szerint.
    stepped_on_mine = False
    x = character["position"]["x"]
    y = character["position"]["y"]
    for i in range(len(landmines)):
        for key in landmines[i]:
            if key == "position":
               if landmines[i]["position"]["y"] == y and landmines[i]["position"]["x"] == x:
                    stepped_on_mine = True
    if stepped_on_mine == True:
        return True
    else:
        return False
            

"""
Helyes megvalositas eseten peldaul egy jobbra, majd ketto lefele lepes eseten ez a helyes kimenet:


████████
██🧙░░██
██░░░░░░
██░░░░██
Moving right is successful
██████████
██░░🧙████
██░░░░░░░░
██░░░░██░░
Moving down is successful
██████████
██░░░░████
██░░🧙░░░░
██░░░░██░░
████████░░
Moving down is successful
The wizard stepped on a mine and died.
██░░░░████
██░░░░░░░░
██░░💀██░░
████████░░
██░░░░░░░░

"""

###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################

character={"name":"The wizard", "icon": "🧙", "position":{"x":1,"y":1},"vision":2}

landmines=[
    {"name": "mine 1", "position" : {"x":1,"y":2}},
    {"name": "mine 2", "position" : {"x":2,"y":3}},
    {"name": "mine 3", "position" : {"x":4,"y":3}},
]

map = [
    ["█","█","█","█","█","█"],
    ["█","░","░","█","█","█"],
    ["█","░","░","░","░","█"],
    ["█","░","░","█","░","█"],
    ["█","█","█","█","░","█"],
    ["█","░","░","░","░","█"],
    ["█","█","█","█","█","█"]
]


while True:
    if stepped_on_mine(character,landmines):
        character["icon"] = "💀"
        print(character["name"],"stepped on a mine and died.")
        pretty_map_print(map,character)
        break
    pretty_map_print(map,character)
    command = input()
    if command=="end": break
    print ("Moving "+command+" is "+ 
        ("successful" if move(map,character,command) else "impossibru")
    )
