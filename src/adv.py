from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print('#######################################')
print('Welcome to the game! Please type in your name.')
player_name = input('>')
player = Player(player_name, room['outside'])
print(f'Welcome, {player.name}! For help, type in help.')


while True:
    print('-------------------------------------')
    print(f'{player.name} is currently at the {player.location}')
    print('What would you like to do?')
    action = input('>')
    if action == 'help':
        print('---HELP: To move, type in the letter of the cardinal direction you want to go in. For example, type n and hit enter to move north, or e for east.')
    elif action == 'n' or 'N':
        if player.location.n_to is not None:
            player.location = player.location.n_to
        else:
            print('You can\'t go there!')
    elif action == 'e' or 'E':
        if player.location.e_to is not None:
            player.location = player.location.e_to
        else:
            print('You can\'t go there!')
    elif action == 's' or 'S':
        if player.location.s_to is not None:
            player.location = player.location.s_to
        else:
            print('You can\'t go there!')
    elif action == 'w' or 'W':
        if player.location.w_to is not None:
            player.location = player.location.w_to
        else:
            print('You can\'t go there!')

    



