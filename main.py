# Room Descriptions
import json
from enemy import Enemy
from item import Item
from player import Player
from room import Room

f = open('descriptions.json')
d = json.load(f) # d is descriptions

sword = Item("Longsword", d["sword_desc"], d["discover_sword"])
shield = Item("Shield", d["shield_desc"], d["discover_shield"])
potion = Item("Potion", d["potion_desc"], d["discover_potion"])
torch = Item("Torch", d["torch_desc"], d["discover_torch"])
key = Item("Key", d["key_desc"], d["discover_key"])

goblin = Enemy("Goblin", d["goblin_desc"], d["goblin_hit"], d["goblin_defeat"])
minotaur = Enemy("Minotaur", d["minotaur_desc"], d["minotaur_hit"], d["minotaur_defeat"])

start_room = Room(None, None, None, None, None, None, d["start_desc"], False)

room_left = Room(None, None, start_room, None, None, sword, d["east_west_hall"], False)
room_up = Room(None, start_room, None, None, None, None, d["north_south_hall"], False)
room_right = Room(None, None, None, start_room, None, None, d["deadend"], False)
room_down = Room(start_room, None, None, None, minotaur, None, d["north_south_hall"], False)

room_left_corner = Room(None, None, room_left, None, None, None, d["east_north_turn"], False)
room_left_north_corridor = Room(None, room_left_corner, None, None, None, None, d["north_south_hall"], False)
room_shield = Room(None, room_left_north_corridor, None, None, None, shield, d["deadend"], False)

room_north_corridor = Room(None, start_room, None, None, None, None, d["north_south_hall"], False)
room_further_north_corridor = Room(None, room_north_corridor, None, None, None, None, d["north_south_hall"], False)
room_north_east_west = Room(None, room_further_north_corridor, None, None, goblin, None, d["north_east_south_west"], False)
room_northest = Room(None, room_north_east_west, None, None, None, None, d["deadend"], False)
room_westest = Room(None, None, room_north_east_west, None, None, None, d["deadend"], False)
room_eastest = Room(None, None, None, room_north_east_west, None, key, d["deadend"], False)

room_door = Room(room_down, None, None, None, goblin, None, d["deadend"], True)

room_left_corner.set_nearby_rooms(room_left_north_corridor, room_left, None, None)
room_left_north_corridor.set_nearby_rooms(room_shield, None, room_left_corner, None)

room_up.set_nearby_rooms(room_north_corridor, None, start_room, None)
room_north_corridor.set_nearby_rooms(room_further_north_corridor, None, room_up, None)
room_further_north_corridor.set_nearby_rooms(room_north_east_west, None, room_north_corridor, None)
room_north_east_west.set_nearby_rooms(room_northest, room_eastest, room_further_north_corridor, room_westest)

room_down.set_nearby_rooms(start_room, None, room_door, None)

sword = Item("Longsword", sword_desc, discover_sword)
shield = Item("Shield", shield_desc, discover_shield)
potion = Item("Potion", potion_desc, discover_potion)
torch = Item("Torch", torch_desc, discover_torch)
key = Item("Key", key_desc, discover_key)

goblin = Enemy("Goblin", goblin_desc, goblin_hit, goblin_defeat)
minotaur = Enemy("Minotaur", minotaur_desc, minotaur_hit, minotaur_defeat)

Room.rooms["start_room"] = Room("room_up", "room_down", "room_right", "room_left", None, None, start_desc, False)
Room.rooms["room_left"] = Room(None, None, "start_room", "room_left_corner", None, sword, east_west_hall, False)
Room.rooms["room_up"] = Room("room_north_corridor", "start_room", None, None, None, None, north_south_hall, False)

Room.rooms["room_right"] = Room(None, None, None, "start_room", None, None, deadend, False)
Room.rooms["room_down"] = Room("start_room", "room_door", None, None, minotaur, None, north_south_hall, False)

Room.rooms["room_left_corner"] = Room("room_left_north_corridor", None, "room_left", None, None, None, east_north_turn, False)
Room.rooms["room_left_north_corridor"] = Room("room_shield", "room_left_corner", None, None, None, None, north_south_hall, False)
Room.rooms["room_shield"] = Room(None, "room_left_north_corridor", None, None, None, shield, deadend, False)

Room.rooms["room_north_corridor"] = Room("room_further_north_corridor", "room_up", None, None, None, None, north_south_hall, False)
Room.rooms["room_further_north_corridor"] = Room("room_north_east_west", "room_north_corridor", None, None, None, None, north_south_hall, False)
Room.rooms["room_north_east_west"] = Room("room_northest", "room_further_north_corridor", "room_eastest", "room_westest", goblin, None, north_east_south_west, False)
Room.rooms["room_northest"] = Room(None, "room_north_east_west", None, None, None, None, deadend, False)
Room.rooms["room_westest"] = Room(None, None, "room_north_east_west", None, None, None, deadend, False)
Room.rooms["room_eastest"] = Room(None, None, None, "room_north_east_west", None, key, deadend, False)

Room.rooms["room_door"] = Room("room_down", None, None, None, goblin, None, deadend, True)

start_room.north = room_up
start_room.south = room_down
start_room.east = room_right
start_room.west = room_left
"""
# Major oversight in the method of constructing the map and rooms referencing other rooms, python does not have a compiler
# rl1 = Room(None,None,None,start_room,None,potion,east_south_turn,False)
# rl2 = Room(None,None,None,None,goblin,None,north_south_west,False)
# rl3 = Room(None,None,None,None,None,None,deadend,False)

player = Player(Room.rooms["start_room"])

def prompt_user(player):
    user_input = input("What will you do?\n")
    print() # new line to make viewing output easier
    match user_input.strip(" ").lower():
        case "north":
            player.move("north")
        case "east":
            player.move("east")
        case "south":
            player.move("south")
        case "west":
            player.move("west")
        case "describe room":
            Room.rooms[player.location].describe()
        case "status":
            player.display_status()
        case "quit":
            print("A hero never quits!!!")
        case "help":
            print( """You may perform the following actions:
north: move to the room to the north if one exists
east: move to the room to the east if one exists
south: move to the room to the south if one exists
west: move to the room to the west if one exists
describe room: describe the room you are currently in
describe item: describe any item that may exist in the room
status: describe current health and inventory
quit: exits the game without victory
help: display this message """)
        case _:
            print("Invalid action. Try again or type 'help'")
            prompt_user(player)


def main():
    player.location.describe()
    while True:
        prompt_user(player)

        if player.location.enemy != None:
            player.location.enemy.attack(player)
            player.location.enemy = None

        if player.location.item != None:
            playerPickedItUp = player.location.item.discover()
            if playerPickedItUp:
                player.inventory.append(player.location.item)
                player.inventory_disp.append(player.location.item.name)
                match player.location.item.name:
                    case "Key":
                        player.hasKey = True
                    case "Sword":
                        player.hasSword = True
                print(f"You picked up the {player.location.item.name}!")
                player.location.item = None
            else:
                print(f"You didn't pick up the {player.location.item.name}.")

if __name__ == "__main__":
    main()
