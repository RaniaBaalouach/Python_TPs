class Vehicule:
    def __init__(self, marque):
        self.marque = marque

    def rouler(self):
        print(f"{self.marque} est en mouvement.")


class Voiture(Vehicule):
    def __init__(self, marque, nombre_de_portes):
        super().__init__(marque)
        self.nombre_de_portes = nombre_de_portes

voiture = Voiture("Toyota", 4)
voiture.rouler()
