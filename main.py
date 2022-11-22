#   |   | 0
# ----------
# X | X |   
# ----------
#   |   |
# Felder von 1-9 durchnummerieren


class Spielfeld():
    
    def __init__(self):
        self.brett = (0,0,0,0,0,0,0,0,0)
    
    def feld():
        print("   |    |   ")
        print("------------")
        print("   |    |   ")
        print("------------")
        print("   |    |   ")

    def symbol():
        pass   

    def spielzug(self):
        print("")
        zahl = int(input("Auf welches Feld wollen sie setzen: "))
        self.brett[zahl]
        if self.brett[zahl] != 0:
            print("Hier wurde bereits hingesetzt!")
        elif self.brett[zahl] == 0:
            self.brett[zahl] = figur




