
percek = []
smsek = []
percekelemek = 0
smsekelemek = 0
total = 0

for hónap in range(12):
    percekelemek = int(input())
    percek.append(percekelemek)
    smsekelemek = int(input())
    smsek.append(smsekelemek)

havidíj = int(input())
percdíj = int(input())
smsdíj = int(input())
költség = 0
szamla=[]

for hónap in range(12):
    nagyobb = (percek[hónap] * percdíj) + (smsek[hónap] * smsdíj)
    if nagyobb > havidíj:
        költség = nagyobb
        szamla.append(költség)
        
    else:
        költség = havidíj
        szamla.append(költség)

for i in range(len(szamla)):
    total = szamla[i] + total


print(szamla)
print(total)


