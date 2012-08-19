import player
import descriptions
import item
import room
import npc

#The environment
class World(object):
    def __init__(self):
        #######Start Rooms#############
        
        
        ############DORM###############
        #######Bedroom Start###########
        dorm = room.Room("Javier's Dorm", descriptions.dorm)
        dorm.add_elem(item.Item("Wine Bottle", descriptions.wine, True, 
                                descriptions.wineTake))
        dorm.add_elem(item.Item("Bed", descriptions.bed, False,
                                descriptions.bedTake))
        dorm.add_elem(item.Item("Settlers of Catan set", 
                                descriptions.settlers, False,
                                descriptions.settlersTake))
        dorm.add_elem(item.Item("Sheet Music", descriptions.sheetMus, 
                                False, descriptions.sheetMusTake))
        dorm.add_elem(item.Item("Computer", descriptions.computer, False,
                                descriptions.computerTake))
        dorm.add_elem(item.Item("Amp", descriptions.amp, False,
                                descriptions.ampTake))
        #######Dorm End################
        #######Bathroom Start##########
        bathroom = room.Room("Javier's Bathroom", descriptions.bathroom)
        bathroom.add_elem(item.Item("Toliet", descriptions.toliet, False,
                                    descriptions.tolietTake))
        bathroom.add_elem(item.Item("Sink", descriptions.sink, False,
                                    descriptions.sinkTake))
        #######Bathroom End############
        #######Outside Start###########
        outside = room.Room("The Outside", descriptions.outside)
        outside.add_elem(npc.Npc("Zoey Deschanel", descriptions.Zoey,
                                    False, descriptions.ZoeyTake))
        #######Outside End#############
        
        
        #############WEAN##############
        wean = room.Room("Wean Hall", descriptions.wean)
        ########classroom Start########
        classroom = room.Room("Javier's Classroom", descriptions.classroom)
        classroom.add_elem(item.Item("Chalkboard", descriptions.chalkboard,
                                     False, descriptions.chalkboardTake))
        classroom.add_elem(item.Item("Chalk", descriptions.chalk, False,
                                     descriptions.chalkTake))
        ######Jacob's Office Start#####
        office = room.Room("Jacob's Office", descriptions.office)
        office.add_elem(npc.Npc("Jacob Davis", descriptions.jacob, False,
                                   descriptions.jacobTake))
        #############CFA###############
        cfa = room.Room("College of Fine Arts", descriptions.cfa)
        ########piano room Start#######
        practice = room.Room("Practice Room", descriptions.practice)
        practice.add_elem(item.Item("Piano", descriptions.piano, False,
                                    descriptions.pianoTake))
        practice.add_elem(item.Item("Music Stand", descriptions.stand,
                                    False, descriptions.standTake))
        
        #######Add doors###############
        dorm.add_door(bathroom, "west")
        bathroom.add_door(dorm, "east")
        dorm.add_door(outside, "north")
        outside.add_door(dorm, "south")
        outside.add_door(wean, "north")
        wean.add_door(outside, "south")
        wean.add_door(classroom, "east")
        classroom.add_door(wean, "west")
        wean.add_door(office, "west")
        office.add_door(wean, "east")
        outside.add_door(cfa, "west")
        cfa.add_door(outside, "east")
        cfa.add_door(practice, "north")
        practice.add_door(cfa, "south")
        self.rooms = { "Javier's Dorm":dorm, 
                       "Javier's Bathroom":bathroom,
                       "The Outside":outside,
                       "Wean Hall":wean,
                       "Javier's Classroom":classroom,
                       "Jacob's Office":office,
                       "The College of Fine Arts":cfa,
                       "Practice Room":practice}
        self.currentRoom = dorm
    
    def find_room(self, item):
        for room in self.rooms:
            currentItem = find_elem(item)
            if (item is not None):
                return room
        return None
    
    def move_object_to(self, item, destLoc):
        curLoc = find_room(item)
        if (room is not None):
            destLoc.add_elem(item)
            curLoc.delete_elem(item)
        else:
            print("Initalizing Error: item" + item + "is not found")
    
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
        elif ((item is None) or (item == self.currentRoom.name) or (item == "room")):
            self.currentRoom.print(True)
        #Print info about player
        elif (item.lower() == player.player.name.lower()):
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
