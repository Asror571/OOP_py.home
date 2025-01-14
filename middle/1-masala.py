class school:                           # School nomli class yaratildi 
    def __init__(self,school_name):     # Va unga faqat maktab nomi xusiyati saqlandi 
        self.school_name = school_name   # Maktab nomini saqlaydi 
        self.students = []                # Studentslar ro'yxatini saqlash uchun      
    def add_student(self,student_name):       # Talabalarni qo'shish uchun
        if student_name not in self.students:   # Agar talaba studentlar ro'yxatida  mavjud bo'lsa 
            self.students.append(student_name)
            print(f"{student_name} mofaqiyatli qo'shildi")    # Studentlar ro'yxatiga qo'shildi 
        else :
            print(f"{student_name} bu o'quvchi bor")        # agar bor bo'lsa  o'quvchi bor deb chiqaradi 
    
    def remove_student(self,student_name):      # O'quvchi ma'lumotlarini o'chirish 
        if student_name in self.students:        # Agar talaba talabalar ro'yxatida bor bo'lsa 
            self.students.remove(student_name)    # O'chiriladi 
            print(f"{student_name} muofqiyatli o'chirildi ")
        else:
            print("Bu o'quvchi mavjud emas")    # Aks xolda
    
    def chop_etish(self):           # Talabalarni ro'yxatini chiqarish 
        if self.students:
            for talaba in self.students:    # Loop yordamida chiqarildi 
                print(f"{talaba}")
        else :
            print("Hozircha talabalar yo'q brat")

school = school("Najot Ta'lim")     # Metodlar call qilindi 

school.add_student("Ali")       
school.add_student("Vali")  
school.add_student("Ali")  

school.chop_etish()     

school.remove_student("Ali") 
school.remove_student("Hasan")

school.chop_etish()       



    
        