class Bokhylla:
    def __init__(self, antal_hyllor):
        self.antal_hyllor = antal_hyllor

    def beräkna_böcker(self):
        böcker = self.antal_hyllor * 20
        print(f"Bokhyllan kan rymma {böcker} böcker.")

# Testa klassen
bokhylla1 = Bokhylla(5)
bokhylla1.beräkna_böcker()