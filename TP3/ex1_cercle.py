import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return math.pi * self.rayon ** 2

    def calculer_circonference(self):
        return 2 * math.pi * self.rayon

cercle = Cercle(5)
print("Surface:", cercle.calculer_surface())
print("Circonférence:", cercle.calculer_circonference())
