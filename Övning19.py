class Tåg:
    def __init__(self, antal_vagnar):
        self.antal_vagnar = antal_vagnar

    def beräkna_passagerare(self):
        passagerare = self.antal_vagnar * 50
        print(f"Tåget kan ta {passagerare} passagerare.")

# Testa klassen
tåg1 = Tåg(10)
tåg1.beräkna_passagerare()
tåg2 = Tåg(5)
tåg2.beräkna_passagerare()
tåg3 = Tåg(0)
tåg3.beräkna_passagerare()
tåg4 = Tåg(20)
tåg4.beräkna_passagerare()
