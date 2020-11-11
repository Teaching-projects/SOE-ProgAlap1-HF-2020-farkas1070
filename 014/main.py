"""
Ideje mozgatni a hosunket :-)

A bemenetek lekezeleset elintezi a foprogram, Nektek csak egy move fuggvenyt kell megirni, ami megprobalja a megadott iranyba mozgatni a hosunket. 

Ez az irany lehet "up", "down", "left", "right".

Hogy ne egy unalmas ures palyan mozogjunk, a foprogram most fixen az alabbi helyzetbol indit: 

████████████████████████████
██🧙░░░░░░░░░░██████████████
██░░░░░░░░‍░░░░██████░░░░░░██
██░░░░██████████████░░██░░██
██░░░░██░░░░░░░░░░██░░██░░██
██░░░░░░░░░░░░██░░██░░██░░██
██████████░░░░██░░██░░██░░██
██░░░░░░░░░░░░██░░░░░░██░░██
████████████████████████████

A szabaly a mozgasra nyilvan a kovetkezo: ha val van, nem tudunk oda menni. A palyarol feltetelezhetjuk, hogy zart, azaz nem lehet rola lemenni, ezt kulon nem kell vizsgalni.

"""

def pretty_map_print(map, character):
    x = character["position"]["x"]
    y = character["position"]["y"]
    sorok = len(map[1])
    oszlopok = len(map)

    if (x <= sorok - 1 and x >= 0) and (y <= oszlopok - 1 and y >= 0): 
        map[y][x] = "🧙"

    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end='')
        print()


def move(map,character,direction):
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




###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


character={"name":"The wizard", "position":{"x":1,"y":1}}
map = [
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","░","░","░","█"],
    ["█","░","░","█","█","█","█","█","█","█","░","█","░","█"],
    ["█","░","░","█","░","░","░","░","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","█","░","█","░","█"],
    ["█","█","█","█","█","░","░","█","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","░","░","█","░","█"],
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"]
]

while True:
    pretty_map_print(map,character)
    command = input()
    if command=="end": break
    print ("Moving "+command+" is "+ 
        ("successful" if move(map,character,command) else "impossibru")
    )
