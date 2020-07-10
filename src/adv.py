from room import Room
from player import Player
from item import Item
import sys

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


outside = room['outside']
outside.items.append(Item('Sword', 'It\'s a sword.'))
outside.items.append(Item('Shield', 'Goes with your sword.'))
room['overlook'].items.append(Item('Potion', 'Heals you.'))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print('Welcome to the game! Please type in your name.')
player_name = input('>')
player = Player(player_name, room['outside'])
print(f'Welcome, {player.name}! For help, type in help.')

def whereami():
    print('------------------------------------------')
    print(f'You are currently at the {player.location}')
    print('What would you like to do?')

whereami()
player.chk_inv()

while True:

    action = input('>').upper()
    words = action.split(' ')
    if (len(words)) > 1:
        verb = words[0]
        noun = words[1].title()
        if words[0] == 'TAKE':
            # print(player.location.items.name)
            room_search = [x.name for x in player.location.items]
            # player.inventory.append(player.location.items.pop)
            # print(room_search)
            if noun in room_search:
                item_index = room_search.index(noun)
                player.location.items[item_index].on_take()
                player.inventory.append(player.location.items.pop(item_index))

            else:
                print(f'You do not see a single {noun} in the room.')
        elif words[0] == 'DROP':
            inv_search = [x.name for x in player.inventory]
            if noun in inv_search:
                item_index = inv_search.index(noun)
                player.inventory[item_index].on_drop()
                player.location.items.append(player.inventory.pop(item_index))
    else:
        if action == 'HELP':
            print('---HELP: To move, type in the letter of the cardinal direction you want to go in. \nFor example, type n and hit enter to move north, or e for east.\nYou can also type in POS for your position, or i for your inventory.')
        elif action == 'POS':
            whereami()
        elif action == 'I' or action == 'INVENTORY':
            player.chk_inv()
        elif action == 'N':
            if player.location.n_to is not None:
                player.location = player.location.n_to
                whereami()
            else:
                print('You can\'t go there!')
        elif action == 'E':
            if player.location.e_to is not None:
                player.location = player.location.e_to
                whereami()
            else:
                print('You can\'t go there!')
        elif action == 'S':
            if player.location.s_to is not None:
                player.location = player.location.s_to
                whereami()
            else:
                print('You can\'t go there!')
        elif action == 'W':
            if player.location.w_to is not None:
                player.location = player.location.w_to
                whereami()
            else:
                print('You can\'t go there!')
        elif action == 'Q':
            sys.exit()
        else:
            print('I don\'t understand!')

    



