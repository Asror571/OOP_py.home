class Restarand:                   # Resyrand nomli class yaratilildi yani ota class
    def __init__(self, name):      # Va xusisiyatlari saqlandi 
        self.name = name

    def show_info(self):       # Chiroyli chiqisi uchun metod 
        print(f"{self.name} GA XUSH KELIBSIZ!".upper())

class FastFood(Restarand):       # Voris ya'ni o'g'il yoki qiz class yaratildi 
    def __init__(self, name):
        super().__init__(name)   
        self.menu = {                # menyu kiritldi 
            "Burger": 5.99,
            "Fries": 2.49,
            "Soda": 1.49,
            "Hot Dog": 12.4
        }

    def show_menu(self):      # VA menyu chiqarildi 
        print(f"Fast Food Menu  {self.name}:\n")
        for food, narx in self.menu.items():      # Loop yordamida key va valeu ko'rinishida chiqarildi 
            print(f"{food}: ${narx:}")    

class FineDining(Restarand):     # Yana bitta voris class yartildi 
    def __init__(self, name):
        super().__init__(name)
        self.menu = {               # Menyu saqlandi 
            "Lag'mon": 25.99,
            "Osh": 35.99,
            "Shashlik": 15.99
        }

    def show_menu(self):    # Menyu chqarildi 
        print(f"Milliy taomlar menyusi {self.name}:\n")
        for food, narx in self.menu.items():
            print(f"{food}: ${narx:.2f}")

# Va ma'lumotlar berildi  va metodlar call qilindi 

fast_food_restaurant = FastFood("Yema Zarar")
fast_food_restaurant.show_info()
fast_food_restaurant.show_menu()

print("\n")

fine_dining_restaurant = FineDining("Uzbekimni Milliy Taomlari")
fine_dining_restaurant.show_info()
fine_dining_restaurant.show_menu()
