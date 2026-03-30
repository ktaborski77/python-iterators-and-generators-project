def tylko_parzyste(liczby):
    for n in liczby:
        if n % 2 ==0:
            yield n *10

liczby = [1,2,3,4,5,6]

gen = tylko_parzyste(liczby)

print(list(gen))