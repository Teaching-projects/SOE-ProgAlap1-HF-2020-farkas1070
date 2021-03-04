"""
Az feladat egy olyan osztaly letrehozsa, melyben mert adatok listajat tudjuk tarolni, illetve errol mindenfele "statisztikai" dolgot megmondani. Az egyszerueseg kedveert feltetelezzuk, hogy  mert adatok csak egeszek lesznek.

A tesztek az ebben a docstringben megadott peldakra mennek le.

Egy ilyen datasetet igy hozhatunk egyszeruen letre, ahol csak megadjuk, hogy miket vizsgalunk.

>>> ds=DataSet("Szekek szama irodakban")

Ezt kovetoen a `record` metodussal tudunk uj adattokat beletenni.

>>> for cc in [3,4,5,4,5,4,3,4,5,6,5,4,4,3,4,5]: 
...     ds.record(cc)

Ezek utan mar peldaul ki lehet rajzoltatni egy hisztogrammot:

>>> ds.print_histogram()
Szekek szama irodakban
----------------------
    3 | ###
    4 | #######
    5 | #####
    6 | #

Ennek a fuggvenynek olyan kimenetet kell generalnia, hogy kiirja a dattaset nevet, alahuzza gondolatjelekkel, majd vegigmegy az ertekeken aa legkisebbtol a legnagyobbikig, es soronkent kiirja oket 5 karakter szelesen jobbra igazitva, majd egy elvalsazto resz, es utan annyi #, ahanyszor az az ertek elofordult.


Ha van olyan ertek, ami nem szerepelt egyszer sem, de benne van ebben az intervallumban, akkor is megjelenik, csak 0 db #-tel:

>>> ds.record(9)
>>> ds.print_histogram()
Szekek szama irodakban
----------------------
    3 | ###
    4 | #######
    5 | #####
    6 | #
    7 | 
    8 | 
    9 | #

A legkisebb, legnagyobb mert erteket, valamint a mert ertekek intervallumat a kovetkezo fuggvenyek adjak vissza:

>>> ds.min()
3
>>> ds.max()
9
>>> ds.range()
(3, 9)

Nehany tovabbi meres utan:

>>> for cc in [3,5,6,8,6,12,1,3]: ds.record(cc)
>>> ds.min()
1
>>> ds.max()
12
>>> ds.range()
(1, 12)

Legyen az osztalyhoz par statisztiki fuggveny is, mint pl:

A `count` megszamolja, hogy egy adott ertek hanyszor fordult elo:
>>> ds.count(3)
5
>>> ds.count(2)
0
>>> [ds.count(x) for x in range(20)]
[0, 1, 0, 5, 7, 6, 3, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]


Az `average` megadja hogy mennyi volt az atlag mert ertek:
>>> ds.average()
4.84

Vegezetul a `probability` megdja a mert statisztikk alapjan, hogy egy adott erteknek mennyi a valoszinusege:
>>> ds.probability(3)
0.2
>>> ds.probability(2)
0.0
>>> [ds.probability(x) for x in range(20)]
[0.0, 0.04, 0.0, 0.2, 0.28, 0.24, 0.12, 0.0, 0.04, 0.04, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

Egy masik teszt:
>>> ds2 = DataSet("Felev vegi jegyek")
>>> for cc in [5,5,4,5,3,4,5,5]: ds2.record(cc)

>>> ds2.min()
3
>>> ds2.max()
5
>>> ds2.range()
(3, 5)
>>> ds2.average()
4.5
>>> for grade in range(1,6):
...     print(f"{grade} - {ds2.count(grade)} times - {int(100 * ds2.probability(grade))}% ")
1 - 0 times - 0% 
2 - 0 times - 0% 
3 - 1 times - 12% 
4 - 2 times - 25% 
5 - 5 times - 62% 
>>> ds2.print_histogram()
Felev vegi jegyek
-----------------
    3 | #
    4 | ##
    5 | #####
"""

class DataSet:

    def __init__(self, name) -> None:
        self.name = name
        self.datalist = []

    def record(self,data) -> None:
        self.datalist.append(data)
    
    def average(self) -> float:
        total_value = 0
        for value in range(len(self.datalist)):
            total_value += self.datalist[value]
        return total_value / len(self.datalist)

    def min(self) -> int:
        return min(self.datalist)


    def max(self) -> int:
        return max(self.datalist)
    
    def count(self,x) -> int:
        return self.datalist.count(x)

    
    def probability(self,x) -> float:
        return round(self.count(x) / len(self.data), 2)
    
    def range(self) -> tuple:
        min_value = self.min()
        max_value = self.max()
        return (min_value, max_value)

    def print_histogram(self) -> None:
        print(self.name)
        for character in range(len(self.name)):
            if character != len(self.name) - 1:
                print("-", end= "")
            else:
                print("-")
        intervaal = self.range()
        intervaal = list(intervaal)
        for i in range(intervaal[1] + 1):
            if i > intervaal[0] and i not in intervaal:
                intervaal.append(i)
        intervaal.sort()
        for i in range(len(intervaal)):
            amount = self.datalist.count(intervaal[i])
            for x in range(8):
                if x < 4:
                    print(" ",end= "")
                elif x == 4:
                    print(intervaal[i], end= "")
                elif x == 5 or x == 7:
                    print(" ",end= "")
                elif x == 6:
                    print("|",end= "")
            for n in range(amount):
                if n != amount:
                    print("#",end= "")
                else:
                    print("#")
            print("")
                
            
            


