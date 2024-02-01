#Room Descriptions
from Player import Player
from item import Item
from room import Room
from enemy import Enemy


start_desc = "Damp stone brick walls surround you. Light enters from the gaping hole in the ceiling from which you first fell in. There are doorways splitting to the east, west and south. There must be another way out..."
hall_desc = "Ahead is straight corridor with doorways only to the north and south."
deadend = "You find yourself in an empty dead-end room. Better turn around.."
east_north_turn = "The stone walls curve at a right angle, a doorway to the north and tp the east."
east_south_turn = "The stone walls curve at a right angle, a doorway to the south and to the east."
west_north_turn = "The stone walls curve at a right angle, a doorway to the north and to the west."
north_south_west = "The path splits off into 3 directions, to the north south or west."
north_south_east = "The path splits off into 3 directions, to the north south or east."
null_direction = "You can't go that way, just a wall."

#Item Descriptions
key_desc = "A tarnished brass skeleton key, no doubt for opening a door somewhere.."
discover_key = "A tiny yellow shimmer catches your eye on the floor. You find a brass key and put in it your pocket."
discover_sword = "A rotten goblin lay slayn on the ground with a longsword sticking out from its chest. You remove the blade and carry it with you."
sword_desc = "A shimering steel sword with a golden hilt, it feels heavy in your hands. Must have belonged to some other adventurer. "
discover_shield = "You see a charred human skeleton laying in a pile of soot, a silver shield covering its chest. You pick up the shield in your offhand to take with you, maybe it will serve you beter."
shield_desc = "A shiny silver kite shield strapped to your arm. Don't let those monsters get too close.."
discover_potion = "In a small wooden box you find a vial of red liquid. Just sniffing the concoction makes you buzz with energy. You collect the potion as it may come in handy."
potion_desc = "A rose red potion of what you can only asume gives you more vitality."
discover_torch = "Mounted on the wall is a lit torch illuminating the room. You pick it up off the wall in case you need to explore any dark depths ahead."
torch_desc = "A seeminly normal lit wooden torch, besides the fact that no matter what you do nothing seems to extingish the flames. Strange.."

#Enemy Descriptions
goblin_desc = "A hunched green creature with pointed ears and a rusty dagger ambushes you! Classic Goblin tactics."
goblin_hit = "The goblin swings its dagger at you and makes contact, spilling your blood on the dungeon floor."
goblin_defeat = "You fell the lowly goblin with your attacks, putting it out of its misery."

minotaur_desc = "A tall, half man half bull creature holding a hulking axe blocks your path. The Minotaur lets out a bellow and rushes towards you."
minotaur_hit = "You are unable to avoid the Minotaurs swing, giving you a large gash from the axe blade."
minotaur_defeat = "The minotaur bellows once more and falls to the ground after you deliver a mighty final blow to the beast."

defeat_msg = "You fall to the gorund, bleeding out from your injuries. You simply cannot go on...    GAME OVER!"

sword = Item("Longsword", sword_desc, discover_sword)
shield = Item("Shield", shield_desc, discover_shield)
potion = Item("Potion", potion_desc, discover_potion)
torch = Item("Torch", torch_desc, discover_torch)
key = Item("Key", key_desc, discover_key)

goblin = Enemy("Goblin", goblin_desc, goblin_hit, goblin_defeat)
minotaur = Enemy("Minotaur", minotaur_desc, minotaur_hit, minotaur_defeat)

start_room = Room(None,None,None,None,None,None,start_desc,False)

room_left = Room(None,None,None,start_room,sword,None,deadend,False)
room_up = Room(None,start_room,None,None,None,None,deadend,True)
room_right = Room(None,None,None,start_room,key,None,deadend,False)
room_down =  Room(start_room,None,None,None,None,goblin,deadend,False)

#Major oversight in the method of constructing the map and rooms referencing other rooms, python does not have a compiler
#rl1 = Room(None,None,None,start_room,None,potion,east_south_turn,False)
#rl2 = Room(None,None,None,None,goblin,None,north_south_west,False)
#rl3 = Room(None,None,None,None,None,None,deadend,False)



player= Player(start_room)

def prompt_user(player):
  user_input = input("What will you do?\n")
  match user_input:
      case 'north':
          player.move(player, 'north')
      case 'east':
          player.move(player, 'east')
      case 'south':
          player.move(player, 'south')
      case 'west':
          player.move(player, 'west')
      case 'describe room':
          player.location.describe()
      case "status":
          player.display_status()
      case "help":
          print("You may perform the following actions:\nnorth: move to the room to the north if one exists\neast: move to the room to the east if one exists\nsouth: move to the room to the south if one exists\nwest: move to the room to the west if one exists\ndescribe room: describe the room you are currently in\ndescribe item: describe any item that may exist in the room\nhelp: display this message\n")
      case other:
          print('Invalid action. Try again.')
          prompt_user(player)



def main():
  player.location.describe()
  while True:
    prompt_user(player)

    if player.location.enemy != None:
      player.location.enemy.attack(player)
      player.location.enemy=None
    
    if player.location.item != None:
      player.location.item.discover()
      player.inventory.append(player.location.item)
      player.inventory_disp.append(player.location.item.name)
      match player.location.item.name:
        case "Key":
          player.hasKey=True
        case "Sword":
          player.hasSword=True
      player.location.item = None