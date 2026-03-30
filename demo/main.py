import sys

# Funkcja generująca ogromną ilość danych "zachłannie" (Eager)
def eager_approach(n):
    # Tworzymy pełną listę w pamięci
    return [i**2 for i in range(n)]

# Funkcja generująca dane "leniwie" (Lazy)
def lazy_approach(n):
    # Używamy nawiasów okrągłych - to tworzy generator, nie listę!
    return (i**2 for i in range(n))

# --- TEST WYDAJNOŚCI ---
N = 10_000_000  # 10 milionów elementów

print(f"--- TEST DLA N = {N:,} ELEMENTÓW ---")

# 1. Test Listy (Eager)
try:
    data_list = eager_approach(N)
    size_list = sys.getsizeof(data_list) / (1024**2) # Konwersja na MB
    print(f"[LISTA] Rozmiar w pamięci: {size_list:.2f} MB")
except MemoryError:
    print("[LISTA] BŁĄD: Brak pamięci RAM dla listy!")

# 2. Test Generatora (Lazy)
data_gen = lazy_approach(N)
size_gen = sys.getsizeof(data_gen) # Rozmiar w bajtach
print(f"[GENERATOR] Rozmiar w pamięci: {size_gen} bajtów")

print("-" * 40)
print("WNIOSKI:")
print(f"Generator jest o około {int((size_list * 1024 * 1024) / size_gen)} razy lżejszy!")

def prosty_generator():
    print("--- Startuję! ---")
    yield "A"

#slajd 5:
# Prosta iteracja po liście
owoce = ["jabłko", "banan", "wiśnia"]

for owoc in owoce:
    print(f"Przetwarzam: {owoc}")

#slajd 6:
# Sprawdzamy, czy obiekty posiadają metodę __iter__
owoce = ["jabłko", "banan"]
liczba = 42

# 1. Lista (Zbiór danych) – posiada kontrakt
print(hasattr(owoce, "__iter__"))   # Wynik: True (Książka z danymi)

# 2. Liczba (Skalar) – nie posiada kontraktu
print(hasattr(liczba, "__iter__"))  # Wynik: False (Brak kontraktu)

# slajd 9
lista = ["A", "B"]

# To, co piszemy:
for x in lista:
    print(x)

# To, co faktycznie robi Python:
_iterator = iter(lista)  # 1. Wywołanie iter()

while True:
    try:
        x = next(_iterator)  # 2. Wywołanie __next__()
        print(x)
    except StopIteration:    # 3. Obsługa końca (wyjątek)
        break

#slajd 11
# 1. Mamy zwykły obiekt iterowalny (Iterable)
dane = [10, 20]

# 2. Tworzymy "wskaźnik" (Iterator)
it = iter(dane)

# 3. Ręcznie pobieramy elementy
print(next(it))  # Wynik: 10
print(next(it))  # Wynik: 20

# 4. Co się stanie, gdy dane się skończą?
#print(next(it))  # WYJĄTEK: StopIteration

#slajd 12:
class Odliczanie:
    def __init__(self, start):
        self.obecny = start

    def __iter__(self):
        # Iterator musi być "iterable", więc zwraca samego siebie
        return self

    def __next__(self):
        if self.obecny <= 0:
            raise StopIteration  # Sygnał końca danych
        
        wynik = self.obecny
        self.obecny -= 1
        return wynik

# Użycie:
licznik = Odliczanie(3)
for liczba in licznik:
    print(liczba)  # Wynik: 3, 2, 1
#to samo co wyżej ale za pomoca genertaora
def generator_odliczania(n):
    while n > 0:
        yield n  
        n -= 1

# Użycie (identyczne):
for i in generator_odliczania(3):
    print(i)
# WYJAŚNIENIE DLA SLAJDU 13:
print("Krok 1: Wywołuję funkcję")
moj_gen = prosty_generator()  # Tu się NIC nie wypisze w konsoli!

print("Krok 2: Sprawdzam typ obiektu")
print(type(moj_gen)) # Wypisze: <class 'generator'>

print("Krok 3: Dopiero teraz proszę o wynik")
print(next(moj_gen)) # Dopiero tu zobaczymy "--- Startuję! ---" i "A"


def generator_z_pamiecia():
    print("Pierwsze wywołanie")
    yield "Pierwszy wynik"
    
    print("Wracamy do funkcji i kontynuujemy")
    yield "Drugi wynik"
    

gen = generator_z_pamiecia()

print(next(gen)) # Zobaczymy: Startujemy... -> Pierwszy wynik
print("-" * 20)
print(next(gen)) # Zobaczymy: Wracamy... -> Drugi wynik


def generator_z_licznikiem():
    licznik = 0
    print(f"--- Startujemy. Licznik = {licznik} ---")
    
    while True:
        licznik += 1
        yield f"Wartość licznika: {licznik}"

gen = generator_z_licznikiem()

print(next(gen)) 
print(next(gen)) 
print(next(gen)) 

def cykl_zycia():
    yield "Pierwszy element"
    yield "Drugi element"

gen = cykl_zycia()
print("1. Stworzono generator (ale kod funkcji nie ruszył)")

print(f"2. {next(gen)}") # Start i pierwsza pauza
print(f"3. {next(gen)}") # Wznowienie i druga pauza

try:
    print("4. Próba pobrania trzeciego elementu...")
    next(gen)
except StopIteration:
    print("KONIEC: Generator wyczerpany, cykl życia zakończony.")

# slajd 19
# List comprehension (tworzy całą listę od razu)
lista = [x * 2 for x in range(5)]

# Generator expression (tworzy obiekt "w gotowości")
gen = (x * 2 for x in range(5))

print(lista)  # Wynik: [0, 2, 4, 6, 8]
print(gen)    # Wynik: <generator object <genexpr> at ...>

# Generatora używamy np. w pętli lub funkcją next()
print(next(gen)) # Wynik: 0

#slajd 23 
def generator_id():
    numer = 1
    while True:
        yield f"ID-{numer:04d}"
        numer += 1

# Tworzymy obiekt (nic jeszcze nie zajmuje RAMu)
baza_id = generator_id()

# Możemy pobierać ID w nieskończoność
print(next(baza_id))  # Wynik: ID-0001
print(next(baza_id))  # Wynik: ID-0002

#slajd 24 fibonacci:
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        # obliczamy nową parę jednocześnie
        a, b = b, a + b

# Użycie:
fib = fibonacci()

for _ in range(10):
    print(next(fib), end=" ")
# Wynik: 0 1 1 2 3 5 8 13 21 34

#SLAJD 25:
import itertools

# 1. count() - Automatyczne ID dla procesów
id_generator = itertools.count(start=100, step=10)
print(next(id_generator))  # Wynik: 100
print(next(id_generator))  # Wynik: 110

# 2. cycle() - Przełączanie tur w grze
gracze = ["Gracz 1", "Gracz 2"]
tury = itertools.cycle(gracze)

print(next(tury))  # Wynik: Gracz 1
print(next(tury))  # Wynik: Gracz 2
print(next(tury))  # Wynik: Gracz 1 (zapętlone!)


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# Tradycyjne łączenie (tworzy nową listę w RAM)
nowa_lista = lista_a + lista_b 
# Łączymy wirtualnie
for element in itertools.chain(lista_a, lista_b):
    print(element) # Wypisze: 1, 2, 3, 4, 5, 6

def zuzyty_gen():
    yield 1
    yield 2

gen = zuzyty_gen()

# Pierwsze użycie - wyciągamy wszystkie dane
print(list(gen))  # Wynik: [1, 2]

# Druga próba - generator jest już "pusty"
print(list(gen))  # Wynik: []