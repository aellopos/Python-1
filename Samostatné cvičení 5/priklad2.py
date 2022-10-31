def totalcena(persons, breakfast=False):
  cenaPerPerson = 850
  if breakfast:
    cenaPerPerson += 125
  return cenaPerPerson * persons

print(totalcena(3))
print(totalcena(3, True))