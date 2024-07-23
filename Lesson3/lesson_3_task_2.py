from smartphone import Smartphone

smarthon1 = Smartphone("Apple", "15 Pro", "+7903 123 4455")
smarthon2 = Smartphone("Xiaomi", "redmi note 13 pro", "+7916 456 11 22")
smarthon3 = Smartphone("Huawey", "p60 pro", "+7985 999 56 56")
smarthon4 = Smartphone("Vivi", "x10 pro", "+7926 456 89 89")
smarthon5 = Smartphone("Sony", "Xperia", "+7909 111 74 85")


catalog = [smarthon1, smarthon2, smarthon3, smarthon4, smarthon5]

for s in catalog:
    print(s(f"{self.brand} - {self.model}. {self.phone}"))