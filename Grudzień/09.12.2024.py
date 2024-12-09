'''
class Samochod:

    def __init__(self, marka, model, rok, pojemnosc_baku):
        self.marka = marka
        self.model = model
        self.rok = rok
        self.pojemnosc_baku = pojemnosc_baku

    def opis(self):
        return f"{self.marka} {self.model} {self.rok}"

moj_samochod = Samochod("Toyota", "Corolla", (2020))
print(moj_samochod.opis())

class Osoba:
    def __init__(self, imie, wiek, miasto):
        self.imie = imie
        self.wiek = wiek
        self.miasto = miasto

    def przedstaw_sie(self):
        return f"Nazywam się {self.imie}, mam {self.wiek} lat i mieszkam w {self.miasto}"

osoba1 = Osoba("Anna", 30, "Kraków")
print(osoba1.przedstaw_sie())

class KontoBankowe:
    def __init__(self, wlasciciel, saldo = 0):
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplata(self, kwota):
        self.saldo += kwota
        return f"Wpłacono {kwota} zł. Nowe saldo: {self.saldo} zł."

    def wyplata(self, kwota):
        if kwota > self.saldo:
            return "Brak wystarczających środków na koncie."
        self.saldo -= kwota
        return f"Wypłacono {kwota} zł. Nowe saldo: {self.saldo} zł."

    def pokaz_saldo(self):
        return f"Saldo konta: {self.saldo} zł"

konto1 = KontoBankowe("Jan Kowalski", 1000)

print(konto1.pokaz_saldo())
print(konto1.wplata(500))
print(konto1.wyplata(200))
print(konto1.pokaz_saldo())
'''
