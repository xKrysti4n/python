import re
slowa = []
with open("slowa.txt") as plik:
    for line in plik:
        slowa.append(line.strip())

for pojedyncze_slowo in slowa:
    ile_w = re.findall(r'w', pojedyncze_slowo)
    ile_k = re.findall(r'k', pojedyncze_slowo)
    if len(ile_w) == len(ile_k):
        print(pojedyncze_slowo)


# https://www.korepetycjezinformatyki.pl/wp-content/uploads/nowa-rozszerzona/informatyka-2023-maj-matura-rozszerzona-2.pdf
# https://www.korepetycjezinformatyki.pl/wp-content/uploads/nowa-rozszerzona/informatyka-2023-maj-matura-rozszerzona-odpowiedzi.pdf