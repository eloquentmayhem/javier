import player
import descriptions
import item
import room

#The environment
class World(object):
    def __init__(self):
        #######Start Rooms#############
        #######Dorm Start##############
        dorm = room.Room("Javier's Dorm", descriptions.dorm)
        dorm.add_elem(item.Item("Wine Bottle", descriptions.wine, True))
        dorm.add_elem(item.Item("Bed", descriptions.bed, False))
        dorm.add_elem(item.Item("Settlers of Catan set", 
                        descriptions.settlers, True))
        dorm.add_elem(item.Item("Sheet Music", descriptions.sheetMus, True))
        dorm.add_elem(item.Item("Computer", descriptions.computer, True))
        #######Dorm End################
        #######Bathroom Start##########
        bathroom = room.Room("Javier's Bathroom", descriptions.bathroom)
        bathroom.add_elem(item.Item("Toliet", descriptions.toliet, False))
        bathroom.add_elem(item.Item("Sink", descriptions.sink, False))
        #######Bathroom End############
        #######Outside Start###########
        outside = room.Room("The Outside", descriptions.outside)
        outside.add_elem(item.Item("Zoey Deschanel", descriptions.Zoey,
                              False))
        #######Outside End#############
        #######Add doors###############
        dorm.add_door(bathroom, "west")
        bathroom.add_door(dorm, "east")
        dorm.add_door(outside, "north")
        outside.add_door(dorm, "south")
        self.rooms = { "Javier's Dorm":dorm, 
                       "Javier's Bathroom":bathroom,
                       "The Outside":outside}
        self.currentRoom = dorm
    
    
    #Print description of item specified
    def print_info(self, item):
        #Print info about item in player's inventory 
        if (player.player.have_elem(item)):
            currentItem = player.player.find_elem(item)
            currentItem.print_description()
            return
        #Print info about item in current room
        elif (self.currentRoom.have_elem(item)):
            currentRoom = self.currentRoom.find_elem(item)
            currentRoom.print_description()
            return
        #Print info about room
        elif ((item == self.currentRoom.name) or (item == "room")):
            self.currentRoom.print_description()
        #Print info about player
        elif (item == player.player.name):
            player.player.print_description()
        #Print info about exits from the current room
        elif ((item == "exits") or (item == "doors")):
            self.currentRoom.print_doors()
        #Print info about what's in your inventory    
        elif ((item == "inventory") or (item == "items")):
            player.player.print_inventory()
        else:
            print("You could not obtain any information about this item."),
            print("Perhaps it's a figment of your imagination?")
            
world = World()