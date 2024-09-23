class Räknare:
    def __init__(self, tal=0):
        self.tal = tal

    def öka(self):
        self.tal += 1

    def minska(self):
        self.tal -= 1

    def skriv_ut_tal(self):
        print(f"Talet är nu {self.tal}.")

# Testa klassen
räknare = Räknare()
räknare.skriv_ut_tal()
räknare.öka()
räknare.skriv_ut_tal()
räknare.minska()
räknare.skriv_ut_tal()
