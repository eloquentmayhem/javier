import container

class Room(container.Container):
    def __init__(self, name, description):
        super(Room, self).__init__(name, description)
        self.doors = dict()
    
    #Add an exit
    def add_door(self, door, direction):
        self.doors[direction] = door
    
    #Get the room in the direction specified if it exists
    def get_door(self, direction):
        return self.doors.get(direction)
    
    #Prints all the exits and what direction they are in
    def print_doors(self):
        if (len(self.doors) == 0):
            print("Sorry, there's no doors. You're stuck here forever!")
            return
        for door in self.doors:
            print("To the "+door+": "+self.doors[door].name)
        return
        