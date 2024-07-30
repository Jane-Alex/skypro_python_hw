from address import Address
from mailing import Mailing

to_adress = Address("117519", "Москва", "Чертановская", "5", "25")
from_address = Address("634238", "Краснодар", "Мира", "20", "13")
mailing = Mailing(to_adress, from_address, 1000, "track12345")

print(f"Отправление {mailing.track} из {mailing.from_address} в {mailing.to_address}. Стоимость {mailing.cost} рублей")