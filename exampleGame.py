# this is not fully original code. much of this is based off learning from
# online lessons from www.futurelearn.com, course Object Oriented Programming
# instructors for this class are:
# Chief Learning Officer Sue Sentance, Course Facilitator Martin O'Hanlon,
# Learning Managers Alex Parry, Matt Hogan,

from room import Room
from items import Item, Furniture, Bookshelf
from character import Character, Pet, Enemy
from rpgInfo import RPGInfo

home_sweet_home = RPGInfo('The Parsons\' Home')
home_sweet_home.welcome()
RPGInfo.info()
RPGInfo.author = "William Parsons"


# make the kitchen
kitchen = Room('kitchen')
kitchen.set_description('a room to prepare and cook food.')
kitchen.set_adjacent_rooms(2)
kitchen.set_numdoors(2)
kitchen.set_number_windows(1)
oven = Furniture('oven')
kitchen.add_item(oven, 'oven')

# make the pantry
pantry = Room('pantry')
pantry.set_description('a food storage and laundry room.')
pantry.set_adjacent_rooms(1)
pantry.set_numdoors(2)
pantry.set_number_windows(1)

# make common areas
liv_room = Room('living room')
liv_room.set_description('the largest common room for entertainment.')
liv_room.set_numdoors(3)
liv_room.set_adjacent_rooms(3)
liv_room.set_number_windows(4)

din_room = Room('dining room')
din_room.set_description('the room where the residents and guests enjoy meals.')
din_room.set_numdoors(3)
din_room.set_adjacent_rooms(3)
din_room.set_number_windows(0)

entry_way = Room('entry way room')
entry_way.set_description('the first room upon entering the house.')
entry_way.set_numdoors(6)
entry_way.set_adjacent_rooms(5)
entry_way.set_number_windows(0)

gym = Room('exercise room')
gym.set_description('a small area with exercise/gym equipment. It connects to the garage.')
gym.set_numdoors(2)
gym.set_adjacent_rooms(2)
gym.set_number_windows(1)

garage = Room('garage')
garage.set_description('a normal garage with a car and carpentry tools inside.')
garage.set_numdoors(2)
garage.set_adjacent_rooms(1)
garage.set_number_windows(1)

# make bedrooms
mbed = Room('master bedroom')
mbed.set_description('the best bedroom in the house. The residents reside here.')
mbed.set_numdoors(2)
mbed.set_adjacent_rooms(2)
mbed.set_number_windows(1)

gbed = Room('guest bedroom')
gbed.set_description('the spare bedroom for guests. It doesn\'t have a bed.')
gbed.set_numdoors(2)
gbed.set_adjacent_rooms(2)
gbed.set_number_windows(1)

# bathrooms
mbath = Room('master bathroom')
mbath.set_description('the residents\' primary bathroom. It is very modern looking.')
mbath.set_numdoors(1)
mbath.set_adjacent_rooms(1)
mbath.set_number_windows(1)

gbath = Room('guest bathroom')
gbath.set_description('the second bathroom connected to the ' + str(gbed.name) + '. Oddly, it has carpets.')
gbath.set_numdoors(1)
gbath.set_adjacent_rooms(1)
gbath.set_number_windows(1)

sbath = Room('spare water closet')
sbath.set_description('a spare watercloset room. It is carpeted for some reason.')
sbath.set_numdoors(1)
sbath.set_adjacent_rooms(1)
sbath.set_number_windows(1)

# link all the rooms to create the map
kitchen.link_room(pantry, 'east')
kitchen.link_room(din_room, 'west')
pantry.link_room(kitchen, 'west')
din_room.link_room(kitchen, 'east')
din_room.link_room(liv_room, 'south')
din_room.link_room(entry_way, 'west')
liv_room.link_room(din_room, 'north')
liv_room.link_room(mbed, 'east')
liv_room.link_room(entry_way, 'west')
entry_way.link_room(din_room, 'east')
entry_way.link_room(gym, 'west')
entry_way.link_room(sbath, 'southeast')
entry_way.link_room(gbed, 'north')
entry_way.link_room(liv_room, 'south-east')
gbed.link_room(entry_way, 'south')
gbed.link_room(gbath, 'east')
gbath.link_room(gbed, 'west')
gym.link_room(entry_way, 'east')
gym.link_room(garage, 'north')
garage.link_room(gym, 'south')
mbed.link_room(liv_room, 'west')
mbed.link_room(mbath, 'north')
mbath.link_room(mbed, 'south')
sbath.link_room(entry_way, 'north')

