import random

def generiere_zufaelliges_wort(silben):
    vokale = 'aeiou'
    konsonanten = 'bcdfghjklmnpqrstvwxyz'
    return ''.join(random.choice(konsonanten) + random.choice(vokale) for _ in range(silben))

def generiere_haiku():
    zeile_1 = generiere_zufaelliges_wort(5)
    zeile_2 = generiere_zufaelliges_wort(7)
    zeile_3 = generiere_zufaelliges_wort(5)

    haiku = f"{zeile_1}\n{zeile_2}\n{zeile_3}"
    return haiku

if __name__ == "__main__":
    print("zufällig generiertes Haiku:")
    kreatives_haiku = generiere_haiku()
    print(kreatives_haiku)
