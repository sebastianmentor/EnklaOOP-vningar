class Bok:
    def __init__(self, titel, författare):
        self.titel = titel
        self.författare = författare

    def beskrivning(self):
        print(f"Boken '{self.titel}' är skriven av {self.författare}.")

# Testa klassen
bok1 = Bok("1984", "George Orwell")
bok1.beskrivning()
