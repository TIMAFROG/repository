# class Animal:
#     def __init__(self):
#         pass
#
#     def speak(self):
#         pass
#
#
# class Bird(Animal):
#     def fly(self):
#         pass
#
#
# class Lion(Animal):
#     def growl(self):
#         pass
#
#
# class Monkey(Animal):
#     pass

class Player:
    def __init__(self, name, pos, count_g):
        self.name = name
        self.pos = pos
        self.count_g = count_g

    def zabit_gol(self):
        self.count_g += 1


a = Player('Tima', 3, 2)
print(a.count_g)
a.zabit_gol()
print(a.count_g)
print()
b = Player('Tima', 3, 10)
print(b.count_g)
b.zabit_gol()
print(b.count_g)
