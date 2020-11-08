# this is not fully original code. much of this is based off learning from
# online lessons from www.futurelearn.com, course Object Oriented Programming
# instructors for this class are:
# Chief Learning Officer Sue Sentance, Course Facilitator Martin O'Hanlon,
# Learning Managers Alex Parry, Matt Hogan,
from items import Item, Furniture, Bookshelf


class Room:

    number_of_rooms = 0


    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.doors = 0
        self.rooms = 0
        self.linked_rooms = {}
        self.windows = 0
        self.visited = False
        self.room_items = {}
        self.characters = []
        Room.number_of_rooms += 1 # increments number of class instance for each room made


    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

# an idea from classmate Peter Morgan, used later to display if room has been visited
    def set_room_visited(self):
        self.visited = True

    def set_number_windows(self, numwindows):
        self.windows = numwindows

    def get_numwindows(self):
        return self.windows

    def set_numdoors(self, num_of_doors):
        self.doors = num_of_doors

    def get_numdoors(self):
        return self.doors

    def set_adjacent_rooms(self, adj_rooms):
        self.rooms = adj_rooms

    def get_adjacent_rooms(self):
        return self.rooms

    def get_room_name(self):
        return self.name

# add/remove item to a room
    def add_item(self, item, key):
        self.room_items[key] = item

    def remove_item(self, item_key):
        self.items.pop(item_key)

    def set_character(self, character_name):
        self.characters.append(character_name)

    def remove_character(self, character_name):
        self.characters.remove(character_name)

    def get_characters(self):
        for char in self.characters:
            print(char.name + ', ' + char.description, end='\n')

    def what_is_here(self):
        if len(self.room_items) > 0:
            print('In this room you see a/an: \n', end='')
            for item in self.room_items:
                print(item, end='\n')
        else:
            print('You don\'t see anything of interest here.')
        if len(self.characters) > 0:
            print('You see :')
            self.get_characters()
        else:
            print('You don\'t see anyone in this room.')

# increment using i to enumerate number of connected rooms. just makes it look nicer.
    def get_details(self):
        i = 1
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(str(i) + '.' + 'The ' + room.get_room_name() + ' is to the ' + direction + '.')
            i += 1
# use this method on the room object to get a full description. calls get_details (which calls what_is_here method)

    def describe_room(self):
        print('You are in the ' + self.name + '.')
        if self.visited:
            print('You have been in this room already.')
        else:
            print('You have not been in this room before.')
        print('-' * 30)
        if self.rooms == 0:
            print('There are ' + str(self.doors) + ' doors' ' connecting to '
                  + 'no further rooms.')
        else:
            print('There is/are ' + str(self.doors) + ' door(s)' + ' leading to '
                  + str(self.rooms) + ' different room(s).')
            print('This room has ' + str(self.windows) + ' window(s).\n')
            self.get_details()

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
#        use line below during creation to visually see if worked, remove during production
#        #print(self.name + ' linked rooms :' + repr(self.linked_rooms))

# navigate through the house
    def move(self, direction):
        if direction in self.linked_rooms:
            self.get_description()
            return self.linked_rooms[direction]
        else:
            print('You can\'t go that way')
            return self
