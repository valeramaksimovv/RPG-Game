class Postac:
    def __init__(self, imie, zdrowie, atak, obrona, unik=0.1, trafienie=0.8):
        self.imie = imie
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.atak = atak
        self.obrona = obrona
        self.unik = unik
        self.trafienie = trafienie
        self.ekwipunek = Ekwipunek()
        self.inwentarz = Inwentarz()

    def otrzymaj_obrazenia(self, obrazenia):
        if random.random() < self.unik:
            print(f"{self.imie} unika ataku!")
            return
        zmniejszone = max(obrazenia - self.obrona, 0)
        self.zdrowie -= zmniejszone
        print(f"{self.imie} otrzymal {zmniejszone} obrazen (pozostalo: {self.zdrowie})")

    def czy_zyje(self):
        return self.zdrowie > 0

class Wojownik(Postac):
    def __init__(self, imie):
        super().__init__(imie, zdrowie=120, atak=20, obrona=10, unik=0.05, trafienie=0.85)

    def mocny_cios(self, cel):
        if random.random() > self.trafienie:
            print(f"{self.imie} chybia Mocnym Ciosem!")
            return
        obrazenia = self.atak * random.uniform(1.4, 1.6)
        print(f"{self.imie} uzywa Mocny Cios!")
        cel.otrzymaj_obrazenia(obrazenia)

class Mag(Postac):
    def __init__(self, imie):
        super().__init__(imie, zdrowie=80, atak=10, obrona=5, unik=0.15, trafienie=0.75)
        self.mana = 100
        self.lista_zaklec = []

    def rzuc_zaklecie(self, zaklecie, cel):
        if self.mana < zaklecie.koszt_many:
            print("Za malo many!")
            return
        if random.random() > self.trafienie:
            print(f"{self.imie} chybia zakleciem {zaklecie.nazwa}!")
            self.mana -= zaklecie.koszt_many // 2
            return
        self.mana -= zaklecie.koszt_many
        obrazenia = zaklecie.obrazenia * random.uniform(0.9, 1.2)
        print(f"{self.imie} rzuca zaklecie {zaklecie.nazwa}!")
        cel.otrzymaj_obrazenia(obrazenia)

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
    def __init__(self, postac1, postac2):
        self.postac1 = postac1
        self.postac2 = postac2
        self.czyja_tura = 1

    def rozpocnij(self):
        print("--- START WALKI ---")
        while self.poctac1.czy_zyje() and self.postac2.czy_zyje():
            self.wykonaj_ture()
            self.sprawdz_zwyciezce()
    
    def wykonaj_ture(self):
        if self.czyja_tura == 1:
            print(f"Tura: {self.postac1.imie}")
            if isinstance(self.postac1, Mag) and self.postac1.lista_zaklec:
                self.postac1.rzuc_zaklecie(self.postac1.lista_zaklec[0], self.postac2)
            elif isinstance(self.postac2, Wojownik):
                self.postac1.mocny_cios(self.postac2)
            self.czyja_tura = 2
        else:
            print(f"Tura: {self.postac2.imie}")
            if isinstance(self.postac1, Mag) and self.postac2.lista_zaklec:
                self.postac2.rzuc_zaklecie(self.postac1.lista_zaklec[0], self.postac1)
            elif isinstance(self.postac2, Wojownik):
                self.postac2.mocny_cios(self.postac2)
            self.czyja_tura = 1
    
    def sprawdz_zwyciezce(self):
        if self.postac1.czy_zyje():
            print(f"Zwyciezca: {self.postac1.imei}")
        else:
            print(f"Zwyciezca: {self.postac1.imei}")