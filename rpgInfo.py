# this is not fully original code. much of this is based off learning from
# online lessons from www.futurelearn.com, course Object Oriented Programming
# instructors for this class are:
# Chief Learning Officer Sue Sentance, Course Facilitator Martin O'Hanlon,
# Learning Managers Alex Parry, Matt Hogan,
#
class RPGInfo():

    author = "Anonymous"

    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print('Welcome to ' + self.title)

    @staticmethod
    def info():
        print('Made using OOP Python Programing')

    @staticmethod
    def actions():
        print(f""" 
             Action list:
             look around: inspect room and its contents
             go : move in direction
             fight : fight with character
             talk : talk with character
             play : play with character
             take : take an item from room
             return : put item back
             drop : drop item in room
             inventory : check player inventory
             exit : exit game
             """)

    @classmethod
    def credits(cls):
        print('Thank you for playing')
        print('Created by ' + cls.author)

