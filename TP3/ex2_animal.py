class Animal:
    def parler(self):
        pass


class Oiseau(Animal):
    def parler(self):
        print("Cui-cui!")


class Poisson(Animal):
    def parler(self):
        print("Bloup-bloup!")

oiseau = Oiseau()
poisson = Poisson()
oiseau.parler()
poisson.parler()
