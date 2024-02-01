import random


class Enemy:

  def __init__(self, name, description, hit, defeat):
    self.name = name
    self.description = description
    self.defeat = defeat
    self.hit = hit

  import random

  def attack(self, player):
    print(self.description)
    while player.health > 0:
      player_roll = random.randint(1, 6)
      enemy_roll = random.randint(1, 6)

      player_attack_bonus = 2 if player.hasSword else 0
      enemy_attack_bonus = -2 if player.hasShield else 0

      player_total = player_roll + player_attack_bonus
      enemy_total = enemy_roll + enemy_attack_bonus

      if player_total > enemy_total:
        print(self.defeat)
        break
      elif player_total < enemy_total:
        print(self.hit)
        player.health -= 1

    if player.health <= 0:
      print(
          "You fall to the gorund, bleeding out from your injuries. You simply cannot go on...    GAME OVER!"
      )
      exit()
