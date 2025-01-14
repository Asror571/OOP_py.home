class Talaba:                                  # Class yaratildi 
    def __init__(self, ism, baho, grant_turi, stipendiya):      # Xususiyatlari qo'shildi 
        self.ism = ism       
        self.baho = baho
        self.grant_turi = grant_turi    # Gart yoki kantrak ekanligini saqlash uchun 
        self.stipendiya = stipendiya
    
    def get_enter(self):      # Talabalarni ma'lumotlarini saqlash uchun 
        return f"Ismi: {self.ism}, O'rtacha bahosi: {self.baho}, O'qish turi: {self.grant_turi}, Stipendiya: {self.stipendiya} "
    
    def chop_etish(self):       # Natijani chop etish buchun ,metod yozildi 
        if self.grant_turi.lower() == "grant" and self.baho > 85:      # Gardea talabaning o'qish turi grant bo'lsa hamda o'tracha bahosi 85 dan ziyot bo'lsa    
            return f"{self.ism}ning stipendiyasi: {self.stipendiya}"
        return None


talabalar = []       # talabalarni saqlshy uchun list yaratiledi 
print("5 ta talabaning ma'lumotlarini kiriting:")    # Faqat beshta talabaning ma'lumoti8ni oladi 

for i in range(5):           # For loop- yordamida ma'lujmotlar olindi 
    ism = input(f"{i+1}-talabaning ismini kiriting: ")
    baho = float(input(f"{ism}ning o'rtacha bahosini kiriting: "))
    grant_turi = input(f"{ism} grantda yoki kontraktda o'qiydi : ").lower()
    stipendiya = int(input(f"{ism}ning stipendiyasi miqdorini kiriting : "))

    talabalar.append(Talaba(ism, baho, grant_turi, stipendiya))   # Hamda listga joylandi
    print()

print("Stipendiya oladigan talabalar:")     
for talaba in talabalar:         # Loop aylanganda ham metod tekshiradui ham natijani chiqaradi 
    natija = talaba.chop_etish()
    if natija:
        print(natija)
