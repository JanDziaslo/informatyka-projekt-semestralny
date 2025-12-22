import random

with open('liczby.txt', 'w') as f:
    for _ in range(9999):
        liczba = random.randint(-100000, 100000)
        f.write(str(liczba) + '\n')
print("plik z liczbami zostal wygenrowany")

def bobelkowe():
    tablica = []

    with open('liczby.txt', 'r') as f:
        for line in f:
            tablica.append(int(line.strip()))

    n = len(tablica)

    for i in range(n):
        for j in range(0, n - i - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]

    with open('babelkowe.txt', 'w') as f:
        for liczba in tablica:
            f.write(str(liczba) + '\n')

print("sortowanie babelkowe")
bobelkowe()
print("sortowanie babelkowe zakonczylo sie")

