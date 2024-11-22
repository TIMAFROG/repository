class Character:
    def __init__(self, name, health, attak, defense):
        self.name = name
        self.health = health
        self.attak = attak
        self.defense = defense

    def attack(self, target):
        target.take_damage(self.attak)

    def take_damage(self, damage):
        if damage >= self.health:
            self.health = 0
            print(f'персонаж {self.name} убит')
        else:
            self.health -= (damage - self.defense)


p1 = Character('p1', 1000, 1200, 100)
p2 = Character('p2', 1000, 200, 100)
print(p1.health, p2.health)

p1.attack(p2)
print(p1.health, p2.health)

p2.attack(p1)
print(p1.health, p2.health)

# p2.take_damage(p1.attak)
