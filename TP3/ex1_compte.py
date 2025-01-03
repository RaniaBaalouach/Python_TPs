class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def transferer(self, autre_compte, montant):
        if self.solde >= montant:
            self.solde -= montant
            autre_compte.solde += montant
            return True
        return False

compte1 = CompteBancaire("Ali", 1000)
compte2 = CompteBancaire("Sara", 500)

if compte1.transferer(compte2, 200):
    print("Transfert réussi!")
else:
    print("Fonds insuffisants!")
