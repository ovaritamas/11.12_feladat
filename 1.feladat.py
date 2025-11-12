"""
    Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja
    és az összegükkel tér vissza! 
    A program tartalmazza a függvény hívását is!
"""

szamok_listaja__ = [1, 2, 3, 4, 5, 6]

def osszegzo(szamok_listaja):
    osszeg = 0
    for szam in szamok_listaja:
        osszeg = osszeg + szam
    
    return osszeg
    
sum_uf_num = osszegzo(szamok_listaja__)
