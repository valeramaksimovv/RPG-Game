class Postac:
    def __init__ (self, imie, zdrowie, atak, obrona):
        self.imie = imie
        self.zdrowie = zdrowie
        self.atak = atak
        self.oborona = obrona
        self.ekwipunek = Ekwipunek()
        self.inwentarz = Inwentarz()

    def otrzymaj_obrazenia(self, obrazenia):
        zmniejszone = max (obrazenie - self.obrona, 0)
        self.zdrowie -= zmniejszone
        print(f"{self.imie} otrzymuje {zmniejszone} obrazen (pozostalo {self.zdrowie})")

    def czy_zyje(self):
        return self.zdrowie > 0
    
class Wojownik(Postac):
    def __init__(self, imie):
        super().__init__(imie, zdrowie=120, atak=20, obrona=10)

    def mocny_cios(self, cel):
        obrazenia = self.atak * 1.5
        print(f"{self.imie} uzywa Mocny Cios!")
        cel.otrzymaj_obrazenia(obrazenia)

class Mag(Postac):
    def __init__(self, imie):
        super().__init__(imie, zdrowie=80, atak=10, obrona=5)
        self.mana = 100
        self.lista_zaklec = []

    def rzuc_zaklecie(self, zaklecie, cel):
        if self.mana >= zaklecie.koszt_many:
            self.mana -= zaklecie.koszt_many
            print(f"{self.imie} rzuca zaklecie {zaklecie.nazwa}!")

class Zaklecie:
    def __init__(self, nazwa, obrazenia, koszt_many):
        self.nazwa = nazwa
        self.obrazenia = obrazenia
        self.koszt_many = koszt_many

    def opis(self):
        return f"{self.nazwa}: {self.obrazenia} DMG, koszt many: {self.koszt_many}"

class Przedmiot:
    def __init__(self, nazwa, bonus_atak, bonus_zdrowie, bonus_obrona, typ):
        self.nazwa = nazwa
        self.bonus_atak = bonus_atak
        self.bonus_zdrowie = bonus_zdrowie
        self.bonus_obrona = bonus_obrona
        self.typ = typ 

    def wypisz_przedmiot(self):
        return f"{self.nazwa} (+{self.bonus_atak} atak, +{self.bonus_zdrowie} hp, +{self.bonus_obrona} obrona) [{self.typ}]"

class Ekwipunek:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def usun_przedmiot(self, nazwa):
        self.przedmioty = [p for p in self.przedmioty if p.nazwa != nazwa]

    def wypisz_ekwipunek(self):
        for p in self.przedmioty:
            print(p.wypisz_przedmiot())

class Inwentarz:
    def __init__(self):
        self.zalozone = {"bron": None, "zbroja": None}

    def zaloz(self, przedmiot):
        self.zalozone[przedmiot.typ] = przedmiot

    def zdejmij(self, typ):
        self.zalozone[typ] = None

    def opis(self):
        for typ, przedmiot in self.zalozone.items():
            if przedmiot:
                print(f"{typ}: {przedmiot.wypisz_przedmiot()}")
            else:
                print(f"{typ}: brak")

class Walka:
    def __init__(self, postac1, postc2)
        self.postac1 = postac1
        self.postac2 = postac2
        self.czyja_tura = 1

    def 