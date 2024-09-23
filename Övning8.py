class Student:
    def __init__(self, namn, kurs, poäng):
        self.namn = namn
        self.kurs = kurs
        self.poäng = poäng

    def beskrivning(self):
        print(f"Student: {self.namn}, Kurs: {self.kurs}, Poäng: {self.poäng}")

    def uppdatera_poäng(self, nya_poäng):
        self.poäng = nya_poäng

# Testa klassen
student1 = Student("Maria", "Matematik", 90)
student1.beskrivning()
student1.uppdatera_poäng(95)
student1.beskrivning()
