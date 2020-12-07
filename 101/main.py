from typing import Dict, List

Tippek=List[str]
"""Leadott tippek, azaz betűk listájának típusa."""

def kozte_van(betu:str, betuk:Tippek) -> bool:
    """Megadja, hogy a listában már benne van-e a megadott betű, vagy sem.

    Args:
        betu (str): a keresett betű
        betuk (Tippek): betűk listája

    Returns:
        bool: `True` ha benne van, `False` ha nincsen.
    """

    hamis = 1
    for i in range(len(betuk)):
        if betuk[i] == betu:
            return True
        else:
            hamis += 1
        
        if hamis == len(betuk):
            return False

specialis_karakterek=[' ','.',',','!','?',':','-']

def megjelenites(szo:str, betuk:Tippek) -> str:
    """Visszaad egy olyan szót, amiben a `betuk`-ben lévő betűk látszanak, minden más helyére `_` kerül, kivéve néhány speciális karaktert, amik megjelennek változtatás nélkül. Ezen karakterek listája a `specialis_karakterek` globális listában adott.

    Kis és nagy betűket megkülönbözteti a függvény.

    Args:
        szo (str): a szó, aminek megjelenített változatát meg szeretnénk kapni. 
        betuk (Tippek): Egy karakterből, betűkből álló lista, amit már tippeltünk

    Returns:
        str: a megjelenített változata a szónak
    """

    word = ""
    for i in range(len(szo)):
        if szo[i] in betuk and szo[i] == betuk[i]:
            word = word + szo[i]
        elif szo[i] in betuk and szo[i] != betuk[i]:
            word = word + "_"
        elif szo[i] in specialis_karakterek:
            for j in specialis_karakterek:
                if j == szo[i]:
                    word +=  specialis_karakterek[j]
    
    return word

def megfejtett(szo:str, betuk:Tippek) -> bool:
    """Megadja, hogy sikerült-e már megfejtenünk a szót, azaz minden benne levő betű már a tippjeink között van.

    Args:
        szo (str): a kitalálandó szó
        betuk (Tippek): az eddig tippelt betűk

    Returns:
        bool: `True` ha teljesen megfejtettük a szót, `False` különben
    """
    jo_tippek = 0
    for i in range(len(szo)):
        if szo[i] in betuk:
            jo_tippek += 1
    
    if jo_tippek == len(szo):
        return True
    else:
        return False


def tartalmazza(szo:str, betu:str) -> bool:
    """Megadja, hogy a megaadott betű szerepel-e a megadott szóban.

    Args:
        szo (str): a szó
        betu (str): a betű, amit keresünk, feltételezhető, hogy 1 karakter hosszú

    Returns:
        bool: `True` ha szerepel, `False` ha nem
    """
    betuk = []
    for i in range(len(szo)):
        betuk.append(szo[i])
    
    if betu in betuk:
        return True
    else:
        return False
    


def rossz_tippek(szo:str, betuk:Tippek) -> int:
    """Megadja, hogy hány rossz betűt tippeltünk eddig.

    Args:
        szo (str): a kitalálandó szó
        betuk (Tippek): az eddigi betű tippjeink

    Returns:
        int: a rossz tippek száma
    """
    rossz_tippek = 0
    szobetui = []

    for i in range(len(szo)):
        szobetui.append(szo[i])

    for i in range(len(betuk)):
        if betuk[i] not in szobetui:
            rossz_tippek += 1
    
    return rossz_tippek


def eletek(osszes:int,elhasznalt:int)->str:
    """Visszaad egy olyan szöveget, ami egy indikátor arra, hány életünk van még.

    A szöveg elején van annyi 😄 ahány életünk még maradt, majd annyi 💀 ahányat már "eljátszottunk".

    Args:
        osszes (int): az összes életünk száma
        elhasznalt (int): az eljátszott életek (rossz betű tippek) száma

    Returns:
        str: 😄😄😄💀💀 formátumú indikátor (a példa adatai: 5 összes, 2 elhasznált)
    """
    osszeselet = osszes
    elhasznalt = rossz_tippek(szo,Tippek)
    eletek = ""

    for i in range(len(osszeselet-elhasznalt)):
        eletek = eletek + "😄"
    
    for i in range(len(elhasznalt)):
        eletek = eletek + "💀"
    
    return eletek

def akasztofa(szo:str,osszes_elet:int) -> None:
    """Végigvisz egy akasztófa játékot, ahol a megadott szót kell kitalálni, és `osszes_elet` rossz tipp után vesztettünk.

    A játék minden körben először írja ki, hogy mit látunk a megfejtendő szóból, alá egy indikátort arról, hogy hány életünk van még, majd végül a tippelt karakterek listáját a tippek sorrendjében.

    Ezt követően az "Adja meg a kovetkezo betut: " kiírással kérjünk be egy betűt. Ellenőrzés nem szükséges se arra, hogy egyetlen betűt adtunk-e meg, se arra, hogy volt-e már korábban ez a betű. A megadott betűt irassuk is rögtön ki. (Szimplán, egymagában. Ennek pusztán annyi célja van, hogy nyomon követhetőbbek legyenek az out fájlok.)

    Más kiiratás nem történik, a játék logikája egyértelmű: addig adunk le tippeket betűkre, amíg vagy meg nem fejtődik a szó, vagy el nem fogynak az életeink. Többször leadhatjuk ugyanazt a tippet, de ez rossz, akkor több életet is vesz el. A kiíratott listában is jelenjen meg duplán akkor ez a betű.

    Ha nyertünk, még kerüljön kiírásra a megfejtett szó, valamint alá egy olyan szöveg, hogy "Gratulalok, nyertel, es meg X eleted maradt!", ahol X értelemszerűen a megmaradt életek száma.

    Ha vesztettünk, akkor egy "Sajnalom, nem nyertel, ez lett volna a megoldas: MEGOLDAS".

    Példakimenetek adottak.
    

    Args:
        szo (str): a megfejtendő szó
        osszes_elet (int): az életeink száma, azaz hány rossz tipp után vesztettünk
    """
    megmaradt_életek = osszes_elet
    index = 0
    if index > 0:
        rosszak = rossz_tippek(szo,Tippek)
    else:
        rosszak = 0
    
    while (rosszak != osszes_elet) or (megfejtett(szo, Tippek) == False) or index == 0:
        print(megjelenites(szo, Tippek))
        print(eletek(maxelet,rosszak))
        print(Tippek)
        betu = input("Adja meg a kovetkezo betut: ")
        Tippek.append(betű)
    
        megmaradt_életek -= 1
        index += 1

    if megfejtett(szo, Tippek) == True:
        print(megfejtett(szo, Tippek))
        print("Gratulalok, nyertel, es meg {} eleted maradt!".format(megmaradt_életek))
    
    if rossz_tippek == osszes_elet:
        print("Sajnalom, nem nyertel, ez lett volna a megoldas: {}".format(szo))

    



# Ez alatt ne tessek modositani.

szo=input()
maxelet=int(input())
akasztofa(szo,maxelet)





