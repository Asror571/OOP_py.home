class Student:          # Class yaratildi 
    def __init__(self, ism, kurs, baho, stipendiya):   # uni xususiyatlari saqlandi 
        self.ism = ism
        self.kurs = kurs
        self.baho = baho
        self.stipendiya = stipendiya

    def chop_etish(self):    # Metod yaratildi natijani chop_etish uchun
        return f"Ismi: {self.ism}, Kursi: {self.kurs}, O'rtacha bahosi: {self.baho}, Stipendiyasi: {self.stipendiya} so'm"
    
talaba1 = Student("Asror","Dasturlash",80.4, 00.00)      # Objectalr yani talabalar berildi 
talaba2 = Student("Abdurasul","Dasturlash",100.0, 80.00)
talaba3 = Student("Suxrobbek","Dasturlash",80.7,90.00)
talaba4 = Student("Azizbek","Frontend",85.4,100.00)

talabalar = [talaba1, talaba2, talaba3, talaba4,]   # Barcha talabalar bitta listga saqlandi 

print("Talabalar :")

for talaba in talabalar:     # Va loop yordamida saralanib chiqarildi 
    if talaba.baho > 80 and talaba.stipendiya > 10.00:
        print(talaba.chop_etish())