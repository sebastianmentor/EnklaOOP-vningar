class Mobiltelefon:
    def __init__(self, märke, modell):
        self.märke = märke
        self.modell = modell

    def telefon_info(self):
        print(f"Telefon: {self.märke} {self.modell}")

    def ring(self, telefonnummer):
        print(f"Ringer upp {telefonnummer}! Ringring")
# Testa klassen
telefon1 = Mobiltelefon("Apple", "iPhone 12")
telefon1.telefon_info()