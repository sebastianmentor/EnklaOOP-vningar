class Cykel:
    def __init__(self, typ, färg):
        self.typ = typ
        self.färg = färg

    def cykel_info(self):
        print(f"Cykeln är en {self.typ} i färgen {self.färg}.")

# Testa klassen
cykel1 = Cykel("Mountainbike", "blå")
cykel1.cykel_info()
