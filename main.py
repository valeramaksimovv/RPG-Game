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