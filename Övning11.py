import math

class Triangel:
    def __init__(self, sida1, sida2, sida3):
        self.sida1 = sida1
        self.sida2 = sida2
        self.sida3 = sida3

    def beräkna_omkrets(self):
        omkrets = self.sida1 + self.sida2 + self.sida3
        print(f"Omkretsen av triangeln är {omkrets}.")

    def beräkna_area(self):
        # Vi använder Herons formel
        s = 0.5*(self.sida1 + self.sida2 + self.sida3)
        a = s - self.sida1
        b = s - self.sida2
        c = s - self.sida3
        area = math.sqrt(s*a*b*c)
        print(f"Arean av triangeln är {area}")

# Testa klassen
triangel1 = Triangel(3, 4, 5)
triangel1.beräkna_omkrets()
triangel1.beräkna_area()
