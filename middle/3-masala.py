class Student:                        # Student nomli class yaratildi 
    def __init__(self, name, age, grades):        # Uni xususiyatlari saqlandi 
        self.name = name
        self.age = age
        self.grades = grades

    def get_average(self):    # O'rtacha bahosini hisoblash uchun metod yaratil;di 
        if len(self.grades) == 0:    # Agar baholar yo'q bo'lsa  0 qaytaradi 
            return 0
        return sum(self.grades) / len(self.grades)    # Aks holda o'rtacha qiymatni qaytaradi 

    def is_passing(self):      # 60 baldan   yuqori   talabalarni chiqarish uchun 
        if self.get_average() > 60:
            return True              # 60 baldan yuqoi bo'lsa True qaytaradi 
        return False

talaba1 = Student("Asror", 16, [56, 78, 80, 90, 89, 78, 12])   # Bitta object yaratildi 
 
print(f"O'rtacha baho: {talaba1.get_average()}")     # NAtijalar chiqarildi 
print(f"{talaba1.is_passing()}")
