#   |   | 0
# ----------
# X | X |   
# ----------
#   |   |
# Felder von 1-9 durchnummerieren
# 8 Gewinn möglichkeiten


class Spielfeld():
    
    def __init__(self):
        self.brett = [0,0,0,0,0,0,0,0,0]
        self.zeichen = ""
        self.ingame = True


    def board(self):
        print ("     ", self.brett[0], "  |  ", self.brett[1], "  |  ", self.brett[2], "\n     ", self.brett[3], "  |  ", self.brett[4], "  |  ", self.brett[5], "\n     ", self.brett[6], "  |  ", self.brett[7], "  |  ", self.brett[8])

class Spielzug(Spielfeld):

    def symbol(self):
        print("")
        wertX = ["x", "X"]
        wertO = ["o", "O", "0"]
        while True: 
            zeichen = str(input("Player 1, geben Sie ein ob sie X oder O nehmen möchten: "))
            if zeichen in wertX:
                self.figur = "X" 
                self.spielzug()
            elif zeichen in wertO:
                self.figur = "O"
                self.spielzug()
            else:
                print("Geben Sie entweder X oder O ein!")

    def spielzug(self):
        while self.ingame == True:
            print("")
            if self.figur == "X":
                print("Player", self.figur, "ist an der Reihe!")
                zahl = int(input("Auf welches Feld wollen sie setzen: "))   #ToDo: Nummerierung von 1-9 statt 0-8
                if zahl < 1 or zahl > 9:
                    print("Wählen Sie bitte eine Zahl zwischen 1-9 aus!")
                    self.board()
                else:
                    zahl = zahl - 1 
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
                if zahl < 0 or zahl > 9:
                    print("Wählen Sie bitte eine Zahl zwischen 1-9 aus!")
                    self.board()
                else:
                    zahl = zahl - 1
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
        
        for i in range(len(self.brett)):
            if self.brett[0] == 'X' and self.brett[4] == 'X' and self.brett[8] == 'X' or self.brett[0] == 'O' and self.brett[4] == 'O' and self.brett[8] == 'O':
                endwert = self.brett[4]
                print("Player", endwert, "hat Gewonnen!")
                break
            elif self.brett[0] == 'X' and self.brett[1] == 'X' and self.brett[2] == 'X' or self.brett[0] == 'O' and self.brett[1] == 'O' and self.brett[2] == 'O':
                endwert = self.brett[1]
                print("Player", endwert, "hat Gewonnen!")
                break
            elif self.brett[3] == 'X' and self.brett[4] == 'X' and self.brett[5] == 'X' or self.brett[3] == 'O' and self.brett[4] == 'O' and self.brett[5] == 'O':
                endwert = self.brett[4]
                print("Player", endwert, "hat Gewonnen!")
                break
            elif self.brett[6] == 'X' and self.brett[7] == 'X' and self.brett[8] == 'X' or self.brett[6] == 'O' and self.brett[7] == 'O' and self.brett[8] == 'O':
                endwert = self.brett[7]
                print("Player", endwert, "hat Gewonnen!")
                break
            elif self.brett[0] == 'X' and self.brett[3] == 'X' and self.brett[6] == 'X' or self.brett[0] == 'O' and self.brett[3] == 'O' and self.brett[6] == 'O':
                endwert = self.brett[3]
                print("Player", endwert, "hat Gewonnen!")
                break
            elif self.brett[1] == 'X' and self.brett[4] == 'X' and self.brett[7] == 'X' or self.brett[1] == 'O' and self.brett[4] == 'O' and self.brett[7] == 'O':
                endwert = self.brett[4]
                print("Player", endwert, "hat Gewonnen!")
                break
            elif self.brett[2] == 'X' and self.brett[5] == 'X' and self.brett[8] == 'X' or self.brett[2] == 'O' and self.brett[5] == 'O' and self.brett[8] == 'O':
                endwert = self.brett[5]
                print("Player", endwert, "hat Gewonnen!")
                break
            elif self.brett[2] == 'X' and self.brett[4] == 'X' and self.brett[6] == 'X' or self.brett[2] == 'O' and self.brett[4] == 'O' and self.brett[6] == 'O':
                endwert = self.brett[4]
                print("Player", endwert, "hat Gewonnen!")
                break
            elif all(y == 'X' or y == 'O' for y in self.brett):
                print("Unentschieden!")
                break
            else:
                self.spielzug()
        self.replay()

    def replay(self):
        
        while True:
            answer = str(input("Wollen Sie erneut spielen (yes/no): "))
            
            yes_answer = ['yes', 'y', 'ja', 'j']
            no_answer = ['no', 'n', 'nein']

            if answer.lower() in yes_answer:
                print("Spiel wird neu gestartet...")
                start()
            elif answer.lower() in no_answer:
                print("Spiel wird beendet...")
                exit()
            else:
                print("Bitte geben Sie ja oder nein ein!")

def start():
   
    instanz1 = Spielzug()

    print("\n########  ###                ########                          ########                      ")
    print("  ###            ######        ###     ######     ######         ###     ######     ######   ")
    print("  ###     ###    ###           ###     ##  ##     ###            ###     ##  ##     ####     ")
    print("  ###     ###    ######        ###     ##### #    ######         ###     ######     ###### \n")

    instanz1.symbol()

if __name__ == "__main__":
    start()
