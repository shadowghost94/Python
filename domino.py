class Domino:
    def __init__(self,x,y):
        self.face_A= x;
        self.face_B= y;

    def affiche_points(self):
        print( "face A: {0}     face B: {1}".format( self.face_A, self.face_B) )

    def valeur(self):
        return self.face_A+self.face_B;

d1= Domino(5, 3)
d1.affiche_points()

d2= Domino(7, 9)
d2.affiche_points()
