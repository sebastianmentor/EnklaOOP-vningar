class Dator:
    def __init__(self, processor, ram):
        self.processor = processor
        self.ram = ram

    def dator_info(self):
        print(f"Dator med processor: {self.processor} och RAM: {self.ram} GB")

# Testa klassen
dator1 = Dator("Intel i7", 16)
dator1.dator_info()