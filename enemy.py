class Enemy:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def attack(self, player):
        while player.health > 0:
            player_roll = random.randint(1, 6)
            enemy_roll = random.randint(1, 6)

            player_attack_bonus = 2 if player.has_sword else 0
            enemy_attack_bonus = -2 if player.has_shield else 0

            player_total = player_roll + player_attack_bonus
            enemy_total = enemy_roll + enemy_attack_bonus

            if player_total > enemy_total:
                print(f"Player defeats the {self.name}!")
                break
            elif player_total < enemy_total:
                print(f"{self.name} wins! Player takes 1 damage.")
                player.health -= 1
            else:
                print("It's a tie! Rerolling...")

        if player.health <= 0:
            print("Player's HP reached 0. Game over.")
            exit()
