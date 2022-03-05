"""
TODO: Define the Creature class, as described on page 10 of the assignment
description. You are allowed to change the scaffold somewhat to better suit
the needs of your program (change function parameters, etc.)

You are allowed to create as many methods as you feel are necessary.
"""
from item import Item

class Creature:
    def __init__(self,name,description,terror_rating,location,direction):
        self.name = name
        self.description = description
        self.terror_rating = int(terror_rating)
        self.location = location
        self.direction = direction
        self.inv = []
        self.current_location = location
        self.attempt_to_catch = 2
        self.attempt_to_take = True
    def take(self, item):
        self.inv.append(item)
        self.current_location.item.remove(item)
    def get_terror_rating(self):
        terror_rating_appearence = self.terror_rating
        for x in self.inv:
            terror_rating_appearence += x.terror_rating
        return terror_rating_appearence
    def get_accessiable_direction(self,initialed_direction):
        direction_list_dict = {"northwest":self.current_location.northwest,\
                                "north":self.current_location.north,\
                                "northeast":self.current_location.northeast,\
                                "west":self.current_location.west,\
                                "east":self.current_location.east,\
                                "southwest":self.current_location.southwest,\
                                "south":self.current_location.south,\
                                "southeast":self.current_location.southeast}
        direction_list = ["northwest","north","northeast","west","east","southwest","south","southeast"]
        accessiable_direction = None
        for x in direction_list:    #initialed_direction will be the direction attribute the creature instance has.
            if x == initialed_direction.lower():
                i = direction_list.index(x)
        start = i
        while i < 8 + start:    #let the creature pick direction clockwisely(set by the direction_list).
            if direction_list_dict[direction_list[(i % 8)-1]] != " ":
                accessiable_direction = direction_list_dict[direction_list[(i % 8)-1]]
                break
            i += 1
        return accessiable_direction
    def take_turn(self,player):
        if self.current_location == player.current_location:
            print("")   #first scenario: the chaser meet player in one room.
            print("{} is trying to catch you!".format(self.name))
            if player.get_terror_rating() > self.get_terror_rating():
                if self.attempt_to_catch == 2:
                    print("But your presence still terrifies them...")
                    self.attempt_to_catch -= 1
            else:
                print("Oh no, you've been caught!")
                print("========= GAME OVER =========")
                quit()
        #second block of code for second scenario: creature can reach to player one turn away.
        elif self.current_location.northwest != " " and self.current_location.northwest == player.current_location:
            self.current_location = player.current_location
            print("{} has arrived at {}.".format(self.name,self.current_location.name))
        elif self.current_location.north != " " and self.current_location.north == player.current_location:
            self.current_location = player.current_location
            print("{} has arrived at {}.".format(self.name,self.current_location.name))
        elif self.current_location.northeast != " " and self.current_location.northeast == player.current_location:
            self.current_location = player.current_location
            print("{} has arrived at {}.".format(self.name,self.current_location.name))
        elif player.current_location.west != " " and self.current_location.west == player.current_location:
            self.current_location = player.current_location
            print("{} has arrived at {}.".format(self.name,self.current_location.name))
        elif player.current_location.east != " " and self.current_location.east == player.current_location:
            self.current_location = player.current_location
            print("{} has arrived at {}.".format(self.name,self.current_location.name))
        elif player.current_location.southwest != " " and self.current_location.southwest == player.current_location:
            self.current_location = player.current_location
            print("{} has arrived at {}.".format(self.name,self.current_location.name))
        elif player.current_location.south != " " and self.current_location.south == player.current_location:
            self.current_location = player.current_location
            print("{} has arrived at {}.".format(self.name,self.current_location.name))
        elif player.current_location.southeast != " " and self.current_location.southeast == player.current_location:
            self.current_location = player.current_location
            print("{} has arrived at {}.".format(self.name,self.current_location.name))
        #third part for third scenario: the chaser is either not stay in the player room or can reach 
            #player one turn away.
        else:
            if self.current_location.item != [] and self.attempt_to_take == True:
                self.take(self.current_location.item[0])   #attempt_to_take allow creature instance only take one item in one location
                self.attempt_to_take = False            
            else:
                accessiable_direction = self.get_accessiable_direction(self.direction)
                if accessiable_direction != None:   #get_accessiable_direction return a goable adjacent location instance 
                    self.current_location = accessiable_direction
class player:
    def __init__(self):
        self.terror_rating = 5
        self.inv = []
        self.current_location = None
    def get_terror_rating(self):
        terror_rating_appearence = self.terror_rating
        for x in self.inv:
            terror_rating_appearence += x.terror_rating
        return terror_rating_appearence
    def get_inv(self):
        burner = []
        for x in self.inv:
            burner.append(x.item_name)
        return burner
    def drop(self, item):
        burner = False
        i = 0
        while i < len(self.inv):
            if item == self.inv[i].short_name:
                stuff_being_taken = self.inv[i]
                burner = True
            i += 1
        if burner:   #burner is the counter to check 
                        #whether player actually has the item
            print("You drop the {}.".format(stuff_being_taken.item_name))
            for x in self.inv:
                if stuff_being_taken.short_name == x.short_name:
                    self.inv.remove(x)
                    self.current_location.item.append(x)
        else:
            print("You don't have that in your inventory.")
    def take(self,item):
        burner = False
        i = 0
        while i < len(self.current_location.item):
            if item == self.current_location.item[i].short_name:
                stuff_being_taken = self.current_location.item[i]
                burner = True
            i += 1
        if burner:  #burner is the counter to check whether current_location
                    # has the item. 
            print("You pick up the {}.".format(stuff_being_taken.item_name))
            for x in self.current_location.item:
                if stuff_being_taken.short_name == x.short_name:
                    self.inv.append(x)
                    self.current_location.item.remove(x)
        else:
            print("You don't see anything like that here.")




