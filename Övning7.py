class Cirkel:
    def __init__(self, radie):
        self.radie = radie

    def beräkna_omkrets(self):
        omkrets = 2 * 3.14 * self.radie
        print(f"Omkretsen av cirkeln är {omkrets}.")

# Testa klassen
cirkel1 = Cirkel(4)
cirkel1.beräkna_omkrets()

# # Användning av pi från math
# import math
# class Cirkel:
#     def __init__(self, radie):
#         self.radie = radie

#     def beräkna_omkrets(self):
#         omkrets = 2 * math.pi * self.radie
#         print(f"Omkretsen av cirkeln är {omkrets:.1f}.")

# # Testa klassen
# cirkel1 = Cirkel(4)
# cirkel1.beräkna_omkrets()
