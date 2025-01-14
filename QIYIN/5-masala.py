class Vaqt:
    def __init__(self, soat, minut, sekund):
        self.saat = soat
        self.minut = minut
        self.sekund = sekund

    def __str__(self):
        return f"{self.saat}:{self.minut}:{self.sekund}"

class Hour(Vaqt):
    def oshir(self):
        self.saat += 5
        if self.saat >= 24:
            self.saat -= 24

class Minut(Vaqt):
    def oshir(self):
        self.minut += 5
        if self.minut >= 60:
            self.minut -= 60
            self.saat += 1
            if self.saat >= 24:
                self.saat -= 24

class Sekund(Vaqt):
    def oshir(self):
        self.sekund += 5
        if self.sekund >= 60:
            self.sekund -= 60
            self.minut += 1
            if self.minut >= 60:
                self.minut -= 60
                self.saat += 1
                if self.saat >= 24:
                    self.saat -= 24

# Dastur ishlatish
vaqt = Vaqt(12, 30, 45)
print(f"Boshqa vaqt: {vaqt}")

hour = Hour(vaqt.saat, vaqt.minut, vaqt.sekund)
hour.oshir()
print(f"Soat oshirilgan vaqt: {hour}")

minut = Minut(vaqt.saat, vaqt.minut, vaqt.sekund)
minut.oshir()
print(f"Minut oshirilgan vaqt: {minut}")

sekund = Sekund(vaqt.saat, vaqt.minut, vaqt.sekund)
sekund.oshir()
print(f"Sekund oshirilgan vaqt: {sekund}")
