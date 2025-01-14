class Shopping_carta:      # Class yaratildi 
    def __init__(self):     
        self.products = []   # Maxsulotlarnbi saqlash uchun 

    def add_product(self, name, price):     # Maxsulotlarni9 qo'shish uchun metod 
        for product in self.products:        # Loop yordamida products listidagi maxsulotlarni9 tekshiradi 
            if product["name"] == name:
                print(f"{name} - bu mahsulot allaqachon olingan!") 
                return
        self.products.append({'name': name, 'price': price})     # Agar maxsuylo6t yo'q bo'lsa qo'shadi 

    def remove_product(self, name):           # Maxsulotlarni o'chirish 
        for product in self.products:        # LOop yotrdamida tekshiradi 
            if product["name"] == name:          #Agar topilsa o'chiradi 
                self.products.remove(product)
                print(f"{name} - mahsulot o'chirildi.")
                return
        print(f"{name} - bu mahsulot allaqachon o'chirilgan")  # Topolmasa 

    def get_total(self):         # Maxsulotlarnbi umumiy summasini hisovblash uichun  metod
        total = sum(product["price"] for product in self.products)    # LOOP yordamida list aylantirb sum yordamida qo'shib chiqildi 
        return total

    def show_products(self):      # Maxsulotlarni chiqarish uchun metod yaratildi 
            print("Savatchadagi mahsulotlar:")         # Va savatdagi m,axsulotlar chiqrildi 
            for product in self.products:
                print(f" - {product['name']}: {product['price']} so'm")

carta = Shopping_carta ()   # carta nomli o'zgaruvchiga onlindi 

carta.add_product("Xurmo", 12345.00)      # VA objectlar qo'shil;di 
carta.add_product("Limon", 13.00)
carta.add_product("Banan", 11.00)
carta.add_product("Mandarin", 14.00)

carta.remove_product("Mandarin")

total = carta.get_total()
print(f"Umumiy summa: {total} so'm")

carta.show_products()    # MAxsulotlarni9 chiqarish uchun funksiya call qilindi 
