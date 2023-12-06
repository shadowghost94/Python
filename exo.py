
class Personne(object):

    @property
    def __init__(self, nom, prenom, age, sexe):
        self.nom=nom
        self.prenom= prenom
        self.age= age
        self.sexe= sexe

    def affichage():
        print("je m'appelle {1} {2} j'ai {3} ans et je suis de sexe {}", format(nom, prenom, age, sexe))

Pers1= Personne("SALIFOU", "Ouzéïrou", 21, "M")
Pers1.affichage()
