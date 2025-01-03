class Etudiant:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)

    def calculer_moyenne(self):
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)

etudiant = Etudiant("Ali", 20)
etudiant.ajouter_note(15)
etudiant.ajouter_note(18)
print("Moyenne:", etudiant.calculer_moyenne())
