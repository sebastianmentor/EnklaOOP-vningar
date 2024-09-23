class Fjärrkontroll:
    def __init__(self, antal_knappar):
        self.antal_knappar = antal_knappar

    def fjärrkontroll_info(self):
        print(f"Fjärrkontrollen har {self.antal_knappar} knappar.")

    def start_knapp(self):
        print(f"Starta tv:n!")

# Testa klassen
fjärrkontroll1 = Fjärrkontroll(30)
fjärrkontroll1.fjärrkontroll_info()
