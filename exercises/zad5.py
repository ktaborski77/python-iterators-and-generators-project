import itertools
def paczki_danych(iterable, rozmiar):
    iterator = iter(iterable)
    while True:
        paczka = list(itertools.islice(iterator, rozmiar))
        if not paczka:
            break
        yield paczka

for batch in paczki_danych([1, 2, 3, 4, 5, 6, 7], 3):
    print(batch)