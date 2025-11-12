"""
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, 
hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def harommal_oszthatok(szamok):
    harommal_oszthatok_listaja = 0
    for szam in szamok:
        if szam % 3 == 0:
            harommal_oszthatok_listaja = harommal_oszthatok_listaja + 1

    return harommal_oszthatok_listaja

harmasok = harommal_oszthatok(lista)

print(harommal_oszthatok(lista))

