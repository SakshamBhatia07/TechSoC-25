import random
l_pokemons=["pikachu","charmander"]
l_disabilities=["Burn","Paralyse"]
def Paralyse(x):
  pass

class Pokemon:
  def __init__(self,name,HP,attack,defense,speed,moves):
    self.moves=moves
    self.name=name
    self.HP=HP
    self.attack=attack
    self.defense=defense
    self.speed=speed
  def display_stats(self):
    print(f"{self.name} - HP: {self.HP}/100, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}\nMoves: {self.moves[0][0]} ({self.moves[0][1]}), {self.moves[1][0]} ({self.moves[1][1]}), {self.moves[2][0]} ({self.moves[2][1]}), {self.moves[3][0]} ({self.moves[3][1]})\n")
pikachu = Pokemon("Pikachu", 140, 55, 40, 90, [("Thunder Shock", 40), ("Quick Attack", 30), ("Agility", 0), ("Thunder", 70)])
pikachu.display_stats()
charmander = Pokemon("Charmander", 120, 70, 30, 60, [("Ember", 80), ("Scratch", 40), ("Growl", 0), ("Flamethrower", 100)])
charmander.display_stats()
print("Your pokemon is pikachu")
while True:
  i=int(input("Enter your attck number 1 to 4: "))
  charmander.HP-=pikachu.moves[i-1][1]
  if charmander.HP<=0:
    charmander.HP=0
  print(f"\nPikachu used {pikachu.moves[i-1][0]}\nDamage: {pikachu.moves[i-1][1]}\nCharmander's health lowers to {charmander.HP}\n")
  if charmander.HP<=0:
    print("Charmander fainted, you won")
    break
  a=random.randint(0,3)
  pikachu.HP-=charmander.moves[a][1]
  if pikachu.HP<=0:
    pikachu.HP=0
  print(f"Charmander used {charmander.moves[a][0]}\nDamage: {charmander.moves[a][1]}\nPikachu's health lowers to {pikachu.HP}\n")
  if pikachu.HP<=0:
    print("Pikachu fainted, you lost")
    break

