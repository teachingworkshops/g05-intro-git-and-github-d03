import Player.py
class Room:
    def __init__(self, north, east, south, west, enemy, item, description, isDark, isDoor):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.enemy = enemy
        self.item = item
        self.description = description
        self.isDark = isDark
        self.isDoor = isDoor

    def describe(self):
        print(self.description)

    def describeItem(self):
        if (self.item != None):
            print (self.item.description)
    
    def roomCheck (self, player) :
        if (player.location.isDark):
            print ('The room is too dark to see anything.')
        if (player.location.isDoor):
            if (player.hasKey):
                 print("You use the key on the door and escape the dungeon!")
                 exit
            #player.hasKey will be implemented once the Item class is uploaded
        else:
            print("You see a large, locked door at the end of the hall.")
            
            

    