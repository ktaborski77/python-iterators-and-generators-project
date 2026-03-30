def suma_kroczaca(liczby):
    suma = 0  # Ta zmienna zostanie "zamrożona" przy każdym yield!
    for n in liczby:
        suma += n
        yield suma  # Zwracamy aktualny stan i czekamy na next()

# TEST ZADANIA 3
dane = [10, 20, 30, 40]
gen = suma_kroczaca(dane)

print("=== SYMULACJA AKUMULATORA ===")
for wynik in gen:
    print(f"Otrzymano wartość: {wynik}")