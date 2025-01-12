class Student:                                         # Student nomli class yaratildi
    def __init__(self,name,surname,course,garde):       # __init__ funksiyasi bilan talabaning xusisiyatlarini aniqlandi yani objectni 
        self.name = name   
        self.suname = surname
        self.course = course
        self.garde = garde
    
    def toliq_name(self):   # Va talabani to'liq ismini chiqrish uchun metod yozildi 
        return(f" Ismi : {self.name} \n Familiyasi : {self.suname} ")
    
talaba1 = Student("Asror","Qurbonazarov","Dasturlash","100")        # object yartildi hamda xususiyatlar saqlandi 
print(talaba1.toliq_name())          # metod call qilindi 
  