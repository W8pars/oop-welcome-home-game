# this is not fully original code. much of this is based off learning from
# online lessons from www.futurelearn.com, course Object Oriented Programming
# instructors for this class are:
# Chief Learning Officer Sue Sentance, Course Facilitator Martin O'Hanlon,
# Learning Managers Alex Parry, Matt Hogan,

# create item class with getters/setters
class Item():
    def __init__(self, item_name):
        self.item_name = item_name
        self.description = ''
        self._item_description = ''
        self.height = 0
        self.width = 0
        self.weight = 0
        self.location = None
        self.items = []

    def set_name(self, item_name):
        self.item_name = item_name

    def get_item_name(self):
        return self.item_name

    @property
    def item_description(self):
        item_described = self._item_description
        return item_described

    @item_description.setter
    def item_description(self, i_description):
        self._item_description = i_description

#    def set_item_description(self, item_description):
#        self.description = item_description

#    def get_item_description(self):
#        return self.description

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

# furniture class to extend item class
class Furniture(Item):
    def __init__(self, item_name):
        super().__init__(item_name)

# example of furniture class extending further and giving it new self attr and new
# methods to gain understanding of manipulating objects that hold objects
class Bookshelf(Furniture):
    def __init__(self, item_name):
        super().__init__(item_name)
        self.books = 10

    # create number of book setter/getter
    def set_number_of_books(self, number_of_books):
        self.books = number_of_books

    def get_number_of_books(self):
        return self.books

# create take book off shelf method
    def take_book(self, xbooks):
        self.books -= xbooks
        self.get_number_of_books()
        print('There are now ' + str(self.books) + ' books on the shelf.')
        # ? possible to create book object Item class so able to move it around/drop it/put elsewhere?

# create return book to shelf method
    def return_book(self, xbooks):
        self.books += xbooks
        self.get_number_of_books()
        print('There are now ' + str(self.books) + ' books on the shelf.')
