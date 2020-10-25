
egyenleg = 0
hónap = 0
nincs_kamat = 0

while hónap != 12:
    pénzmozgás = int(int(input()))
    egyenleg += pénzmozgás
    nincs_kamat += pénzmozgás
    if hónap != 0:
        egyenleg -= 2000
    if egyenleg > 0:
        egyenleg += int(egyenleg * 0.05)
    else:
        egyenleg += int(egyenleg * 0.1)
    hónap += 1


print(int(egyenleg))
print(nincs_kamat)
