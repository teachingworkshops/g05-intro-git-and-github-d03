import Player


class Room:

  def __init__(self, north, south, east, west, enemy, item, description,
               isDoor):
    self.north = north
    self.east = east
    self.south = south
    self.west = west
    self.enemy = enemy
    self.item = item
    self.description = description
    self.isDoor = isDoor

  def describe(self):
    print(self.description)

  def roomCheck(self, player):
    if (player.location.isDoor):
      if (player.hasKey):
        print("You use the key on the door and escape the dungeon!")
        exit
      #player.hasKey will be implemented once the Item class is uploaded
      else:
        print("You see a large, locked door at the end of the hall.")
    else:
      self.describe()
