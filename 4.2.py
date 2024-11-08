numery_odbiorcow = []

with open("odbiorcy_przyklad.txt") as plik:
    for line in plik:
        for l in line.split():
            numery_odbiorcow.append(int(l))
obecni_odb = numery_odbiorcow

def rundy(obecni_odbiorcy, numery_odbiorcow, obecna_runda):
    obecna_runda += 1
    bufor = [[] for x in range(0, len(numery_odbiorcow))]
    obenca_tura = [0 for x in range(0, len(numery_odbiorcow))]

    for x in range(0, len(obecni_odbiorcy)):
        bufor[obecni_odbiorcy[x] - 1].append(x + 1)

    for k in range(0, len(numery_odbiorcow)):
        for x in bufor[k]:
            obenca_tura[x - 1] = numery_odbiorcow[k]

    for p in range(0, len(obenca_tura)):
        if obenca_tura[p] - 1 == p:
            print(f"Znaleziono pakiet {obenca_tura[p]} w rundzie {obecna_runda}")
            return 

    # print(obenca_tura)

    return obenca_tura, obecna_runda

obecna_r = 1
# print(numery_odbiorcow)
for x in range(0, 4):
    wynik = rundy(obecni_odb, numery_odbiorcow, obecna_r)
    # print(wynik)
    if wynik is None:
        break
    obecni_odb, obecna_r = wynik
