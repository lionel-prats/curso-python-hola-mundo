import os
os.system('cls' if os.name == 'nt' else 'clear')
# ref. video 72


class Coordenadas:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # metodo magico equal (para comparar objetos)
    def __eq__(self, otro):
        print("pasando por el metodo magico __eq__")
        return self.lat == otro.lat and self.lon == otro.lon

    # metodo magico not equal (para comparar objetos)
    def __ne__(self, otro):
        print("pasando por el metodo magico __ne__")
        return not (self.lat == otro.lat and self.lon == otro.lon)

    # metodo magico less than (para comparar objetos)
    def __lt__(self, otro):
        print("pasando por el metodo magico __lt__")
        return self.lat + self.lon < otro.lat + otro.lon

    # metodo magico less or equal (para comparar objetos)
    def __le__(self, otro):
        print("pasando por el metodo magico __le__")
        return self.lat + self.lon <= otro.lat + otro.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

print(coords != coords2)
print(coords > coords2)
print(coords >= coords2)
