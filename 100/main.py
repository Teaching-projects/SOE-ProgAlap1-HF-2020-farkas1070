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
    távolság = 0
    if p2x < p1x:
        távolság = math.sqrt(((abs(p2x-p1x))**2) + ((abs(p2y-p1y))**2))
    return távolság
   
# Ez a fuggveny egy gpx-et var, ami a fent leirt pontokbol allo lista.
# A fuggveny adja meg a track teljes hosszat, ami a pontok kozotti legvonalbeli tavolsagok osszege.
# Nem kell foglalkozni 3d tavolsaggal, csak a "felulnezeti tavolsaggal".
def total_distance(gpx):
    total_distance = 0
    for i in range(len(gpx)):
        distance = position_distance(gpx[i]["position"], gpx[i+1]["position"])
        total_distance += distance
    return total_distance


# Ez adja meg maasodpercben, milyen hosszan futottunk
def total_time(gpx):
    összmásdopercek = 0
    for i in range(len(gpx)):
        eltérés = gpx[i+1]["timestamp"] - gpx[i]["timestamp"]
        összmásdopercek += eltérés
    return összmásdopercek
# Ez a fuggveny adja meg masodpercben, hogy a futas soran hany masodpercig alldogaltunk csak futas helyett.
# Alldogalasnak szamit, ha ket meresi pont kozott nem valtozik a pozicio
def idle_time(gpx):
    standingsecs = 0
    for i in range(len(gpx)):
        if gpx[i+1]["position"] == gpx[i]["position"]:
            eltérés = gpx[i+1]["timestamp"] - gpx[i]["timestamp"]
            eltérés += standingsecs
    return standingsecs

# Ez a fuggveny adja vissza masodpercben, hogy mennyit mozogtunk
def moving_time(gpx):
    mozgási_idő = None
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
    idő = seconds
    idő = str(idő)
    if len(idő) == 4:
        minutes1 = idő[0]
        minutes2 = idő[1]
        allminutes = idő[0:2]
        seconds1 = idő[0]
        seconds2 = idő[1]
        allseconds = idő[3:5]
        if miutes1 == 0 or seconds1 == 0:
            if minutes1 == 0 and seconds1 != 0:
                string = "{}:{}".format(minutes2,allseconds)
                return string
            if minutes1 !=0 and seconds1 == 0:
                string = "{}:{}".format(allminutes,seconds2)
                return string
            if minutes1 == 0 and seconds1 == 0:
                string = "{}:{}".format(minutes2,seconds2)
                return string
        elif minutes1 != 0 and seconds1 != 0:
            string = "{}:{}".format(allminutes,allseconds)
            return string
    if len(idő) == 6:
        hours1 = idő[0]
        hours2 = idő[1]
        allhours = idő[0:2]
        allminutes = idő[2:4]
        seconds1 = idő[4]
        seconds2 = idő[5]
        allseconds = idő[4:6]
        if hours1 == 0 or seconds1 == 0:
            if hours1 == 0 and seconds1 != 0:
                string = "{}:{}:{}".format(hours1,allminutes,allseconds)
                return string
            if hours1 !=0 and seconds1 == 0:
                string = "{}:{}:{}".format(allhours,allminutes,seconds2)
                return string
            if hours1 == 0 and seconds1 == 0:
                string = "{}:{}:{}".format(hours2,allminutes,seconds2)
                return string
        elif hours1 != 0 and seconds1 != 0:
            string = "{}:{}:{}".format(allhours,allminutes,allseconds)
            return string

# Ez a fuggveny szamolja ki, hogy mennyi volt az osszes emelkedes, azaz hany metert mentunk felfele
def total_ascent(gpx):
    összesemelkedés = 0
    for i in range(len(gpx)):
        távolság = position_distance(gpx[i]["position"], gpx[i+1]["position"])
        if gpx[i]["elevation"] > 0:
            távolság += összesemelkedés
    return összesemelkedés


# Ez a fuggveny keresse meg a gpx track elejen azt a legrovidebb reszt, ami mar atlepi a megadott tavolsagot, majd errol a reszrol adjon vissza egy masolatot.
# A fuggveny adjon vissza egy ures tracket, ha az egesz gpx track nincs olyan hosszu, mint a megadott tavolsag.
def chop_after_distance(gpx, distance):
    track = []
    össztáv = 0
    for i in range(len(gpx)):
        if össztáv > distance:
            return track
        else:
            össztáv += position_distance(gpx[i]["position"], gpx[i+1]["position"])
    if len(track) == 0:
        return track

# Ez a fuggveny keresse meg a leggyorsabb, legalabb 1 km-es szakaszt a trackben, es adjon vissza rola egy masolatot
def fastest_1k(gpx):
    minimum = 100000000000
    for i in range(len(gpx)):
        lista = chop_after_distance(gpx,1000)
        if lista[-1]["timestamp"] < minimum:
            minimum = lista[-1]["timestamp"]
        else:
            lista = chop_after_distance(gpx,1000)
    return lista

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

