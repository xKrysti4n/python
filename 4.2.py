
ile_potrzeba_liter = {'w':1, 'a':2, 'k':1, 'c':1, 'j':1, 'e':1}

slowa = []
with open("przyklad.txt") as plik:
    for line in plik:
        slowa.append(line.strip())

def policz_wystapienia(pojedyncze_slowo):
    obecny_licznik = {'w':0, 'a':0, 'k':0, 'c':0, 'j':0, 'e':0}
    for litera in pojedyncze_slowo:
        if litera in obecny_licznik:
            obecny_licznik[litera] += 1
    return obecny_licznik



for pojedyncze_slowo in slowa:
    sprawdz_dla_tej_litery = policz_wystapienia(pojedyncze_slowo)
    wynik = min([sprawdz_dla_tej_litery[index] // wartosc for index,wartosc in ile_potrzeba_liter.items()])



    print(wynik,end=" ")
