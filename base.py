numery_odbiorcow = []

with open("odbiorcy_przyklad.txt") as plik:
    for line in plik:
        for l in line.split():
            numery_odbiorcow.append(int(l))
obecni_odb = numery_odbiorcow

def rundy(obecni_odbiorcy, numery_odbiorcow):
    bufor = [[] for x in range(0, len(numery_odbiorcow))]
    obenca_tura = [0 for x in range(0, len(numery_odbiorcow))]

    for x in range(0, len(obecni_odbiorcy)):
        bufor[obecni_odbiorcy[x] - 1].append(x + 1)
    for k in range(0, len(numery_odbiorcow)):
        for x in bufor[k]:
            obenca_tura[x - 1] = numery_odbiorcow[k]
    print(obenca_tura)
    return obenca_tura


print(numery_odbiorcow)
for x in range(0, 1):
    obecni_odb = rundy(obecni_odb, numery_odbiorcow)
