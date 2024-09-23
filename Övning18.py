class TV:
    def __init__(self, storlek, upplösning):
        self.storlek = storlek
        self.upplösning = upplösning

    def tv_info(self):
        print(f"TV:n är {self.storlek} tum med en upplösning på {self.upplösning}.")

# Testa klassen
tv1 = TV(55, "4K")
tv1.tv_info()
