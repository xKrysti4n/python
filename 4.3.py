
ile_potrzeba_liter = {'w':1, 'a':2, 'k':1, 'c':1, 'j':1, 'e':1}

slowa = []

with open("slowa.txt") as plik:
    for line in plik:
        slowa.append(line.strip())

def policz_wystapienia(pojedyncze_slowo):
    obecny_licznik = {'w':0, 'a':0, 'k':0, 'c':0, 'j':0, 'e':0}
    for litera in pojedyncze_slowo:
        if litera in obecny_licznik:
            obecny_licznik[litera] += 1
    return obecny_licznik

def sparawdz_czego_mniej(slowo,ile_wystapien_wakacje):
    if ile_wystapien_wakacje == 0:
        return len(slowo)
    else:
        return len(slowo) - ile_wystapien_wakacje * 7

for pojedyncze_slowo in slowa:
    sprawdz_dla_tego_slowa = policz_wystapienia(pojedyncze_slowo)
    ile_razy_wakacje = min([sprawdz_dla_tego_slowa[index] // wartosc for index,wartosc in ile_potrzeba_liter.items()])

    wynik = sparawdz_czego_mniej(pojedyncze_slowo,ile_razy_wakacje)
    print(wynik,end=" ")


