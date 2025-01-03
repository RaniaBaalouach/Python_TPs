class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur


class Triangle:
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def calculer_surface(self):
        return 0.5 * self.base * self.hauteur

formes = [Rectangle(10, 5), Triangle(10, 5)]

for forme in formes:
    print("Surface:", forme.calculer_surface())
