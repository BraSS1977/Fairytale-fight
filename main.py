from abc import ABC, abstractmethod

# Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self, fighter):
        pass

# Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self, fighter):
        damage = 10
        return f"Боец {fighter.name} бьет мечом, нанося {damage} урона!", damage

class Bow(Weapon):
    def attack(self, fighter):
        damage = 5
        return f"Боец {fighter.name} стреляет из лука, нанося {damage} урона!", damage

# Класс Fighter
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        """Изменяет текущее оружие бойца на новое."""
        self.weapon = new_weapon
        print(f"{self.name} сменил оружие на {new_weapon.__class__.__name__}.")

    def attack(self, monster):
        attack_result, damage = self.weapon.attack(self)
        print(attack_result)
        monster.take_damage(damage)

# Класс Monster
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона! Осталось здоровья: {self.health}")
        return self.health


# Пример использования:
sword1 = Sword()
bow1 = Bow()
fighter = Fighter("Иван", sword1)
monster = Monster("Кощей", 50)

fighter.attack(monster)
fighter.change_weapon(bow1)
fighter.attack(monster)