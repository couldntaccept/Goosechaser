from creature import Creature
from item import Item


def test_creatures_1():
    """
    Here we try to assign invalid type of input for terror_rating of creature class
    """
    try:
        c1 = Creature("pig","There is a pig in the corner.", "unknown", "Gate", "north")
    except ValueError:
        print("Test 1 failed.")
def test_creatures_2():
    """
    Here we test whether the get_terror_rating method of creature is working 
    or not.
    """
    c2 = Creature("pig","There is a pig in the corner.", "5", "Gate", "north")
    if c2.get_terror_rating() != 5:
        print("Test 2 failed.")
def test_creatures_3():
    """
    Here we initialize a legit working creature instance and let it TAKE a item 
    to see whether the terror_rating of the instance is change or not. 
    """
    c3 = Creature("pig","There is a pig in the corner.", "5", "Gate", "north")
    item_1 = Item("sword", "BF_sword", "storm hidden in the peace····", 3, "summoner hill")
    c3.take(item_1)
    if c3.get_terror_rating() != 8:
        print("Test 3 failed.")
def test_creatures_4():
    """
    Here we initialize a legit working creature instance with a item when it be 
    created, then let the instance DROP it, the test will fail if the terror_rating
    of the instance is not the initialed one.
    """
    c4 = Creature("pig","There is a pig in the corner.", "5", "Gate", "north")
    item_2 = Item("sword", "BF_sword", "storm hidden in the peace····", 3, "summoner hill")
    c4.inv.append(item_2)
    if c4.get_terror_rating() != 5:
        print("Test 4 failed.")
def test_creatures_5():
    """
    Here we initialize a legit working creature instance and let it TAKE a item
    then DROP it, test will fail if the terror_rating of the instance is not
    initialed one.
    """
    c5 = Creature("pig","There is a pig in the corner.", "5", "Gate", "north")
    item_3 = Item("sword", "BF_sword", "storm hidden in the peace····", 3, "summoner hill")
    c5.take(item_3)
    c5.drop(item_3)
    if c5.get_terror_rating() != 5:
        print("Test 5 failed.")

