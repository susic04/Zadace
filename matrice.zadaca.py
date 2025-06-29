"""Napisati program koji generira kvadratnu matricu dimenzija 7x7.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na rubovima matrice."""

import random
r = 7
s = 7
matrica=[]

for i in range(r):
  red = []
  for j in range(s):
    unos = random.randint(1, 9)
    red.append(unos)
  matrica.append(red)

for i in range(r):
  for j in range(s):
    print(matrica[i][j], end=" ")
  print()

zbroj = 0 
for i in range (r):
    for j in range (s):
        if i== 0 or i == 6 or j == 0 or j== 6:
            zbroj += matrica[i][j]
print("Zbroj elemenaata na rubovima matrice je: ",zbroj)
