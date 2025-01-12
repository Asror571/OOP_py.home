class Dokon:                          # Dokon nomli class yaratildi 
    def __init__(self,name,manzil,maxsulot,working_time):     # Xusisiyatlari saqlandi 
        self.name  = name
        self.manzil = manzil
        self.maxsulot  = maxsulot
        self.working_time = working_time

    def chop_etish (self):       # NAtijani cho etish uchun metod yozildi 
        if self.maxsulot == 'Elektronika':      # Fqat Elektronika turidagi maxsulot sotadigan dokon malumotalrini chiqarishi uchun 
            return f"Dokon nomi : {self.name } \n Manzili : {self.manzil} \n Maxsulot turi : {self.maxsulot} \n Ish vaqti : {self.working_time} \n"   
         
dokonlar = []     # Dokonlarnbi saqlash uchun list yartildi

user = int(input("Nechta dokon ma'lumotini kiritasiz :"))    #Userdan netchta dokon malumotini kiritishini xo'raldi 


for i in range(user):      # Va loop yordamida ular dokon xususiyatlari olindi 

    name = input("Dokon nomini kiriting :")
    manzil = input("Manzilini kiriting :")
    maxsulot = input("Maxsulot turini kiriting :")
    working_time = input("Ish vaqitini kiritng (08 : 30 dan 19 : 00 )")
    
    dokon = Dokon(name,manzil,maxsulot,working_time)      #  dokonlar nbomli listga saqalandi 
    dokonlar.append(dokon)
  
for dokon in dokonlar:      # Metod call qilindi hamda natija chiqariladi 
    print(dokon.chop_etish())

