# this is not fully original code. much of this is based off learning from
# online lessons from www.futurelearn.com, course Object Oriented Programming
# instructors for this class are:
# Chief Learning Officer Sue Sentance, Course Facilitator Martin O'Hanlon,
# Learning Managers Alex Parry, Matt Hogan

# import these to allow Character class to use move/take/interact methods

from items import Item, Furniture, Bookshelf
from room import Room
# import these to allow Character class to use move/take/interact methods


class Character():

    # create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.opendialogue = ''
        self.char_items = []

    # describe the character
    def describe(self):
        print(self.name + ' is here!')
        print(self.name + ' is ' + self.description)

    def get_char_name(self):
        return self.name

    def get_char_description(self):
        return self.description

    # set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_char_type(self, ctype):
        self.char_type = ctype

    def get_char_type(self):
        return self.char_type

    # talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[ " + self.name + " says ]: " + self.conversation)
        else:
            print(self.name + ' doesn\'t want to talk.')

    # play with this character
    def play(self):
        print(self.name + ' doesn\'t want to play with you.')
        return True

    # fight the character
    def fight(self):
        print(self.name + ' doesn\'t want to fight with you.')
        return True

    def pick_up_item(self, item):
        self.char_items.append(item)

# specifically one item *maybe iterate thru the list and then add to room for dropped loot?
    def drop_item(self, item):
        self.char_items.remove(item)

    def get_items_carried(self):
        for item in self.char_items:
            print(item.get_item_name())

# a few examples of extending char class and updating att/methods
class Enemy(Character):

    enemies_remaining = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy.enemies_remaining +=1

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print('You fend ' + self.name
                  + ' off with ' + combat_item)
            Enemy.enemies_remaining -= 1
            return True
        else:
            print(self.name + ' attacks you, takes your wallet, and leaves. Bad choice.')
            return False

    def play(self):
        print('What is wrong with you? Do I look like I want to PLAY with you??')

class Pet(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def play(self, toy):
        print('You play fetch with '
              + self.name + ' by throwing the ' + toy + '.')
