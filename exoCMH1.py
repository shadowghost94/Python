class ComptBancaire():
    "classe permettant d'instancier des objets compte bancaire"

    def __init__(self, nom='Dupont', solde=1000):
        self.nom= nom;
        self.solde= solde;

    def depot(self, montant):
        self.solde += montant;
        #print("le compte de {0} contient à cet instant {1} euros".format(self.nom, self.solde) )

    def retrait(self, montant):
        self.solde -= montant;

    def affiche(self):
        print("le solde du compte bancaire de {0} est de {1} euros".format(self.nom, self.solde) )

compte1= ComptBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

compt2= ComptBancaire()
compt2.depot(25)
compt2.affiche()
