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
