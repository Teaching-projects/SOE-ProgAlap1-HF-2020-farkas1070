"""
A hosunk nem lat el a vegtelensegig. X-Ray vision megvan, mint Supermannek, amiatt nem kell aggodni, de van mostantol egy "vision" tulajdonsaga, ami megmondja, hogy mekkora "korben" (negyzet valojaban) lat. Ha mondjuk a vision 3, akkor egy 7x7-es negyzetet lat, mert 3-nyit lat el balra jobbra, fel le. Tehat mondjuk a korabbi peldanal maradva a kezdoallapot:

██████████
██🧙░░░░░░
██░░░░░░░░
██░░░░████
██░░░░██░░

Balra itt nem lat el 3-at, meg felfele, mert nincs annyi a palyabol ugye. Egy jobbra lepes utan:
████████████
██░░🧙░░░░░░
██░░░░░░░░░░
██░░░░██████
██░░░░██░░░░
majd lefele:
████████████
██░░░░░░░░░░
██░░🧙░░░░░░
██░░░░██████
██░░░░██░░░░
██░░░░░░░░░░
meg 3x le, aztan jobbra:
██░░░░░░░░░░░░
██░░░░████████
██░░░░██░░░░░░
██░░░░🧙░░░░░░
██████████░░░░
██░░░░░░░░░░░░
██████████████
Es akkor itt most mar "teljesen kihasznalja" a latasat. 


A bemenetek lekezeleset elintezi a foprogram, eloszor beker egy ilyen "vision" erteket, majd utana a mozgasokat ugy, ahogy mult heten.

Terkepnek a korabbit hasznalja, es ugyanugy a bal felso ficakbol indulunk.

"""

def pretty_map_print(map, character):
    x = character["position"]["x"]
    y = character["position"]["y"]
    sorok = len(map[1])
    oszlopok = len(map)

    if (x <= sorok - 1 and x >= 0) and (y <= oszlopok - 1 and y >= 0): 
        map[y][x] = "🧙"

    látás = character["vision"]
    #for i in range(map[(y-látás):(y+látás)]):
       # for j in range(map[(x-látás):(x+látás)]):
         #   print(map[i][j])
          #  if map[i][j] != "🧙":
             #   print(map[i][j])
     #   print('')
    if y <= látás and x <= látás:
        for i in range(len(map[0:y+látás+1])):
            for j in range(len(map[0:x+látás+1])):
                print(map[i][j],end='')
                if map[i][j] != "🧙":
                    print(map[i][j],end='')
            print('')
    if y > látás and x > látás:
        for i in range(map[y-látás:y+látás]):
            for j in range(map[x-látás:x+látás]):
                print(map[i][j],end='')
                if map[i][j] != "🧙":
                    print(map[i][j],end='')
        print('')
    if y > látás and x <= látás:
        for i in range(map[y-látás:y+látás]):
            for j in range(map[0:x+látás+1]):
                print(map[i][j],end='')
                if map[i][j] != "🧙":
                    print(map[i][j],end='')
        print('')
    if y <= látás and x > látás:
        for i in range(map[0:y+látás+1]):
            for j in range(map[x-látás:x+látás]):
                print(map[i][j],end='')
                if map[i][j] != "🧙":
                    print(map[i][j],end='')
        print('')

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
    else:
        return False



###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


vision=int(input())
character={"name":"The wizard", "position":{"x":1,"y":1},"vision":vision}
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
