#   |   | 0
# ----------
# X | X |   
# ----------
#   |   |
# Felder von 1-9 durchnummerieren


class Spielfeld():
    
    def __init__(self):
        self.brett = [0,0,0,0,0,0,0,0,0]
        self.player1 = ""
        self.player2 = ""
        self.zeichen = ""
        self.ingame = True
    
    def feld():
        print("   |    |   ")
        print("------------")
        print("   |    |   ")
        print("------------")
        print("   |    |   ")

    def symbol(self, zeichen):
        print("")
        if self.zeichen == "X" or "x":
            #self.player1 = "X"
            #self.player2 = "O"
            self.figur = "X"

        elif self.zeichen == "O" or "o" or "0":
            #self.player1 = "O"
            #self.player2 = "X"
            self.figur = "O"
            

    def spielzug(self):
        while self.ingame == True:
            print("")
            if self.figur == "X":
                print("Player", self.figur, "ist an der Reihe!")
                zahl = int(input("Auf welches Feld wollen sie setzen: "))
                self.brett[zahl]
                if self.brett[zahl] != 0:
                    print("\nHier wurde bereits hingesetzt!")
                elif self.brett[zahl] == 0:
                    self.brett[zahl] = self.figur
                    self.figur = "O"
            else:
                print("Player", self.figur, "ist an der Reihe!")
                zahl = int(input("Auf welches Feld wollen sie setzen: "))
                self.brett[zahl]
                if self.brett[zahl] != 0:
                    print("\nHier wurde bereits hingesetzt!")
                elif self.brett[zahl] == 0:
                    self.brett[zahl] = self.figur
                    self.figur = "X"

    def gewinnen(self):
        pass

instanz1 = Spielfeld()

print("########  ###                ########                          ########                      ")
print("  ###            ######        ###     ######     ######         ###     ######     ######   ")
print("  ###     ###    ###           ###     ##  ##     ###            ###     ##  ##     ####     ")
print("  ###     ###    ######        ###     ##### #    ######         ###     ######     ###### \n")

zeichen = str(input("Player 1, geben Sie ein ob sie X oder O nehmen möchten: "))
instanz1.symbol(zeichen)
instanz1.spielzug()