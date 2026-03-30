import random

def symulator_gieldy(cena):
    while True:
        zmienność = random.randint(-5, 5) # Losujemy zmianę
        cena += zmienność
        yield cena

# TEST ZADANIA 4
start = 100
gen_giełda = symulator_gieldy(start)

print(f"=== START NOTOWAŃ (Cena wejścia: {start}) ===")
ostatnia_cena = start

for i in range(1, 11):
    ostatnia_cena = next(gen_giełda)
    print(f"Notowanie {i:2}: {ostatnia_cena} PLN")

# Podsumowanie
roznica = ostatnia_cena - start
status = "ZYSK" if roznica > 0 else "STRATA"
print(f"=== KONIEC DNIA: {status} ({roznica} PLN) ===")