class Kniha:
  def sleva(self, sleva_v_procentech):
    self.cena *= (1 - sleva_v_procentech/100)
  def __str__(self):
    print(f"Název knihy: {self.nazev}. Počet stran: {self.pocet_stran}. Cena: {self.cena}")
  def __init__(self, nazev, pocet_stran, cena):
    self.nazev = nazev
    self.pocet_stran = pocet_stran
    self.cena = cena

kniha = Kniha("Noc, která mě zabila", 590, 499)
print(kniha)
kniha.sleva(10)
print(kniha)