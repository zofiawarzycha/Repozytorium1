'''
class Produkt: #klasa bazowa
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def opis(self): #metoda opis
        return f"Produkt: {self.nazwa}, Cena: {self.cena} zł, Ilość: {self.ilosc}"

class Elektronika(Produkt): #klasa pochodna
    def __init__(self, nazwa, cena, ilosc, gwarancja):
        super().__init__(nazwa, cena, ilosc) #wywołanie konstruktora klasy bazowej
        self.gwarancja = gwarancja

    def opis(self): #nadpis metody opis (wywołanie jej z klasy bazowej)
        podstawowy_opis = super().opis()
        return f"{podstawowy_opis}, Gwarancja: {self.gwarancja} msc."

produkt1 = Produkt("Jabłka", 3, 100)
elektronika1 = Elektronika("Laptop", 3000, 10, 24)

print(produkt1.opis())
print(elektronika1.opis())


class Ksiazka:
    liczba_ksiazek = 0

    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        Ksiazka.liczba_ksiazek += 1

    def opis(self):
        return f"Książka: {self.tytul}, Autor: {self.autor}, Rok wydania: {self.rok_wydania} rok."

    @staticmethod #używany do definiowania metod, które nie są związane z żadnym konkretnym obiektem (instancją) klasy
    def ilosc_ksiazek():
        return f"Liczba książek: {Ksiazka.liczba_ksiazek}"

ksiazka1 = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", 1834)
ksiazka2 = Ksiazka("Lalka", "Bolesław Prus", 1890)

print(ksiazka1.opis())
print(ksiazka2.opis())
print(Ksiazka.ilosc_ksiazek())


from abc import ABC, abstractmethod

class Zwierze(ABC): #klasa abstrakcyjna
    @abstractmethod #zapowiada metodę bez implementacji
    def dzwiek(self):
        pass #bo brak implementacji

class Pies(Zwierze):
    def dzwiek(self):
        return "Hau hau!"

class Kot(Zwierze):
    def dzwiek(self):
        return "Miau!"

pies = Pies()
kot = Kot()

print(pies.dzwiek())
print(kot.dzwiek())


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

class Film(Media):
    def __init__(self, tytul, rezyser, rok_premiery):
        super().__init__()
        self.tytul = tytul
        self.rezyser = rezyser
        self.rok_premiery = rok_premiery

    def info(self):
        return f"Film: {self.tytul}, Reżyser: {self.rezyser}, Rok premiery: {self.rok_premiery} rok."

    def play(self):
        return "Oglądanie filmu..."

class Album(Media):
    def __init__(self, tytul, artysta, rok_wydania):
        super().__init__()
        self.tytul = tytul
        self.artysta = artysta
        self.rok_wydania = rok_wydania

    def info(self):
        return f"Album: {self.tytul}, Artysta: {self.artysta}, Rok wydania: {self.rok_wydania} rok."

    def play(self):
        return "Odtwrzanie muzyki..."

ksiazka1 = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", 1834)
film1 = Film("Incepcja", "Christopher Nolan", 2010)
album1 = Album("Abbey Road", "The Beatels", 1969)

print(ksiazka1.info())
print(ksiazka1.play())
print(film1.info())
print(film1.play())
print(album1.info())
print(album1.play())
print(Media.total_media_count())


Stwórz hierarchię klas, która obejmie:

Klasę abstrakcyjną Zwierze z metodą abstrakcyjną jedz() oraz zwykłą metodą spij(), która zwraca "Zwierzę śpi".
Klasy pochodne, takie jak Pies, Kot, Krowa, z implementacją metody jedz() odpowiednią dla każdego zwierzęcia.

from abc import ABC, abstractmethod

class Zwierze(ABC):
    @abstractmethod
    def jedz(self):
        pass
    def spij(self):
        return "Zwierzę śpi"

class Pies(Zwierze):
    def __init__(self, jedzenie):
        super().__init__()
        self.jedzenie = jedzenie
    def jedz(self):
        return f"Pies je {self.jedzenie}."

class Kot(Zwierze):
    def __init__(self, jedzenie):
        super().__init__()
        self.jedzenie = jedzenie
    def jedz(self):
        return f"Kot je {self.jedzenie}."

class Krowa(Zwierze):
    def __init__(self, jedzenie):
        super().__init__()
        self.jedzenie = jedzenie
    def jedz(self):
        return f"Krowa je {self.jedzenie}."

pies1 = Pies("kość")
kot1 = Kot("mysz")
krowa1 = Krowa("trawa")

print(pies1.jedz())
print(pies1.spij())
print(kot1.jedz())
print(kot1.spij())
print(krowa1.jedz())
print(krowa1.spij())
'''



