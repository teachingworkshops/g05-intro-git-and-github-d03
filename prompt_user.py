def prompt_user(player):
        input = input("What will you do?\n")
        match input:
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
            case 'describe item':
                player.location.item.describe()
            case "take item" :
                player.location.take()
            case "help":
                print("You may perform the following actions:\nnorth: move to the room to the north if one exists\neast: move to the room to the east if one exists\nsouth: move to the room to the south if one exists\nwest: move to the room to the west if one exists\ndescribe room: describe the room you are currently in\ndescribe item: describe any item that may exist in the room\ntake item: add the item in the room to your inventory\nhelp: display this message\n")
            case other:
                print('Invalid action. Try again.')
                promptUser()

    

def main():
    player.location = STARTROOM
    while True:
        STARTROOM.describe()
        promptUser()