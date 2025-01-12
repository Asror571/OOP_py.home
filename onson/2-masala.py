class Employee:                     # Employee nomli class yaratildi 
    def __init__(self,name,maosh):      # Va xususiyatlari  aniqlandi 
        self.name = name
        self.maosh = maosh
    
    def sum_maosh(self):              # Yillik maoshni hisoblab beradigan metod yaratildi 
        yillik_maosh = self.maosh*12
        return yillik_maosh

xodim1 = Employee("Asror",15000000)      # object yaratildi 
print(f"{xodim1.name} ning yillik maoshi : {xodim1.sum_maosh()}")     # Natija chiarildi 
