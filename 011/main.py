"""
Ez a program nem fog mast csinalni, mint inicializal nekunk egy "terkepet", ami nem lesz mas, mint egy listakbol allo lista. 

A kovetkezo terkep:

██████████████
█░░░░░░███████
█░░░░░░███░░░█
█░░███████░█░█
█░░█░░░░░█░█░█
█░░░░░░█░█░█░█
█████░░█░█░█░█
█░░░░░░█░░░█░░
██████████████


peldaul igy lenne eltarolva egy listakbol allo listaban:

terkep = [
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","░","░","░","█"],
    ["█","░","░","█","█","█","█","█","█","█","░","█","░","█"],
    ["█","░","░","█","░","░","░","░","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","█","░","█","░","█"],
    ["█","█","█","█","█","░","░","█","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","░","░","█","░","░"],
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"]
]

Tehat a terkep[0][0] a terkep bal felso sarkat tartalmazza, a terkep[0][1] a tole jobbra levo mezot, stb. A lista jobb felso sarka most a terkep[0][13], a jobb also pedig a terkep[8][13].

Ez egy "felulnezet" egy epuletre, ahol █ reprezentalj a falakat, es ░ a szabadon bejarhato teruletet.

Elso alkalommal most az a feladat, hogy irjatok egy olyan fuggvenyt, ami visszaad egy ilyen terkepet.
"""


def initialize_map (width, height):
    térkép = []

    
    tégla = "█"
    nincs_tégla = "░"
    for i in range(1):
        egység = ["█"]*width
        térkép.append(egység)
    for i in range(height-2):
        egység = []
        egység.append(tégla)
        for i in range(width-2):
            egység.append(nincs_tégla)
        egység.append(tégla)
        térkép.append(egység)
    for i in range(1):
        egység = ["█"]*width
        térkép.append(egység)
            

    return térkép


"""
peldaul az initialize_map(3,4) a kovetkezo listat adja vissza:
[["█","█","█"],["█","░","█"],["█","░","█"],["█","█","█"]]

Ami nem mas, mint:
[
    ["█","█","█"],
    ["█","░","█"],
    ["█","░","█"],
    ["█","█","█"]
]

Egy kicsit nagyobb pelda: initialize_map(10,6) eredmenye:
[
    ["█","█","█","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","█","█","█","█","█","█","█","█","█"]
]
"""


###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


width=int(input())
height=int(input())
print(initialize_map(width,height))
