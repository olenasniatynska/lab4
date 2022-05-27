"""An addition to the game
    file with classes
"""

class Room:
    """
    Descriptions of many rooms
    """
    def __init__(self, name):
        self.name = name
        self.l_rooms = []

    def __repr__(self):
        return self.name
    
    def link_room(self,linked_room, direction):
        """
        Containce information about linked room
        """
        self.l_rooms.append((linked_room, direction))

    def set_description(self,description):
        """Contains descriptive information about room"""
        self.description = description

    def set_character(self, character):
        """Containce the name of the character"""
        self.charact = character

    def set_item(self, item_name):
        """
        Containce name of the item
        """
        self.i_name = item_name

    def get_name(self):
        """Returns the name of the room"""
        return self.name

    def get_character(self):
        """Returns the name of the character"""
        return self.charact

    def get_item(self):
        """Returns the name of the item"""
        return self.name

    def get_details(self):
        """Prints the name of the room and description"""
        print(self.name)
        print('')
        print(self.set_description)
        for room in self.l_rooms:
            print(f'The {room[0]} is on the {room[1]}')
        
    def move(self, direc):
        for i in self.l_rooms:
            if i[1] == direc:
                return i[0]
        return "You can't go there"


class Enemy:
    """
    class Enemy
    """
    killed_enemies = 0

    def __init__(self, name, description):
        """
        Accespts infornation about hte class
        """
        self.name = name
        self.desc = description
        self.conversation = None

    def describe(self):
        """Prints wheather eenmy is here"""
        print(f"{self.name} is here !!! Aufpassen")
        print(self.desc)
    
    def set_conversation(self,phrase):
        """Contains the conversations"""
        self.phrase = phrase

    def set_weakness(self, weakness):
        """Contains the information about weakness"""
        self.weak = weakness

    def talk(self):
        """Prints enemy's phrase"""
        if self.phrase == None:
            print("")
        else:
            print()

    def fight(self, item):
        """To make the option fight"""
        if item == self.weak:
            print(f"You killed {self.name}")
            self.killed_enemies += 1
            return True

        else:
            print("Your idea didn't work. Sorry:_(")
            return False

    def get_defeated(self):
        """Returns the number of killed enemies"""
        self.killed_enemies


class Item:
    """Shows the information about Item"""
    def __init__(self, name):
        self.name = name

    def set_description(self, description):
        """Contains the description about item"""
        self.descr = description

    def get_name(self):
        """Returns the name of the item"""
        return self.name

    def describe(self):
        """Prints the information about the location of item"""
        print(f'The [{self.name}] is here - {self.descr}')
