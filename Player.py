class Player:
    def __init__(self, name, starting_location=(0, 0), max_inventory_slots=5, max_health=100):
        self.name = name
        self.location = starting_location
        self.inventory = []
        self.max_inventory_slots = max_inventory_slots
        self.health = max_health

    def display_status(self):
        print(f"{self.name}'s Status:")
        print(f"Location: {self.location}")
        print(f"Health: {self.health}")
        print(f"Inventory: {self.inventory}")

    def move(self, direction):
        x, y = self.location
        if direction.lower() == 'up':
            self.location = (x, y + 1)
        elif direction.lower() == 'down':
            self.location = (x, y - 1)
        elif direction.lower() == 'left':
            self.location = (x - 1, y)
        elif direction.lower() == 'right':
            self.location = (x + 1, y)
        else:
            print("Invalid direction. Use 'up', 'down', 'left', or 'right'.")

    def pick_up_item(self, item):
        if len(self.inventory) < self.max_inventory_slots:
            self.inventory.append(item)
            print(f"{self.name} picked up {item}.")
        else:
            print(f"{self.name}'s inventory is full. Cannot pick up {item}.")
