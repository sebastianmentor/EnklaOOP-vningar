class Kvadrat:
    def __init__(self, sida):
        self.sida = sida

    def beräkna_omkrets(self):
        omkrets = 4 * self.sida
        print(f"Omkretsen av kvadraten är {omkrets}.")

# Testa klassen
kvadrat1 = Kvadrat(6)
kvadrat1.beräkna_omkrets()
