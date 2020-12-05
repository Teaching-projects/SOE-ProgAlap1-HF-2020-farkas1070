"""
Ebben a perogramban a celunk egy futasok adatait rogzito fajlok statisztikainak kiiratasa.

Az alap adatszerkezetunke gy ilyen dictionary:

{"position":(x,y), "timestamp":ts, "elavation:e}

ahol:
 - x es y meterben megadott koordinatak egy alap viszonyitasi ponthoz kepest
 - ts egy egesz timestamp, ami masodpercben mondja meg, mennyi ido telt el ejfel ota
 - e pedig egy folytonos, meterben mert ertek a tengerszint feletti magassagrol


egy gpx track nem mas, mint ilyen adatpontoknak egy listaja.

A feladatban tobb, esetenkent egymasra epulo fuggvenyt kell megirni, melyek errol a trackrol arulnak el informaciokat.

"""

# Ez a fugggveny adja meg ket position kozotti legvonalbeli tavolsagot meterben. 
# p1 es p2 is (x,y) tuple-ok
def position_distance(p1,p2):
    import math
    p1x = p1[0]
    p1y = p1[1]
    p2x = p2[0]
    p2y = p2[1]
    távolság = math.sqrt(((abs(p2x-p1x))**2) + ((abs(p2y-p1y))**2))
    return távolság
   
# Ez a fuggveny egy gpx-et var, ami a fent leirt pontokbol allo lista.
# A fuggveny adja meg a track teljes hosszat, ami a pontok kozotti legvonalbeli tavolsagok osszege.
# Nem kell foglalkozni 3d tavolsaggal, csak a "felulnezeti tavolsaggal".
def total_distance(gpx):
    total_distance = 0
    for i in range(len(gpx)-1):
        distance = position_distance(gpx[i]["position"], gpx[i+1]["position"])
        total_distance += distance
    return total_distance


# Ez adja meg maasodpercben, milyen hosszan futottunk
def total_time(gpx):
    összmásdopercek = 0
    for i in range(len(gpx)-1):
        eltérés = gpx[i+1]["timestamp"] - gpx[i]["timestamp"]
        összmásdopercek += eltérés
    return összmásdopercek
# Ez a fuggveny adja meg masodpercben, hogy a futas soran hany masodpercig alldogaltunk csak futas helyett.
# Alldogalasnak szamit, ha ket meresi pont kozott nem valtozik a pozicio
def idle_time(gpx):
    standingsecs = 0
    for i in range(len(gpx)-1):
        if gpx[i+1]["position"] == gpx[i]["position"]:
            eltérés = gpx[i+1]["timestamp"] - gpx[i]["timestamp"]
            eltérés += standingsecs
    return standingsecs

# Ez a fuggveny adja vissza masodpercben, hogy mennyit mozogtunk
def moving_time(gpx):
    mozgási_idő = 0
    összidő = total_time(gpx)
    nemmozgóidő = idle_time(gpx)
    mozgási_idő = összidő - nemmozgóidő
    return mozgási_idő


# Ez a fuggveny adjon vissza egy stringet, amiben "szepen" benne van egy eltelt ido, amit masodpercben kapunk meg
# Szep alat mm:ss formatumot ertjuk, ha nem volt legalabb egy ora, es hh:mm:ss formatumot, ha igen.
# Mindket esetben a legelso tag (mm vagy hh) eseteben nem szukseges a 2 szeles kiiras 0-val paddingolva, a tobbi pozicion viszont igen.
# Jo peldak: 3:14, 12:23:05, 1:00:01
# Rossz peldak: 03:14, 12:23:5, 1:0:1
def pretty_time(seconds):
    hours = seconds // (60*60)
    maradék1 = seconds - (hours*60*60)
    minutes = maradék1 // 60
    maradék2 = maradék1 - (minutes * 60)
    secs = maradék2
    if hours < 0:
        minutes = str(minutes)
        secs = str(secs)
        if len(minutes) != 2:
            minutes = "0{}".format(minutes)
        time = "{}:{}".format(minutes, secs)
        return time

    else:
        hours = str(hours)
        minutes = str(minutes)
        secs = str(secs)
        if len(minutes) != 2:
            minutes = "0{}".format(minutes)
        time = "{}:{}:{}".format(hours,minutes,secs)
        return time

# Ez a fuggveny szamolja ki, hogy mennyi volt az osszes emelkedes, azaz hany metert mentunk felfele
def total_ascent(gpx):
    összesemelkedés = 0
    for i in range(len(gpx)-1):
        távolság = position_distance(gpx[i]["position"], gpx[i+1]["position"])
        if gpx[i+1]["elavation"] > gpx[i]["elavation"]:
            összemelkedés += távolság
    return összesemelkedés


# Ez a fuggveny keresse meg a gpx track elejen azt a legrovidebb reszt, ami mar atlepi a megadott tavolsagot, majd errol a reszrol adjon vissza egy masolatot.
# A fuggveny adjon vissza egy ures tracket, ha az egesz gpx track nincs olyan hosszu, mint a megadott tavolsag.
def chop_after_distance(gpx, distance):
    track = []
    össztáv = 0
    for i in range(len(gpx)-1):
        if össztáv > distance:
            return track
        else:
            track.append(gpx[i])
            össztáv += position_distance(gpx[i]["position"], gpx[i+1]["position"])
    if len(track) == 0:
        return track

# Ez a fuggveny keresse meg a leggyorsabb, legalabb 1 km-es szakaszt a trackben, es adjon vissza rola egy masolatot
def fastest_1k(gpx):
    lista = gpx
    kilométeresek = []
    while True:
        szakasz = chop_after_distance(lista,1000)
        del lista[0:len(szakasz)]
        if len(szakasz) != 0:
            kilométeresek.append(szakasz)
    
    difference = 0
    differences = []

    for i in range(len(kilométeresek)):
        for j in range(len(kilométeresek[i])-1):
            if j == 0:
                difference = kilométeresek[i][j]["timestamp"][-1]
                differences.append(difference)
            else:
                difference = kilométeresek[i][j-(j+1)]["timestamp"] - kilométeresek[i+1][j-(j+1)]["timestamp"]
                differences.append(difference)
            
    legrövidebb = min(differences)
    for i in range(len(differences)):
        if differences[i] == legrövidebb:
            helyiérték = i
    
    for i in range(len(kilométeresek)):
        if i == helyiérték:
            return kilométeresek[i]

# Az alabbi reszek betoltenek egy ilyen pickle fajlt, es kiirjak a statisztikakat megformazva
import pickle

infile=open(input(),"rb")
gpx=pickle.load(infile)
infile.close()

print("Run statistics:")
print(" - Total distance: {:.2f} km".format(total_distance(gpx)/1000))
print(" - Total time    : {}".format(pretty_time(total_time(gpx))))
print(" - Total time    : {}".format(pretty_time(moving_time(gpx))))
print(" - Total ascent  : {:.0f} m".format(total_ascent(gpx)))
print(" - Fastest 1k    : {}".format(pretty_time(total_time(fastest_1k(gpx)))))