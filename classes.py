# Putting everything in one file named "classes" gets REALLY scary messy when
# programs get bigger. Better to put different classes in different files.
# You can start off doing this the Java-esque way where each class gets its own file,
# then later if you want you can group related classes into the same file.
import descriptions

class Container(object):
    def __init__(self, name, description):
        self.items = []
        self.name = name
        self.description = description

    
    def add_elem(self, item):
        self.items += [item]
    
    def delete_elem(self, item):
        for i in xrange(len(self.items)):
            currentItem = self.items[i]
            # Ah! Commented-out code! Good to remove this before committing.
 #           print("current Item: "+currentItem.name + "item: " + item)
            if (currentItem == item):
                    self.items.remove(currentItem)
                    return
        #not in container
        else:
            pass
    def have_elem(self, item):
        for i in xrange(len(self.items)):
            currentItem = self.items[i]
            if (currentItem.name == item):
                return True
        return False
        
    # I think you can make have_elem/delete_elem more consise by rewriting them
    # in terms of find_elem
    def find_elem(self, item):
        for i in xrange(len(self.items)):
            currentItem = self.items[i]
            if (currentItem.name == item):
                return currentItem
        return None
        
    def get_description(self):
        print(self.description)
            

class Item(object):
    def __init__(self, name, description, mutable):
        self.description = description
        self.name = name
        #true if mutable, else false
        self.mutable = mutable
    
    def is_mutable(self):
        return self.mutable
        
    # Having a function called "get<blah>" print stuff is weird. Better to either
    # return the description or rename to print_description
    def get_description(self):
        print(self.description)
                    
class Room(Container):
    def __init__(self, name, description):
        super(Room, self).__init__(name, description)
        self.doors = dict()
    
    def add_door(self, door, direction):
        self.doors[direction] = door
    
    def get_door(self, direction):
        return self.doors.get(direction)
    
    #Make thie later
    def print_doors(self):
        if (len(self.doors) == 0):
            print("Sorry, there's no doors. You're stuck here forever!")
            return
        for door in self.doors:
            print("To the "+door+": "+self.doors[door].name)
        return
        
class Player(Container):
    def __init__(self, name, description):
        super(Player, self).__init__(name, description)
        # Does this belong in Player? I feel like this more part of the world
        # than part of the player.
        #######Rooms Here#############
        dorm = Room("Javier's Dorm", descriptions.dorm)
        dorm.add_elem(Item("Wine Bottle", descriptions.wine, True))
        dorm.add_elem(Item("Bed", descriptions.bed, False))
        dorm.add_elem(Item("Settlers of Catan set", 
                        descriptions.settlers, True))
        dorm.add_elem(Item("Sheet Music", descriptions.sheetMus, True))
        dorm.add_elem(Item("Computer", descriptions.computer, True))
        #######Dorm End################
        bathroom = Room("Javier's Bathroom", descriptions.bathroom)
        bathroom.add_elem(Item("Toliet", descriptions.toliet, False))
        bathroom.add_elem(Item("Sink", descriptions.sink, False))
        #######Bathroom End############
        outside = Room("The Outside", descriptions.outside)
        outside.add_elem(Item("Zoey Deschanel", descriptions.Zoey,
                              False))
        #######Add doors###############
        dorm.add_door(bathroom, "west")
        bathroom.add_door(dorm, "east")
        dorm.add_door(outside, "north")
        outside.add_door(dorm, "south")
        self.rooms = { "Javier's Dorm":dorm, 
                       "Javier's Bathroom":bathroom,
                       "The Outside":outside}
        self.currentRoom = dorm
        
        
    def go_direction(self, direction):
        targetRoom = self.currentRoom.get_door(direction)
        # Use "targetRoom is None". Comparing against None in Python does scary things
        if (targetRoom == None):
            print("Can't go there, kiddo")
        else:
            self.currentRoom = targetRoom
            print("You go into " + self.currentRoom.name + ".")
            self.currentRoom.print_doors()
            
    def take_item(self, item):
        currentItem = self.currentRoom.find_elem(item)
        #use currentItem is not None due to scariness
        if(not(currentItem == None)):
            if (currentItem.is_mutable()):
                self.add_elem(currentItem)
                self.currentRoom.delete_elem(currentItem)
                print("You take the "+item+".")
                return
            else:
                print("You can't take the  "+item+"!")
                return
        else:
            print("The "+item+" does not exist!")
            return
    
    def set_item(self, item, location):
        currentItem = self.find_elem(item)
        # is not None
        if (not(currentItem == None)):
            if (isinstance(location, Container)):
                self.delete_elem(currentItem)
                location.add_elem(currentItem)
                print ("You drop the "+item+".")
                return
            else: 
                print("yup, haven't implemented giving to people yet")
                return
        else:
            print("You don't have this item!")
            return
    
    def get_info(self, item):
        if (self.have_elem(item)):
            currentItem = self.find_elem(item)
            currentItem.get_description()
            return
        elif (self.currentRoom.have_elem(item)):
            currentItem = self.currentRoom.find_elem(item)
            currentItem.get_description()
            return
        elif ((self.currentRoom.name == item) or ("room" == item)):
            self.currentRoom.get_description()
        elif (self.name == item):
            self.get_description()
        elif (("exits" == item) or ("doors" == item)):
            self.currentRoom.print_doors()
        else:
            print("Not valid")
    
            
    def get_inventory(self):
        pass
