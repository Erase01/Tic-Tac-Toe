#   |   | 0
# ----------
# X | X |   
# ----------
#   |   |
# Felder von 1-9 durchnummerieren


class Spielfeld():
    
    def __init__(self):
        self.brett = (0,0,0,0,0,0,0,0,0)
        self.player1 = ""
        self.player2 = ""
    
    def feld():
        print("   |    |   ")
        print("------------")
        print("   |    |   ")
        print("------------")
        print("   |    |   ")

    def symbol(self, zeichen):
        print("")
        if self.player1 == "X" or "x":
            self.player2 = "O"
        elif self.player1 == "O" or "o" or "0":
            self.player2 = "X"
            

    def spielzug(self):
        print("")
        zahl = int(input("Auf welches Feld wollen sie setzen: "))
        self.brett[zahl]
        if self.brett[zahl] != 0:
            print("Hier wurde bereits hingesetzt!")
        elif self.brett[zahl] == 0:
            self.brett[zahl] = figur


instanz1 = Spielfeld()

print("########  ###                ########                          ########\n")
print("  ###            ######        ###     ######     ######         ###     ######     ######   \n")
print("  ###     ###    ###           ###     ##  ##     ###            ###     ##  ##     ####     \n")
print("  ###     ###    ######        ###     ##### #    ######         ###     ######     ######   \n")

zeichen = str(input("Player 1, geben Sie ein ob sie X oder O nehmen möchten: "))
instanz1.symbol(zeichen)

