class Bok:
    def __init__(self, titel, författare):
        self.titel = titel
        self.författare = författare

    def beskrivning(self):
        print(f"Boken '{self.titel}' är skriven av {self.författare}.")

    def ändra_titel(self, ny_titel):
        self.titel = ny_titel

    def skriv_ut_författare(self):
        print(f"Författaren till denna bok är {self.författare}.")

# Testa klassen med de nya metoderna
bok4 = Bok("Moby Dick", "Herman Melville")
bok4.beskrivning()
bok4.ändra_titel("Moby-Dick: The Whale")
bok4.beskrivning()
bok4.skriv_ut_författare()
