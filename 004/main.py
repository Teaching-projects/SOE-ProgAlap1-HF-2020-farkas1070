"""
Kerj be ket egesz szamot (feltetelezhetjuk, hogy pozitivak), es ird ki a legnagyobb kozos osztojukat, majd a legkisebb kozos tobbszorosuket.

pl:
Bemenet:
6
27
Kimenet:
3
54
"""
def lko(szám1, szám2):
    if szám2 ==0:
        return szám1
    else:
        return lko(szám2, szám1 % szám2)
szám1 = int(input())
szám2 = int(input())
érték = lko(szám1, szám2)
print(érték)
lkt = (szám1 * szám2) / érték
print(int(lkt))