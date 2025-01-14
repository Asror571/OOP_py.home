class Maneger:    # Class yaratildi 

    def __init__(self, name, lavozim,working_time, ish_haqqi):    # xususiyatlari saqlandi 
        self.name = name
        self.lavozim = lavozim
        self.working_time =working_time
        self.ish_haqqi = ish_haqqi
    
    def chop_etish(self):    # Natijani chiqarish uchun metod 
        if self.lavozim == 'Rahbar' and self.working_time >= 40: # AGAr lavozimi rahbar bo'lsa hamda ish vaqti 40 soatda ko'p bo'lsa  
            return f"Xodimni : {self.name}, Lavozim: {self.lavozim}, ISh vaqti :: {self.working_time}, Ish haqqi: {self.ish_haqqi}"

# Objectlar yaratildi 
xodim1 = Maneger("Asror", 'Rahbar', 45 , 123456789000)
xodim2 = Maneger("Suxrobbek", 'Dasturchi', 40, 1234500)
xodim3 = Maneger("Abdurasul", 'Direktor', 20, 12345009090909)


print(xodim1.chop_etish())  
print(xodim2.chop_etish())  
