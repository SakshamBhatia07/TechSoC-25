import random


class Pokemon:
    def __init__(self, name, HP, attack, defense, speed, moves):
        self.moves = moves
        self.name = name
        self.HP = HP
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def display_stats(self):
        print(
            f"{self.name} - HP: {self.HP}/100, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}\nMoves: {self.moves[0][0]} ({self.moves[0][1]}), {self.moves[1][0]} ({self.moves[1][1]}), {self.moves[2][0]} ({self.moves[2][1]}), {self.moves[3][0]} ({self.moves[3][1]})\n")


Pikachu = Pokemon("Pikachu", 700, 55, 40, 90,
                  [("Thunder Shock", 40), ("Quick Attack", 30), ("Agility", 0), ("Thunder", 70)])
Pikachu.display_stats()
Charmander = Pokemon("Charmander", 1000, 70, 30, 60,
                     [("Ember", 80), ("Scratch", 40), ("Growl", 0), ("Flamethrower", 100)])
Charmander.display_stats()
print("The Battle Starts Now!!\n\nYour pokemon is Pikachu")


def attack(Pokemon1, Pokemon2, i):
    a = random.randint(1, 10)
    if a == 1:
        Pokemon2.HP -= round((Pokemon1.attack * Pokemon1.moves[i - 1][1] * 2) / Pokemon2.defense, 0)
        print(
            f"\n{Pokemon1.name} used {Pokemon1.moves[i - 1][0]} and it was a critical hit\nDamege: {(round(Pokemon1.attack * Pokemon1.moves[i - 1][1] * 2) / Pokemon2.defense, 0)}")
    else:
        Pokemon2.HP -= round((Pokemon1.attack * Pokemon1.moves[i - 1][1]) / Pokemon2.defense, 0)
        print(
            f"\n{Pokemon1.name} used {Pokemon1.moves[i - 1][0]}\nDamage: {round((Pokemon1.attack * Pokemon1.moves[i - 1][1]) / Pokemon2.defense, 0)}")
    if Pokemon2.HP <= 0:
        print(f"{Pokemon2.name} fainted\n")
    else:
        print(f"{Pokemon2.name} has {Pokemon2.HP} HP left\n")


if Charmander.speed > Pikachu.speed:
    b = random.randint(0, 3)
    attack(Charmander, Pikachu, b)
    if Pikachu.HP <= 0:
        print("You lost")

while True:
    i = int(input("Enter your attack number 1 to 4: "))
    attack(Pikachu, Charmander, i)
    if Charmander.HP <= 0:
        print("You won")
        break
    b = random.randint(0, 3)
    attack(Charmander, Pikachu, b)
    if Pikachu.HP <= 0:
        print("You lost")
        break

    print(f"Pikachu has {round(Pikachu.HP, 0)} HP left\nCharmander has {round(Charmander.HP, 0)} HP left\n")
