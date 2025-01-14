from datetime import datetime          #datetime import qilindi 
class Book:                # class yaratildi 
    def __init__(self, name, yozuvchi):   # va xususiyatlari saqlandi 
        self.name = name           
        self.yozuvchi = yozuvchi
        self.qarzdor = None                 # Qarzdor yo'q 
        self.qaytarish_muddati = None      # Qaytarish muddati ham yo'q

    def borrow(self, name, date):      # metod yaratildi 
        if self.qarzdor:               # Agar qarzdor to'g'ri bo'lsa 
            print(f"Kitobni {self.qarzdor}  qarzga olingan.")
        else:
            self.qarzdor = name   # Uni kitob qarz olgnlarga qo'shib qoyamiz
            self.qaytarish_muddati = datetime.strptime(date, '%Y-%m-%d')     # va qatratish_mudatini ham qo'shmiz 
            print(f"{self.name} kitobini {name}  {date} sanasi gacha qarzga olingan")   # Va qachongacha ekanligini chiaraamiz 

    def return_book(self):      # Qaytarish uchun metod yaratildi 
        if not self.qarzdor:      # Agar qarzdor qarzdorlar ro'yxatida yo'q bo'lsa 
            print("Bu kitob qarzga olinmagan")
            return
        
        today = datetime.today()   # Agar bor bo'ladigan bo'lsa 
        if self.qaytarish_muddati and today > self.qaytarish_muddati:  #Qayatrish muddatdan o'tgan bo'lsa 
            print("Jazo qullaniladi!")  # Nataija
        else:
            print("Kitob vaqtida qaytarilgan")
        
        self.qarzdor = None              # Va tozlalaymiz
        self.qaytarish_muddati = None


book = Book("Talim Va Tarbiya", "Isxoqxon Muxmadjon o'g'li")    # objectlar yartildi hamda metodlar call qilindi 

book.borrow("Asror", "2025-01-14")
book.return_book()

book.borrow("Suxrobbek", "2025-01-22")

book.borrow("Sherbek", "2025-01-12")
book.return_book()