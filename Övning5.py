class Hund:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

    def skäll(self):
        print(f"{self.namn} säger: voff!")

# Testa klassen
hund1 = Hund("Fido", 3)
hund1.skäll()
