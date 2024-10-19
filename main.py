# module_5_1.py
# 19.10.2024 Задача "Developer - не только разработчик"


class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def go_to(self, new_floor):
        for i in range(1, int(new_floor) + 1):
            if new_floor > int(self.number_of_floors) or new_floor < 1:
                print('Такого этажа не существует')
                break
            else:
                print(i)
        return


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
