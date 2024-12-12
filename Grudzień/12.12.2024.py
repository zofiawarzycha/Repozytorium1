'''
Program oblicza średnią arytmetyczną ciągu liczb rzeczywistych wprowadzonych przez użytkownika,
ale ignoruje liczby ujemne. Wprowadzanie kończy się przez wpisanie end.
Jeśli użytkownik nie poda żadnej liczby dodatniej, wyświetl odpowiedni komunikat.

def srednia_arytmetyczna_bez_ujemnych():
    liczby_dodatnie = []
    while True:
        wejscie = input("Podaj liczbę rzeczywistą (lub 'end', aby zakończyć): ")
        if wejscie.lower().strip() == 'end':
            break
        try:
            liczba = float(wejscie)
            if liczba >= 0:
                liczby_dodatnie.append(liczba)
            else:
                print("Ignoruję liczbę ujemną (do średniej wliczam tylko dodatnie).")
        except ValueError:
            print("Nieprawidłowa wartość. Wprowadź liczbę rzeczywistą.")
    if len(liczby_dodatnie) > 0:
        srednia = sum(liczby_dodatnie) / len(liczby_dodatnie)
        print(F"Średnia arytmetyczna liczb dodatnich wynosi {srednia}.")
    else:
        print("Nie podano żadnej liczby dodatniej.")

srednia_arytmetyczna_bez_ujemnych()


Użytkownik podaje zakres od a do b oraz dwie liczby: k1 i k2.
Program wypisuje wszystkie liczby z tego zakresu, które są podzielne zarówno przez k1, jak i k2.

def liczby_od_a_do_b_podzielne_przez_k1_i_k2():
    while True:
        try:
            a = int(input("Podaj liczbę 'a' (dolna granica zakresu): "))
            b = int(input("Podaj liczbę 'b' (górna granica zakresu): "))
            if a >= b:
                print(f"Liczba a = {a} musi być większa lub równa liczbie b = {b}.")
                continue
            break
        except ValueError:
            print("Nieprawidłowa wartość. Podaj liczby całkowite.")

    while True:
        try:
            k1 = int(input("Podaj pierwszy dzielnik 'k1': "))
            k2 = int(input("Podaj drugi dzielnik 'k2': "))
            if k1 == 0 or k2 ==0:
                print("Żadnen z dzielników nie może być równy zero.")
                continue
            break
        except ValueError:
            print("Nieprawidłowa wartość. Podaj liczby całkowite.")

    print(f"Liczby z zakresu <{a}, {b}> podzielne zarówno przez {k1} jak i {k2} to:")
    for liczba in range(a, b + 1):
        if liczba % k1 == 0 and liczba % k2 == 0:
            print(liczba)

liczby_od_a_do_b_podzielne_przez_k1_i_k2()
'''
