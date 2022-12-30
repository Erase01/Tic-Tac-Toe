#   |   | 0
# ----------
# X | X |   
# ----------
#   |   |
# Felder von 1-9 durchnummerieren
# 5 Gewinn möglichkeiten

class Spielfeld():
    
    def __init__(self):
        self.brett = [0,0,0,0,0,0,0,0,0]
        self.player1 = ""
        self.player2 = ""
        self.zeichen = ""
        self.ingame = True
        self.end = True

    
    def feld():
        print("   |    |   ")
        print("------------")
        print("   |    |   ")
        print("------------")
        print("   |    |   ")

    def board(self):
        print ("     ", self.brett[0], "  |  ", self.brett[1], "  |  ", self.brett[2], "\n     ", self.brett[3], "  |  ", self.brett[4], "  |  ", self.brett[5], "\n     ", self.brett[6], "  |  ", self.brett[7], "  |  ", self.brett[8])

class Spielzug(Spielfeld):

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
                    self.board()
                elif self.brett[zahl] == 0:
                    self.brett[zahl] = self.figur
                    self.figur = "O"
                    self.board()
                    self.gewinnen()
            else:
                print("Player", self.figur, "ist an der Reihe!")
                zahl = int(input("Auf welches Feld wollen sie setzen: "))
                self.brett[zahl]
                if self.brett[zahl] != 0:
                    print("\nHier wurde bereits hingesetzt!")
                    self.board()
                elif self.brett[zahl] == 0:
                    self.brett[zahl] = self.figur
                    self.figur = "X"
                    self.board()
                    self.gewinnen()
    
    
    def gewinnen(self):
        #item1 = {0,4,8}

        #indexmap = dict((i, x) for i, x in enumerate(self.brett))
        #print(indexmap)
        #for i in range(len(self.brett)):
        #    if i[0] == 'X' and i[4] == 'X' and i[8] == 'X':
        #        print("Player X hat Gewonnen!")

        if self.brett[0:2] == 'X' or self.brett[0:2] == 'O':
            endwert = self.brett[1]
            print("Player", endwert, "hat Gewonnen!")
            self.replay()
        elif self.brett[3:5] == 'X' or self.brett[3:5] == 'O':
            endwert = self.brett[4]
            print("Player", endwert, "hat Gewonnen!")
            self.replay()
        elif self.brett[6:8] == 'X' or self.brett[6:8] == 'O':
            endwert = self.brett[7]
            print("Player", endwert, "hat Gewonnen!")
            self.replay()
        elif self.brett[0] == 'X' or self.brett[0] == 'O':      # ToDo: überprüfung bearbeiten (for Schleife for i in range(len(brett)))
            if self.brett[4] == 'X' or self.brett[4] == 'O':
                if self.brett[8] == 'X' or self.brett[8] == 'O':
                    endwert = self.brett[4]
                    print("Player", endwert, "hat Gewonnen!")
                    self.replay()
        elif self.brett[2] == 'X' or self.brett[2] == 'O':
            if self.brett[4] == 'X' or self.brett[4] == 'O':
                if self.brett[6] == 'X' or self.brett[6] == 'O':
                    endwert = self.brett[4]
                    print("Player", endwert, "hat Gewonnen!")
                    self.replay()
        elif self.brett[:] == 'X' or 'O':              #ToDo: Unentschieden bearbeiten
            print("Unentschieden!")
            self.replay()
        else:
            self.spielzug()

    def replay(self):
        answer = str(input("Wollen Sie erneut spielen(yes/no)"))
        if answer == 'yes' or 'ja' or 'y' or 'j':
            print("Spiel wird neu gestartet...")                    #does not work so far
            self.ingame = False
        elif answer == 'no' or 'n' or 'nein':
            print("Spiel wird beendet...")
            exit()


instanz1 = Spielzug()
while instanz1.end == True:


    print("########  ###                ########                          ########                      ")
    print("  ###            ######        ###     ######     ######         ###     ######     ######   ")
    print("  ###     ###    ###           ###     ##  ##     ###            ###     ##  ##     ####     ")
    print("  ###     ###    ######        ###     ##### #    ######         ###     ######     ###### \n")

    zeichen = str(input("Player 1, geben Sie ein ob sie X oder O nehmen möchten: "))
    instanz1.symbol(zeichen)
    instanz1.spielzug()
