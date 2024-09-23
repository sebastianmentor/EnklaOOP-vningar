class Person:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

    def hälsning(self):
        print(f"Hej, jag heter {self.namn} och jag är {self.ålder} år gammal.")

# Testa klassen
person1 = Person("Emma", 25)
person1.hälsning()