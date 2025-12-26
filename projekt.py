import random
import time

def generowanie():
    with open('liczby.txt', 'w') as f:
        for _ in range(9999):
            liczba = random.randint(-100000, 100000)
            f.write(str(liczba) + '\n')

def bobelkowe():
    tablica = []

    with open('liczby.txt', 'r') as f:
        for line in f:
            tablica.append(int(line.strip()))

    n = len(tablica)
    start_time = time.time()

    for i in range(n):
        for j in range(0, n - i - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]

    end_time = time.time()
    czas_wykonania = end_time - start_time


    with open('babelkowe.txt', 'w') as f:
        f.write('zlozonosc obliczeniowa: O(n²)'+ '\n')
        f.write(f'czas wykonywania: {czas_wykonania:.6f} s\n')
        for liczba in tablica:
            f.write(str(liczba) + '\n')

def wstawianie():
    tablica = []

    with open('liczby.txt', 'r') as f:
        for line in f:
            tablica.append(int(line.strip()))

    n = len(tablica)
    start_time = time.time()

    for i in range(1, n):
        pom = tablica[i]
        j = i - 1
        while j >= 0 and tablica[j] > pom:
            tablica[j + 1] = tablica[j]
            j -= 1
        tablica[j + 1] = pom

    end_time = time.time()
    czas_wykonania = end_time - start_time

    with open('wstawianie.txt', 'w') as f:
        f.write('zlozonosc obliczeniowa: O(n²)' + '\n')
        f.write(f'czas wykonywania: {czas_wykonania:.6f} s\n')
        for liczba in tablica:
            f.write(str(liczba) + '\n')

def wybieranie():
    tablica = []

    with open('liczby.txt', 'r') as f:
        for line in f:
            tablica.append(int(line.strip()))

    n = len(tablica)

    start_time = time.time()
    for i in range(n - 1):
        pmin = i

        for j in range(i + 1, n):
            if tablica[j] < tablica[pmin]:
                pmin = j

        tablica[i], tablica[pmin] = tablica[pmin], tablica[i]

    end_time = time.time()
    czas_wykonania = end_time - start_time

    with open('wybieranie.txt', 'w') as f:
        f.write('zlozonosc obliczeniowa: O(n²)' + '\n')
        f.write(f'czas wykonywania: {czas_wykonania:.6f} s\n')
        for liczba in tablica:
            f.write(str(liczba) + '\n')

def szybkie():
    tablica = []

    with open('liczby.txt', 'r') as f:
        for line in f:
            tablica.append(int(line.strip()))

    n = len(tablica)

    def sortowanie(tab, lewy, prawy):
        if lewy >= prawy:
            return

        i = lewy
        j = prawy
        pivot = tab[(lewy + prawy) // 2]

        while i <= j:
            while tab[i] < pivot:
                i += 1
            while tab[j] > pivot:
                j -= 1
            if i <= j:
                tab[i], tab[j] = tab[j], tab[i]
                i += 1
                j -= 1

        if lewy < j:
            sortowanie(tab, lewy, j)
        if i < prawy:
            sortowanie(tab, i, prawy)

    start_time = time.time()

    sortowanie(tablica, 0, n - 1)

    end_time = time.time()
    czas_wykonania = end_time - start_time

    with open('szybkie.txt', 'w') as f:
        f.write('zlozonosc obliczeniowa: O(n log n)' + '\n')
        f.write(f'czas wykonywania: {czas_wykonania:.6f} s\n')
        for liczba in tablica:
            f.write(str(liczba) + '\n')

def kubelkowe():

    tablica = []

    with open('liczby.txt', 'r') as f:
        for line in f:
            tablica.append(int(line.strip()))

    n = len(tablica)

    start_time = time.time()

    mini = min(tablica)
    maxi = max(tablica)

    liczniki = [0] * (maxi - mini + 1)

    for i in range(n):
        liczniki[tablica[i] - mini] += 1

    j = 0

    for i in range(len(liczniki)):
        while liczniki[i] > 0:
            tablica[j] = i + mini
            liczniki[i] -= 1
            j += 1

    end_time = time.time()
    czas_wykonania = end_time - start_time


    with open('kublkowe.txt', 'w') as f:
        f.write('zlozonosc obliczeniowa: O(n²)' + '\n')
        f.write(f'czas wykonywania: {czas_wykonania:.6f} s\n')
        for liczba in tablica:
            f.write(str(liczba) + '\n')

def numerki():
    print("sortowanie babelkowe (1), sortowanie przez wstawianie (2), sortowanie przez wybieranie (3), sortowanie szybkie (4), sortowanie kubelkowe (5), wszytkie sortowania (6), zakoncz program(0)")
    odp = int(input("podaj metode sortowania w postaci liczby: " ))
    return odp

def test(odp):
    if(odp==1):
        print("sortowanie babelkowe"+"\n")
        bobelkowe()
        print("sortowanie babelkowe zakonczylo sie"+"\n")
        test(numerki())
    elif(odp==2):
        print("sortowanie przez wstawianie"+"\n")
        wstawianie()
        print("sortowanie przez wstawianie zakonczylo sie"+"\n")
        test(numerki())
    elif(odp==3):
        print("sortowanie przez wybieranie"+"\n")
        wybieranie()
        print("sortowanie przez wybieranie zakonczylo sie"+"\n")
        test(numerki())
    elif(odp==4):
        print("sortowanie szybkie"+"\n")
        szybkie()
        print("sortowanie szybkie zakonczylo sie"+"\n")
        test(numerki())
    elif(odp==5):
        print("sortowanie kubelkowe"+"\n")
        kubelkowe()
        print("sortowanie kubelkowe zakonczylo sie"+"\n")
        test(numerki())
    elif (odp==6):
        print("sortowanie babelkowe" +"\n")
        bobelkowe()
        print("sortowanie babelkowe zakonczylo sie"+"\n")

        print("sortowanie przez wstawianie"+"\n")
        wstawianie()
        print("sortowanie przez wstawianie zakonczylo sie"+"\n")

        print("sortowanie przez wybieranie")
        wybieranie()
        print("sortowanie przez wybieranie zakonczylo sie"+"\n")

        print("sortowanie szybkie"+"\n")
        szybkie()
        print("sortowanie szybkie zakonczylo sie"+"\n")

        print("sortowanie kubelkowe")
        kubelkowe()
        print("sortowanie kubelkowe zakonczylo sie"+"\n")
        test(numerki())
    elif (odp==0):
        print("koniec sortowania"+"\n")
    else:
        print("nieprawidlowa wartosc"+"\n")
        print ("sprobuj ponownie :)"+"\n")
        test(numerki())

generowanie()
test(numerki())

