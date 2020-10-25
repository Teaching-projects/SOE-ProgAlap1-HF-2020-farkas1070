x=0.0
y=0.0


origo_távolság = 0
x = 0
y = 0

parancs = input()

while parancs != "stop":
    if parancs == "forward":
        mennyiség = float(input())
        y += mennyiség
        parancs = input()
    if parancs == "right":
        mennyiség1 = float(input())
        x += mennyiség1
        parancs = input()
    if parancs == "left":
        mennyiség2 = float(input())
        x -= mennyiség2
        parancs = input()
    if parancs == "backward":
        mennyiség3 = float(input())
        y -= mennyiség3
        parancs = input()
    if parancs == "stop":
        print(round(x, 2))
        print(round(y, 2))


origo_távolság = ((x **2) + (y**2)) ** (1/2)
print(round(origo_távolság, 2))



    