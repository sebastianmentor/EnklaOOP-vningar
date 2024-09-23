class Kamera:
    def __init__(self, märke, upplösning):
        self.märke = märke
        self.upplösning = upplösning

    def kamera_info(self):
        print(f"Kameran {self.märke} har en upplösning på {self.upplösning} megapixlar.")

    def knapp(self):
        print(f"Tar en bild!")

# Testa klassen
kamera1 = Kamera("Canon", 24)
kamera1.kamera_info()
