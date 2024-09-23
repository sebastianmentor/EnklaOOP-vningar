class Bil:
    def __init__(self, modell, år):
        self.modell = modell
        self.år = år

    def beskrivning(self):
        print(f"Bilen är en {self.modell} från år {self.år}.")

# Testa klassen
bil1 = Bil("Volvo", 2018)
bil1.beskrivning()
