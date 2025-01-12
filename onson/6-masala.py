class Avtomobile:           # Avtomobile   nomli class yaratildi 
    def __init__(self, marka, model, ishlab_chiqarilgan, narxi):       # Va uni xuxusiyatlari saqlandi 
        self.marka = marka
        self.model = model
        self.ishlab_chiqarilgan = ishlab_chiqarilgan
        self.narxi = narxi

    def chop_etish(self):       # Natijani chop etish uchun metod yaratildi 
        if self.ishlab_chiqarilgan > 2010:
            return f"Mashina markasi : {self.marka} \nMashina modeli : {self.model} \nIshlab chiqarilgan yili : {self.ishlab_chiqarilgan} \nNarxi : {self.narxi} \n"


def enter_metod(avtomobillar):     # Userdan ma'lumotlarni olish uchun metod yaratildi 
    print("Avtomobile malumotlarini kiritng :")
    while True:                                                  
        marka = input("Avtomobile markasini kiriting :")
        if marka.lower() == 'stop':                           # Qachonki user stop kiritganchha davom etadi 
            break
        model = input("Mashinani modelini kiriting :")
        
        while True: 
            try:
                ishlab_chiqarilgan = int(input("Ishlab chiqarilgan yilini kiritng :"))    # Agar son notog'ri berilgan bo'lsa 
                break  
            except ValueError:
                print("Iltimos, yilni raqam sifatida kiriting.")      
        
        while True:
            try:
                narxi = float(input("Mashinani narxini kiritng :"))     # Gar to'g'ri narx berilmatgan bo'lsa 
                break  
            except ValueError:
                print("Iltimos, narxni to'g'ri kiriting.") 

        moshina = Avtomobile(marka, model, ishlab_chiqarilgan, narxi)  
        avtomobillar.append(moshina)         # listga append qiladi 
 

avtomobillar = [] 
enter_metod(avtomobillar)    # metod call qilindi 

for moshina in avtomobillar:     # va natijalar chiqarildi 
    print(moshina.chop_etish())
