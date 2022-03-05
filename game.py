import sys

from creature import Creature, player
from item import Item
from location import Location, print_map
from preprocessing import process_locations, process_exits,\
                          process_items, process_creatures
# python3 game.py <PATHS> <ITEMS> <CHASERS> <EXITS>
p1 = player()
if len(sys.argv) < 5:
    print("Usage: python3 game.py <PATHS> <ITEMS> <CHASERS> <EXITS>")
    exit()
locations_list = process_locations(sys.argv[1])
items_list = process_items(sys.argv[2],locations_list)
chasers_list = process_creatures(sys.argv[3],locations_list)
process_exits(sys.argv[4],locations_list)
file = open(sys.argv[1])
paths_list = file.readlines()
file.close()
if len(locations_list) == 0:
    print("The game cannot run without any rooms :(")
    exit()
if len(chasers_list) == 0:
    print("There is nothing chasing you!")
    exit()
p1.current_location = locations_list[0]
print_map(p1.current_location)
print("")
while True:
    command = input(">> ")
    if command.upper() == "HELP":
        print("HELP            - Shows some available commands.")
        print("INV             - Lists all the items in your inventory.")
        print("TAKE <ITEM>     - Takes an item from your current location.")
        print("DROP <ITEM>     - Drops an item at your current location.")
        print("")
        print("LOOK or L       - Lets you see the map/location again.")
        print("LOOK <ITEM>     - Lets you see an item in more detail.")
        print("LOOK ME         - Sometimes, you just have to admire the feathers.")
        print("LOOK <CREATURE> - Sizes up a nearby creature.")
        print("LOOK HERE       - Shows a list of all items in the room.")
        print("")
        print("NORTHWEST or NW - Moves you to the northwest.")
        print("NORTH or N      - Moves you to the north.")
        print("NORTHEAST or NE - Moves you to the northeast.")
        print("EAST or E       - Moves you to the east.")
        print("")
        print("SOUTHEAST or SE - Moves you to the southeast.")
        print("SOUTH or S      - Moves you to the south.")
        print("SOUTHWEST or SW - Moves you to the southwest.")
        print("WEST or W       - Moves you to the west.")
        print("")
        print("FLEE            - Attempt to flee from your current location.")
        print("HONK or Y       - Attempt to scare off all creatures in the same location.")
        print("WAIT            - Do nothing. All other creatures will move around you.")
        print("QUIT            - Ends the game. No questions asked.")
        print("")
    elif command.upper() == "QUIT":
        print("Game terminated.")
        exit()
    elif command.upper() == "LOOK ME":
        print("You are a goose. You are probably quite terrifying.")
        print("In fact, you have a terror rating of: {}".format(p1.get_terror_rating()))
        print("")
    elif command.upper() == "LOOK" or command.upper() == "L":
        print_map(p1.current_location)
        print("")
    elif command.upper() == "NORTHWEST" or command.upper() == "NW": #whole movement action block(start) 
        if p1.current_location.northwest != " ":
            print("You move northwest, to {}.".format(p1.current_location.northwest.name))
            i = 0
            while i < len(p1.current_location.creature):    
                p1.current_location.creature[i].attempt_to_catch = 2
                i += 1             #attempt_to_catch is a counter for chasers to catch the goose
            p1.current_location = p1.current_location.northwest
            i = 0               #the loop let every creature instance take their turn
            while i < len(chasers_list):
                chasers_list[i].take_turn(p1)
                i += 1      #take_turn is an inbuilt method of creature, go to creature for more details.
            print_map(p1.current_location)
        else:
            print("You can't go that way.") 
        print("")                  #all the rest movement action is in the same foramt
    elif command.upper() == "NORTH" or command.upper() == "N":
        if p1.current_location.north != " ":
            print("You move north, to {}.".format(p1.current_location.north.name))
            i = 0
            while i < len(p1.current_location.creature):
                p1.current_location.creature[i].attempt_to_catch = 2
                i += 1
            p1.current_location = p1.current_location.north
            i = 0
            while i < len(chasers_list):
                chasers_list[i].take_turn(p1)
                i += 1
            print_map(p1.current_location)
        else:
            print("You can't go that way.")
        print("")
    elif command.upper() == "NORTHEAST" or command.upper() == "NE":
        if p1.current_location.northeast != " ":
            print("You move northeast, to {}.".format(p1.current_location.northeast.name))
            i = 0
            while i < len(p1.current_location.creature):
                p1.current_location.creature[i].attempt_to_catch = 2
                i += 1
            p1.current_location = p1.current_location.northeast
            i = 0
            while i < len(chasers_list):
                chasers_list[i].take_turn(p1)
                i += 1
            print_map(p1.current_location)
        else:
            print("You can't go that way.")
        print("")
    elif command.upper() == "WEST" or command.upper() == "W":
        if p1.current_location.west != " ":
            print("You move west, to {}.".format(p1.current_location.west.name))
            i = 0
            while i < len(p1.current_location.creature):
                p1.current_location.creature[i].attempt_to_catch = 2
                i += 1
            p1.current_location = p1.current_location.west
            i = 0
            while i < len(chasers_list):
                chasers_list[i].take_turn(p1)
                i += 1
            print_map(p1.current_location)
        else:
            print("You can't go that way.")
        print("")
    elif command.upper() == "EAST" or command.upper() == "E":
        if p1.current_location.east != " ":
            print("You move east, to {}.".format(p1.current_location.east.name))
            i = 0
            while i < len(p1.current_location.creature):
                p1.current_location.creature[i].attempt_to_catch = 2
                i += 1
            p1.current_location = p1.current_location.east
            i = 0
            while i < len(chasers_list):
                chasers_list[i].take_turn(p1)
                i += 1
            print_map(p1.current_location)
        else:
            print("You can't go that way.")
        print("")
    elif command.upper() == "SOUTHWEST" or command.upper() == "SW":
        if p1.current_location.southwest != " ":
            print("You move southwest, to {}.".format(p1.current_location.southwest.name))
            i = 0
            while i < len(p1.current_location.creature):
                p1.current_location.creature[i].attempt_to_catch = 2
                i += 1
            p1.current_location = p1.current_location.southwest
            i = 0
            while i < len(chasers_list):
                chasers_list[i].take_turn(p1)
                i += 1
            print_map(p1.current_location)
        else:
            print("You can't go that way.")
        print("")
    elif command.upper() == "SOUTH" or command.upper() == "S":
        if p1.current_location.south != " ":
            print("You move south, to {}.".format(p1.current_location.south.name))
            i = 0
            while i < len(p1.current_location.creature):
                p1.current_location.creature[i].attempt_to_catch = 2
                i += 1
            p1.current_location = p1.current_location.south
            i = 0
            while i < len(chasers_list):
                chasers_list[i].take_turn(p1)
                i += 1
            print_map(p1.current_location)
        else:
            print("You can't go that way.")
        print("")
    elif command.upper() == "SOUTHEAST" or command.upper() == "SE":
        if p1.current_location.southeast != " ":
            print("You move southeast, to {}.".format(p1.current_location.southeast.name))
            i = 0
            while i < len(p1.current_location.creature):
                p1.current_location.creature[i].attempt_to_catch = 2
                i += 1
            p1.current_location = p1.current_location.southeast
            i = 0
            while i < len(chasers_list):
                chasers_list[i].take_turn(p1)
                i += 1
            print_map(p1.current_location)
        else:
            print("You can't go that way.")
        print("")                   #whole movement action block(finish)
    elif command.upper() == "LOOK HERE":
        if p1.current_location.item == []:
            print("There is nothing here.")
        else:
            for x in p1.current_location.item:
                burner = x.short_name.upper()
                while len(burner) < 16: #16 stand for the space that testcase required.
                    burner += " "
                burner += "|"
                print(burner,x.item_name)
        print("")
    elif command.split()[0].upper() == "TAKE":
        p1.take(command.split()[1])
        i = 0
        while i < len(chasers_list):
            chasers_list[i].take_turn(p1)
            i += 1         #take_turn is an inbuilt method of creature, go to creature for more details.
        print("")
    elif command.split()[0].upper() == "DROP":
        p1.drop(command.split()[1])
        i = 0
        while i < len(chasers_list):
            chasers_list[i].take_turn(p1)
            i += 1  #take_turn is an inbuilt method of creature, go to creature for more details.
        print("")
    elif command.split()[0].upper() == "LOOK" and len(command.split()) == 2:
        burner_for_creature = False #these two burner counter let the print work
        burner_for_item = False    # only if there is items or chasers in the location instance.
        for x in p1.current_location.creature:              #           \
            if x.name == command.split()[1].capitalize():   #           \
                burner_for_creature = True                  #     <-----
                creature_being_looking_for = x              #           \
        looking_list = p1.current_location.item + p1.inv    #           \
        for x in looking_list:                              #           \
            if x.short_name == command.split()[1].lower():  #           \
                burner_for_item = True                      #       <----
                item_being_looking_for = x
        if burner_for_creature:
            #   print different user output depends on terror_rating difference.
            if creature_being_looking_for.get_terror_rating() - p1.get_terror_rating() >= 5:
                print("{} doesn't seem very afraid of you.".format(creature_being_looking_for.name))
            elif p1.get_terror_rating() - creature_being_looking_for.get_terror_rating() >= 5:
                print("{} looks a little on-edge around you.".format(creature_being_looking_for.name))
            else:
                print("Hmm. {} is a bit hard to read.".format(creature_being_looking_for.name))
        elif burner_for_item:
            print(item_being_looking_for.item_name + " - Terror Rating: {}".format(item_being_looking_for.terror_rating))
        else:
            print("You don't see anything like that here.")
        print("")
    elif command.upper() == "INV":
        inventory = p1.get_inv()
        if len(inventory) >= 2:
            print("You, a goose, are carrying the following items:")
            for x in inventory:
                print(" - " + x)
        elif len(inventory) < 2 and len(inventory) > 0:
            print("You, a goose, are carrying the following item:")
            for x in inventory:
                print(" - " + x)
        else:
            print("You are carrying nothing.")
        print("")
    elif command.upper() == "FLEE":
        if p1.current_location.flee == True:
            print("You slip past the dastardly Goosechasers and run off into the wilderness! Freedom at last!")
            print("========= F R E E D O M =========")
            exit()
        else:
            print("There's nowhere you can run or hide! Find somewhere else to FLEE.")
            print("")
    elif command.upper() == "HONK" or command.upper() == "Y":
        if p1.current_location.creature != []:
            print("You sneak up behind your quarry and honk with all the force of a really angry airhorn! HONK!")
            i = 0
            length = len(p1.current_location.creature)
            while i < length:
                if p1.get_terror_rating() > p1.current_location.creature[i].get_terror_rating():
                    print("{} is spooked! They flee immediately!".format(p1.current_location.creature[i].name))
                    chasers_list.remove(p1.current_location.creature[i])
                    p1.current_location.creature.remove(p1.current_location.creature[i])
                    length -= 1
                else:
                    print("{} is not spooked :(".format(p1.current_location.creature[i].name))
                    j = 0
                    while j < len(chasers_list):
                        chasers_list[j].take_turn(p1)
                        j += 1  #take_turn is an inbuilt method of creature, go to creature for more details.
                i += 1
        else:
            print("All shall quiver before the might of the goose! HONK!")
        print("")
        if chasers_list == []:
            print("None can stand against the power of the goose!")
            print("========= V I C T O R Y =========")
            exit()
    elif command.upper() == "WAIT":
        print("You lie in wait.")
        print("")
        i = 0
        while i < len(chasers_list):
            chasers_list[i].take_turn(p1)
            i += 1  #take_turn is an inbuilt method of creature, go to creature for more details.
    else:
        print("You can't do that.")
        print("")
    






