total = int(input("введите количество квартир!: "))
floors = int(input("введите количество этажей: "))
apartment = int(input("номер кв вашего друга? "))
p = (total/floors)
if total % floors > 0 or apartment <= 0 or total < apartment:
     print("кол-во квартир не делится на кол-во этажей!")
if total % floors > 0 or apartment >=0 or total > apartment:
     print('error!')
n = apartment // (p) or (p)
print("номер этажа вашего друга", n)