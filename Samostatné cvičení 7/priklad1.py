class Balik:
  def doruc(self):
    self.doruceno = True
  def __str__(self):
    if self.doruceno:
      doruceno_text = "Balík byl doručen"
    else:
      doruceno_text = "Balík zatím nebyl doručen."
    return "Balík je na adresu {self.adresa} a váží {self.hmotnost}. {doruceno_text}"
  def __init__(self, adresa, hmotnost):
    self.adresa = adresa
    self.hmotnost = hmotnost
    self.doruceno = False