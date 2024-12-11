'''
Stwórz system klas, w którym:

Klasa Produkt zawiera nazwę, cenę i ilość.
Klasa Zamowienie zawiera listę produktów i metodę dodaj_produkt, która pozwala dodać produkt do zamówienia.
Metoda podsumowanie() wyświetla wszystkie produkty w zamówieniu wraz z ich ceną i ilością.


class Produkt:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def __str__(self):
        return f"{self.nazwa}, Cena: {self.cena} zł, Ilość: {self.ilosc}."

class Zamowienie:
    def __init__(self):
        self.produkty = [] #pusta lista "produkty"

    def dodaj_produkt(self, produkt):
        self.produkty.append(produkt) #dodaje produkt do listy produkty

    def podsumowanie(self):
        print("Podsumowanie zamówienia: ")
        for produkt in self.produkty:
            print(produkt)

produkt1 = Produkt("Chleb", 4, 5)
produkt2 = Produkt("Mleko", 3, 6)
produkt3 = Produkt("Masło", 10, 2)

zamowienie = Zamowienie()
zamowienie.dodaj_produkt(produkt1)
zamowienie.dodaj_produkt(produkt2)
zamowienie.dodaj_produkt(produkt3)

zamowienie.podsumowanie()


Rozbuduj klasę Ksiazka:

Dodaj nową klasę Ebook, która dziedziczy po Ksiazka i posiada dodatkowe pole format_pliku oraz metodę pobierz(), która zwraca tekst np. "Pobieranie e-booka...".
Dodaj klasy Audiobook z metodą sluchaj() zwracającą "Słuchanie audiobooka...".

from abc import ABC, abstractmethod

class Media(ABC):
    total_media = 0

    def __init__(self):
        Media.total_media += 1

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @staticmethod
    def total_media_count():
        return f"Total media: {Media.total_media}"

class Ksiazka(Media):
    def __init__(self, tytul, autor, rok_wydania):
        super().__init__()
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def info(self):
        return f"Książka: {self.tytul}, Autor: {self.autor}, Rok wydania: {self.rok_wydania} rok."

    def play(self):
        return "Czytanie książki..."

class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, format_pliku):
        super().__init__(tytul, autor, rok_wydania)
        self.format_pliku = format_pliku

    def info(self):
        podstawowy_opis = super().info()
        return (f"{podstawowy_opis}, Format pliku: {self.format_pliku}.")

    def pobierz(self):
        return "Pobieranie ebooka..."

ebook1 = Ebook("Harry Potter", "J. K. Rowling, 1997", 1997, "PDF")

print(ebook1.info())
print(ebook1.play())

class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, dlugosc_nagrania):
        super().__init__(tytul, autor, rok_wydania)
        self.dlugosc_nagrania = dlugosc_nagrania

    def info(self):
        podstawowy_opis = super().info()
        return f"{podstawowy_opis}, Długość nagrania: {self.dlugosc_nagrania} minut."

    def pobierz(self):
        return "Pobieranie audiobooka..."

audiobook1 = Audiobook("Pan Tadeusz", "Adam Mickiewicz", 1834, 1200)

print(audiobook1.info())
print(audiobook1.pobierz())


class Student:
    def __init__(self, imie, nazwisko, indeks, rok_studiow):
        self.imie = imie
        self.nazwisko = nazwisko
        self.indeks = indeks
        self.rok_studiow = rok_studiow

    def info(self):
        return f"Imię: {self.imie}, Nazwisko: {self.nazwisko}, Numer indeksu: {self.indeks}, Rok studiów: {self.rok_studiow} rok."

class StudentInformatyki(Student):
    def __init__(self, imie, nazwisko, indeks, rok_studiow):
        super().__init__(imie, nazwisko, indeks, rok_studiow)
        self.jezyki_programowania = []

    def dodaj_jezyk(self, jezyk_programowania):
        self.jezyki_programowania.append(jezyk_programowania)
        return {f"Dodano język programowania: {jezyk_programowania}"}

    def info(self):
        podstawowy_opis = super().info()
        return f"{podstawowy_opis}, Języki programowania: {', '.join(self.jezyki_programowania) or 'Brak'}."

class StudentMedycyny(Student):
    def __init__(self, imie, nazwisko, indeks, rok_studiow, specjalizacja):
        super().__init__(imie, nazwisko, indeks, rok_studiow)
        self.specjalizacja = specjalizacja

    def info(self):
        podstawowy_opis = super().info()
        return f"{podstawowy_opis}, Specjalizacja: {self.specjalizacja}."

student1 = Student("Zofia", "Warzycha", 280971, 2)
studentinformatyki1 = StudentInformatyki("Zofia", "Warzycha", 280971, 2)
studentmedycyny1 = StudentMedycyny("Adam", "Nowak", 123456, 1, "Psychiatria")

print(student1.info())
print(studentinformatyki1.info())
print(studentinformatyki1.dodaj_jezyk("Python"))
print(studentinformatyki1.info())
print(studentmedycyny1.info())


from abc import ABC, abstractmethod

class Postac(ABC):
    def __init__(self, imie, poziom, punkty_zdrowia):
        self.imie = imie
        self.poziom = poziom
        self.punkty_zdrowia = punkty_zdrowia
        self.rodzaj_broni = None
        self.rodzaj_zaklecia = None
        self.rodzaj_naboju = None

    @abstractmethod
    def atak(self):
        pass

class Wojownik(Postac):
    def dodaj_bron(self, bron):
        self.rodzaj_broni = bron
        return f"Zdobyto nową broń: {bron}!"
    def atak(self):
        return f"Wojownik {self.imie} atakuje {self.rodzaj_broni}!"

class Mag(Postac):
    def dodaj_zaklecie(self, zaklecie):
        self.rodzaj_zaklecia = zaklecie
        return f"Nauczono się nowego zaklęcia: {zaklecie}!"
    def atak(self):
        return f"Mag rzuca {self.rodzaj_zaklecia or 'zaklęcie'}!"

class Lucznik(Postac):
    def dodaj_naboj(self, naboj):
        self.rodzaj_naboju = naboj
        return f"Nabyto nowy nabój do łuku: {naboj}!"
    def atak(self):
        return f"Łucznik wypuszcza {self.rodzaj_naboju or "strzałę"} z łuku!"

wojownik = Wojownik("Artur", 10, 100)
mag = Mag("Merlin", 12, 80)
lucznik = Lucznik("Legolas", 8, 70)

wojownik.dodaj_bron("miecz")
mag.dodaj_zaklecie("ogniste zaklęcie")
lucznik.dodaj_naboj("strzała z trucizną")

postacie = [wojownik, mag, lucznik]
for postac in postacie:
    print(postac.atak())
'''
