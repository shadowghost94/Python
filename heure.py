class Time(object):
    #heure=0
    #minute=0
    #seconde=0

    def __init__(self, heure, minute, seconde):
        self.heure= heure;
        self.minute= minute;
        self.seconde= seconde;

    def affiche_heure(t):
        print(str(t.heure)+":"+str(t.minute)+":"+str(t.seconde) )

instance= Time(9,58,47)

instance.affiche_heure()
