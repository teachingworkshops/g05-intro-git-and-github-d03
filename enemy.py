class Enemy:
    def __init__(self, name, description, health, attack_bonus):
        self.name = name
        self.description = description
        self.health = health
        self.attack_bonus = attack_bonus

#The is_alive method checks if the enemy is still alive
    def is_alive(self):
        return self.health > 0
    
#The take_damage method reduces the enemy's health.
    def take_damage(self, damage):
        self.health -= damage
