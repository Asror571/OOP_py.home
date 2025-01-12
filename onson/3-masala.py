class Movie:              # Class yartildi 
    def __init__(self, title, duration, rating):        # Filmni xususiyatlari saqlandi 
        self.title = title
        self.duration = duration
        self.rating = rating

    def increase_duration(self, minutes):     # davomiyligini hisoblash uchun metod yaratildi
        self.duration += minutes  
        if self.duration > 150:       #  agar  davomiyli 150 minutdan katta bo'lsa reytingini 0.5 ga kamaytiradi 
            self.rating -= 0.5
    
    def chop_etish(self):                     #  Kinoni chop etish 
        return f"Film nomi : {self.title} \nDavomiyligi : {self.duration} \nReytingi : {self.rating}\n"
    
kino1 = Movie("Iqror", 130, 9.0)  # Kino yartildi 
kino1.increase_duration(30)    # Metod call qilindi 
print(kino1.chop_etish())     # Metod call qilindi 
