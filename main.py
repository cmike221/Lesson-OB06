class Hero:
    def __init__(self, name, health, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Атакует другого героя, отнимая здоровье в размере своей силы удара."""
        if not isinstance(other, Hero):
            raise ValueError("Target must be an instance of the Hero class.")
        if self.is_alive():
            other.health -= self.attack_power
            print(f"{self.name} атакует {other.name}, нанося {self.attack_power} урона.")
        else:
            print(f"{self.name} не может атаковать, потому что он мёртв.")

    def is_alive(self):
        """Возвращает True, если здоровье героя больше 0, иначе False."""
        return self.health > 0

    def __str__(self):
        """Возвращает строковое представление героя."""
        return f"Герой {self.name}: Здоровье = {self.health}, Сила удара = {self.attack_power}"


# Пример использования класса
if __name__ == "__main__":
    hero1 = Hero(name="Герой 1", health=100)
    hero2 = Hero(name="Герой 2", health=80)

    print(hero1)
    print(hero2)

    hero1.attack(hero2)
    print(hero2)

    hero2.attack(hero1)
    print(hero1)

    print(f"Герой 1 жив? {hero1.is_alive()}")
    print(f"Герой 2 жив? {hero2.is_alive()}")
