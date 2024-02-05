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
    print(f"Description: {self.location.description}")
    print(f"Health: {self.health}")
    print(f"Inventory: {self.inventory_disp}")

  def move(self, direction):
    if direction.lower() == 'north' and self.location.north:
      self.location = self.location.north
      print("You move to the north.")
      self.location.roomCheck(self.location, self)
    elif direction.lower() == 'south' and self.location.south:
      self.location = self.location.south
      print("You move to the south.")
      self.location.roomCheck(self.location, self)
    elif direction.lower() == 'east' and self.location.east:
      self.location = self.location.east
      print("You move to the east.")
      self.location.roomCheck(self.location, self)
    elif direction.lower() == 'west' and self.location.west:
      self.location = self.location.west
      print("You move to the west.")
      self.location.roomCheck(self.location, self)
    else:
      print(f"There is no path to the {direction}.")
