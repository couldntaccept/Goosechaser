class Location:
    def __init__(self, name):
        self.name = name
        self.flee = False
        self.item = []
        self.creature = []
        self.north = " "
        self.south = " "
        self.west = " "
        self.east = " "
        self.northwest = " "
        self.northeast = " "
        self.southeast = " "
        self.southwest = " "
        """
        TODO: Constructor; instantiates a Location object. You may modify
        this constructor so that it can receive additional arguments (or
        fewer arguments).
        """

    def add_item(self, item_name):
        self.item.append(item_name)

        """
        TODO: Might help when something is DROPped at a Location, but
        but can be useful in other ways.
        """

    def remove_item(self, item_name):
        self.item.remove(item_name)
        """
        TODO: Might help when something is TAKEn from a Location, but
        but can be useful in other ways.
        """
    def add_creature(self, creature_name):
        self.creature.append(creature_name)

    def remove_creature(self,creature_name):
        self.creature.remove(creature_name)


def print_map(current_location):
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    fifth_line = ""
    if current_location.northwest != " ": # first_line and second_line kniting(START)
        if len(current_location.northwest.creature) == 0:
            first_line += "[ ]"
        else:
            first_line += "[C]"
        second_line += "   \\"
    if current_location.north != " ":
        if current_location.northwest != " ":
            if len(current_location.north.creature) == 0:
                first_line += " [ ]"
            else:
                first_line += " [C]"
            second_line += " |"
        else:
            if len(current_location.north.creature) == 0:
                first_line += "    [ ]"
            else:
                first_line += "    [C]"
            second_line += "     |"
    if current_location.northeast != " ":
        if current_location.north == " " \
            and current_location.northwest != " ":
            if len(current_location.northeast.creature) == 0:
                first_line += "     [ ]"
            else:
                first_line += "     [C]"
            second_line += "   /"
        elif current_location.north == " "\
            and current_location.northwest == " ":
            if len(current_location.northeast.creature) == 0:
                first_line += "        [ ]"
            else:
                first_line += "        [C]"
            second_line += "       /"
        elif current_location.north != " ":
            if len(current_location.northeast.creature) == 0:
                first_line += " [ ]"
            else:
                first_line += " [C]"
            second_line += " /"# first_line and second_line kniting(FINISH)
    if current_location.west != " ": #third_line kniting(START)
        if len(current_location.west.creature) == 0:
            third_line += "[ ]-"
        else:
            third_line += "[C]-"
    else:
        third_line += "    "
    third_line += "[x]"
    if current_location.east != " ":
        if len(current_location.east.creature) == 0:
            third_line += "-[ ]"
        else:
            third_line += "-[C]"#third_line kniting(FINISH)
    if current_location.southwest != " ": # fourth_line and fifth_line kniting(START)
        if len(current_location.southwest.creature) == 0:
            fifth_line += "[ ]"
        else:
            fifth_line += "[C]"
        fourth_line += "   /"
    if current_location.south != " ":
        if current_location.southwest != " ":
            if len(current_location.south.creature) == 0:
                fifth_line += " [ ]"
            else:
                fifth_line += " [C]"
            fourth_line += " |"
        else:
            if len(current_location.south.creature) == 0:
                fifth_line += "    [ ]"
            else:
                fifth_line += "    [C]"
            fourth_line += "     |"
    if current_location.southeast != " ":
        if current_location.south == " " \
            and current_location.southwest != " ":
            if len(current_location.southeast.creature) == 0:
                fifth_line += "     [ ]"
            else:
                fifth_line += "     [C]"
            fourth_line += "   \\"
        elif current_location.south == " "\
            and current_location.southwest == " ":
            if len(current_location.southeast.creature) == 0:
                fifth_line += "        [ ]"
            else:
                fifth_line += "        [C]"
            fourth_line += "       \\"
        elif current_location.south != " ":
            if len(current_location.southeast.creature) == 0:
                fifth_line += "[ ]"
            else:
                fifth_line += "[C]"
            fourth_line += "  \\"#fourth_line and fifth_line kniting(FINISH)
    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)
    print(fifth_line)
    print("You are now at: {}.".format(current_location.name))
    if current_location.creature == [] and current_location.item == []:
        print("There is nothing here.") # this block is for printing different
    else:                               # message depends on the creatures_list
        burner = ""                     # and the items_list of the location
        i = 0                           # instance.
        while i < len(current_location.item):
            if i == len(current_location.item)-1:
                burner += current_location.item[i].full_desc
            else:
                burner += current_location.item[i].full_desc
                burner += " "
            i += 1
        if current_location.creature != [] and current_location.item != []:
            burner += " "
        i = 0
        while i < len(current_location.creature):
            if i == len(current_location.creature)-1:
                burner += current_location.creature[i].description
            else:
                burner += current_location.creature[i].description
                burner += " "
            i += 1
        print(burner)
    if current_location.flee == True:
        print("The path to freedom is clear. You can FLEE this place.")












