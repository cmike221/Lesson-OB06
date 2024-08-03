import random

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


# # Пример использования класса
# if __name__ == "__main__":
#     hero1 = Hero(name="Герой 1", health=100)
#     hero2 = Hero(name="Герой 2", health=80)
#
#     print(hero1)
#     print(hero2)
#
#     hero1.attack(hero2)
#     print(hero2)
#
#     hero2.attack(hero1)
#     print(hero1)
#
#     print(f"Герой 1 жив? {hero1.is_alive()}")
#     print(f"Герой 2 жив? {hero2.is_alive()}")

class Game:
    def __init__(self, player, computer):
        if not isinstance(player, Hero) or not isinstance(computer, Hero):
            raise ValueError("Both player and computer must be instances of the Hero class.")
        self.player = player
        self.computer = computer

    def start(self):
        """Начинает игру, чередуя ходы игрока и компьютера, пока один из героев не умрет."""
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            print(f"{self.computer}")

            if not self.computer.is_alive():
                print(f"{self.computer.name} погиб! {self.player.name} победил!")
                break

            self.computer.attack(self.player)
            print(f"{self.player}")

            if not self.player.is_alive():
                print(f"{self.player.name} погиб! {self.computer.name} победил!")
                break


# Пример использования класса
if __name__ == "__main__":
    # player_hero = Hero(name="Игрок", health=100)
    # computer_hero = Hero(name="Компьютер", health=100)
    try:
        user_input = int(input("Введите произвольное число от 1 до 100: "))
        if not 1 <= user_input <= 100:
            raise ValueError("Число должно быть в диапазоне от 1 до 100.")
    except ValueError as e:
        print(f"Ошибка: {e}")
        exit(1)

    random.seed(user_input)

    player_health = random.randint(50, 200)
    computer_health = random.randint(50, 200)

    player_hero = Hero(name="Игрок", health=player_health)
    computer_hero = Hero(name="Компьютер", health=computer_health)

    game = Game(player=player_hero, computer=computer_hero)
    game.start()
