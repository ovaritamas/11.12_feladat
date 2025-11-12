"""
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza,
ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! 
A program tartalmazza a függvény hívását is!
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def paros_e(szamok):
    for szam in szamok:
        if szam % 2 == 0:
            return True
    return False    

parok = paros_e(lista)