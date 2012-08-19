import container

class Room(container.Container):
    def __init__(self, name, description):
        super(Room, self).__init__(name, description)
        self.doors = dict()
        self.visited = False
    
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
        
    #Print a description of the current room. In verbose mode, give
    #the room's description/contents as well
    def print(self, verbose):
        print("You are in " + self.name + ".")
        if verbose:
            print(self.description)
        self.print_doors()

        if verbose and len(self.items) != 0:
            print("The room contains:")
            for item in self.items:
                print(item.name)
