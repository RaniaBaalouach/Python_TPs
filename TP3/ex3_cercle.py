import math

class Cercle:
    def __init__(self, rayon):
        self.__rayon = rayon

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter
    def rayon(self, valeur):
        if valeur > 0:
            self.__rayon = valeur
        else:
            print("Le rayon doit être positif!")

    def calculer_surface(self):
        return math.pi * self.__rayon ** 2

cercle = Cercle(5)
print("Rayon:", cercle.rayon)
cercle.rayon = 10
print("Nouvelle surface:", cercle.calculer_surface())
