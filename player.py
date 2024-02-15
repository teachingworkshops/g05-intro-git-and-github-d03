from room import Room

class Player:
    def __init__(self, starting_room):
        self.location = starting_room
        self.inventory = []
        self.inventory_disp = []
        self.health = 3
        self.hasKey = False
        self.hasSword = False
        self.hasShield = False

    def display_status(self):
        print(f"Health: {self.health}")
        print(f"Inventory: {self.inventory_disp}")

    def move(self, direction):
        if direction.lower() == "north" and self.location.north:
            self.location = Room.rooms[self.location.north]
            print("You move to the north.")
            self.location.room_check(self)
        elif direction.lower() == "south" and self.location.south:
            self.location = Room.rooms[self.location.south]
            print("You move to the south.")
            self.location.room_check(self)
        elif direction.lower() == "east" and self.location.east:
            self.location = Room.rooms[self.location.east]
            print("You move to the east.")
            self.location.room_check(self)
        elif direction.lower() == "west" and self.location.west:
            self.location = Room.rooms[self.location.west]
            print("You move to the west.")
            self.location.room_check(self)
        else:
            print(f"There is no path to the {direction}.")