# create creatures/enemies w. weaknesses /npc's and put them into desired rooms
## added second intruder along with Character class variable that will count instances of enemies

jackson = Pet('Jackson', 'a smelly dog.')
jasmine = Character('Jasmine', 'your sister.')
intruder = Enemy('A home intruder', 'a robber with a gun.')
intruder2 = Enemy('another home intruder', 'a robber with a knife')
intruder.set_weakness('gun')
intruder2.set_weakness('gun')
entry_way.set_character(jackson)
entry_way.set_character(intruder2)
liv_room.set_character(intruder)
liv_room.set_character(jasmine)

# create any items to allow interaction
bookshelf1 = Furniture('Bookshelf')
bookshelf1.item_description = 'a shelf that can hold many books.'
liv_room.add_item(bookshelf1, 'bookshelf')
book1 = Item('book')
book1.item_description = 'a book on programming with Python'
liv_room.add_item(book1, 'brown book')
squirrel = Item('toy squirrel')
squirrel.item_description = 'Jackson\'s favorite toy'
jackson.pick_up_item(squirrel) #testing creating and giving items to char class

# weapon to fight off intruder
gun = Item('gun')
gun.item_description = 'gun'
entry_way.add_item(gun, 'gun')

current_room = entry_way
alive = True
# give player an item bag to collect items, then write code to search the list for "weapons" to fight/play
player_items = {}
RPGInfo.actions()
print('You come home from a long day at work.')
print('As you enter the house, you hear a scream from inside.')
print('There are ' + str(Room.number_of_rooms) + ' rooms in this house.')
print('There are {} enemies remaining in your house'.format(Enemy.enemies_remaining))
while alive:
    print('-' * 20)
    possible_moves = ['north', 'south', 'east', 'west',
                      'south-east', 'south-west', 'north-east', 'north-west']
    current_room.describe_room()
    print('---' * 20)
    command = input('What would you like to do? \n>').lower()
    if command == 'look around':
        current_room.what_is_here()
    elif command == 'fight':
        if len(current_room.characters) > 0:
            for char in current_room.characters:
                if isinstance(char, Enemy):
                    weapon = input('What do you attack with? >').lower()
                    # check if item in player's possession
                    if weapon in player_items:
                        char.fight(weapon)
                        current_room.characters.remove(char)
                        # set endgame condition if all enemies cleared, game ends
                        if Enemy.enemies_remaining == 0:
                            print('You have cleared all intruders from your house!')
                            alive = False
                    else:
                        char.fight(weapon)
                        alive = False
                else:
                    char.fight()
        else:
            print('There is nobody in this room to fight...')
    elif command == 'play':
        if len(current_room.characters) > 0:
            for char in current_room.characters:
                if isinstance(char, Pet):
                    toy = input('What do you want to play with? >').lower()
                    char.play(toy)
                else:
                    char.play()
        else:
            print('There is nobody in this room...')
    elif command == 'talk':   #### next thing to work on, allow to choose to whom to talk to to. also, if none in room, print noone here
        for char in current_room.characters:
            char.talk()
    elif 'go' in command: #changed wording here to sound more natural
        location = input('Where would you like to go? > ').lower()
        if location in possible_moves:  #update this command to say "command = go (direction/location) then move room
            current_room.set_room_visited()
            current_room = current_room.move(location)
    elif 'take' in command:
        item_to_take = input('What do you want to pick up? >').lower()
        if item_to_take in current_room.room_items:
            vesh = current_room.room_items.pop(item_to_take)
            player_items[vesh.item_name] = vesh
            print(vesh.item_name + ' added to your inventory')
        else:
            print('You don\'n see that item here...')
    # elif return : put item back
    # elif drop : drop item in room
    elif command == 'inventory':
        for item in player_items:
            print(item.item_name)
    elif command == 'exit':
        alive = False
    else:
        print('You can\'t do that.')

RPGInfo.credits()
