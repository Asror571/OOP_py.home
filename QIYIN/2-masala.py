class Instrument:    # Class yaratildi 

    def __init__(self, name, narxi, companiy, instrument_type):    # xususiyatlari saqlandi 
        self.name = name
        self.narxi = narxi
        self.companiy = companiy
        self.instrument_type = instrument_type
    
    def chop_etish(self):    # Natijani chiqarish uchun metod 
        if self.instrument_type == 'Klavyatura' and self.narxi > 20000: # AGAr klavyatura turida hamda nari 20000 dan oshgan maxsulotalrini chiqaradi 
            return f"Nomi: {self.name}, Narxi: {self.narxi}, Ishlab chiqarilgan kompaniya: {self.companiy}, Turi: {self.instrument_type}"

# Objectlar yaratildi 

asbob1 = Instrument("Mini_klavyatura", 30000, 'Apple', 'Klavyatura')
asbob2 = Instrument("Mini_klavyaqtura", 11000, 'Apple', 'Kla')

print(asbob1.chop_etish())   # Metodlar call qilindi 
print(asbob2.chop_etish())  
