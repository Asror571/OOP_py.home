class Telefon:                       # Telefon nomli class yaratildi 
    def __init__(self, name, Ram, narxi, company):    # Uni xususiyatlari saqlandi
        self.name = name
        self.Ram = Ram
        self.narxi = narxi
        self.compyany = company
    
    def chop_etish(self):      # Natijani chop etish uchun metod yozildi 
        if 2 <= self.Ram <= 8:          # Faqat Ram 2 dan katta va 8 dan kichiklarni chop etadi 
            return f"Nomi: {self.name} \nRam: {self.Ram} GB \nNarxi: {self.narxi} \nIshlab chiqargan kompaniya: {self.compyany}\n"

telefonlar = []       # Telefonlarni saqlash uchun list yaratildi 

user = int(input("Qancha telefon ma'lumotlarini kiritmoqchisiz? "))

for i in range(user):                              # User nechta Telefon ma'lumotlarni kiritishni xoxlagancha davom etadi
    name = input("Telefon nomini kiriting: ")
    Ram = int(input("Ramni kiriting (GB): ")) 
    narxi = input("Narxini kiriting: ")
    compyany = input("Kompaniyaning nomini kiriting: ")
    

    phone = Telefon(name, Ram, narxi, compyany)
    telefonlar.append(phone)                        # Telefon va uni xusisiyatlari saqlanadi 

for phone in telefonlar:            # Va har bir telefon chop etildi 
    print(phone.chop_etish())  
