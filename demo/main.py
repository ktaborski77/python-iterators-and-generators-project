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