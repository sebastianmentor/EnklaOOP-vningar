class Rektangel:
    def __init__(self, längd, bredd):
        self.längd = längd
        self.bredd = bredd

    def beräkna_area(self):
        area = self.längd * self.bredd
        print(f"Arean av rektangeln är {area}.")

# Testa klassen
rektangel1 = Rektangel(5, 3)
rektangel1.beräkna_area()
