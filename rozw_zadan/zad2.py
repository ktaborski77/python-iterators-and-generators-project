def rotator_zadan(lista_zadan):
    while True:
        for zadanie in lista_zadan:
            yield zadanie

lista = ["Nauka", "Sprzątanie", "Relaks"]
gen = rotator_zadan(lista)

for dzien in range(1,8):
    zadanie = next(gen)
    print(f"Dzień {dzien}: {zadanie}")