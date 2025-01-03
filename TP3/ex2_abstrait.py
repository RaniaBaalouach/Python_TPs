from abc import ABC, abstractmethod

class Employe(ABC):
    @abstractmethod
    def calculer_salaire(self):
        pass


class EmployeHoraire(Employe):
    def __init__(self, heures, taux):
        self.heures = heures
        self.taux = taux

    def calculer_salaire(self):
        return self.heures * self.taux


class EmployeMensuel(Employe):
    def __init__(self, salaire):
        self.salaire = salaire

    def calculer_salaire(self):
        return self.salaire

employes = [EmployeHoraire(40, 15), EmployeMensuel(3000)]
for emp in employes:
    print("Salaire:", emp.calculer_salaire())
