from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S24", "+79987654321"))
catalog.append(Smartphone("Apple", "iPhone 15 Pro Max", "+79987657654"))
catalog.append(Smartphone("Xiaomi", "POCO F6 Pro", "+79983475321"))
catalog.append(Smartphone("Honor", "Magic 6 Pro", "+79987654677"))
catalog.append(Smartphone("Huawei", "Pura 70 Ultra", "+79986745356"))

for phone in catalog:
    print(phone)