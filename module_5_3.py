# Задача "Перегрузка операторов"
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __add__(self, value):
        if isinstance(value, (int, House)):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self + value

    def __eq__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError(False)
        y = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors == y

    def __lt__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError(False)
        y = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors < y

    def __le__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError(False)
        y = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors <= y

    def __gt__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError(False)
        y = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors > y

    def __ge__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError(False)
        y = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors <= y

    def __ne__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError(False)
        y = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors != y

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10    # __add__
print(h1)
print(h1 == h2)  # __eq__2

h1 += 10        # __iadd__
print(h1)

h2 = 10 + h2    # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

