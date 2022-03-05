from creature import Creature
from item import Item
from location import Location

def process_locations(source):
    try:
        file = open(source)
    except FileNotFoundError:
        print("You have specified an invalid configuration file.")
        exit()
    paths_list = file.readlines()
    file.close()
    burner = []
    for x in paths_list:
        y = x.split(" > ")
        for m in y:
            burner.append(m.strip("\n").strip(" "))
    length = len(burner)
    i = 0
    while i < len(burner): # get rid of the direction words
        if burner[i].upper() == "WEST" or burner[i].upper() == "EAST" \
            or burner[i].upper() == "NORTH" or burner[i].upper()== "SOUTH" \
            or burner[i].upper() == "NORTHWEST" or burner[i].upper() ==  "NORTHEAST"\
            or burner[i].upper() == "SOUTHEAST" or burner[i].upper() == "SOUTHWEST":
            burner.remove(burner[i])
            length -= 1
            continue
        i += 1
    locations_list = list(dict.fromkeys(burner)) # get rid of the duplicates
    i = 0
    while i < len(locations_list):
        if locations_list[i] == "": # take care of the special case when paths 
            locations_list.remove(locations_list[i])# configuration files have 
        i += 1                      #extra lines between blocks of paths
    burner = []
    for x in locations_list:
        burner.append(Location(x))
    locations_list = burner
    locations_list_1 = locations_list
    for x in locations_list: # set up the relationships between locations(start)
        for y in paths_list:
            if x.name == y.split(" > ")[0]:
                if y.split(" > ")[1].upper() == "NORTH":
                    for m in locations_list_1:
                        if m.name == y.split(" > ")[2].strip("\n").strip(" "):
                            x.north = m
                elif y.split(" > ")[1].upper() == "SOUTH":
                    for m in locations_list_1:
                        if m.name == y.split(" > ")[2].strip("\n").strip(" "):
                            x.south = m
                elif y.split(" > ")[1].upper() == "EAST":
                    for m in locations_list_1:
                        if m.name == y.split(" > ")[2].strip("\n").strip(" "):
                            x.east = m
                elif y.split(" > ")[1].upper() == "WEST":
                    for m in locations_list_1:
                        if m.name == y.split(" > ")[2].strip("\n").strip(" "):
                            x.west = m
                elif y.split(" > ")[1].upper() == "NORTHEAST":
                    for m in locations_list_1:
                        if m.name == y.split(" > ")[2].strip("\n").strip(" "):
                            x.northeast = m
                elif y.split(" > ")[1].upper() == "NORTHWEST":
                    for m in locations_list_1:
                        if m.name == y.split(" > ")[2].strip("\n").strip(" "):
                            x.northwest = m
                elif y.split(" > ")[1].upper() == "SOUTHEAST":
                    for m in locations_list_1:
                        if m.name == y.split(" > ")[2].strip("\n").strip(" "):
                            x.southeast = m
                elif y.split(" > ")[1].upper() == "SOUTHWEST":
                    for m in locations_list_1:
                        if m.name == y.split(" > ")[2].strip("\n").strip(" "):
                            x.southwest = m # set up the relationships between locations(finish)
    return locations_list

def process_items(source, locations):
    burner = []
    try:
        file = open(source)
    except FileNotFoundError:
        print("You have specified an invalid configuration file.")
        exit()
    lines = file.readlines()
    file.close()
    file = open(source)
    i = 0
    while i < len(lines):
        item_details = file.readline().split(" | ")
        if len(item_details) > 2:
            burner.append(Item(item_details[0],item_details[1],item_details[2],item_details[3],item_details[4].strip("\n")))
        i += 1
    file.close()
    item_list = burner
    for x in item_list:
        for y in locations:
            if x.location == y.name:
                y.item.append(x)
    return item_list

def process_creatures(source, locations):
    burner = []
    try:
        file = open(source)
    except FileNotFoundError:
        print("You have specified an invalid configuration file.")
        exit()
    lines = file.readlines()
    file.close()
    file = open(source)
    i = 0
    while i < len(lines):
        creature_details = file.readline().split(" | ")
        burner.append(Creature(creature_details[0],creature_details[1],creature_details[2],creature_details[3],creature_details[4].rstrip()))
        i += 1
    file.close()
    creatures_list = burner
    for x in creatures_list:
        for y in locations:
            if x.location == y.name:
                y.creature.append(x)
                x.location = y
                x.current_location = y
    return creatures_list

def process_exits(source, locations):
    try:
        file = open(source)
    except FileNotFoundError:
        print("You have specified an invalid configuration file.")
        exit()
    exits = file.readlines()
    file.close()
    for x in exits:
        i = 0
        while i < len(locations):
            if x.strip("\n").strip(" ") == locations[i].name:
                locations[i].flee = True
            i += 1










