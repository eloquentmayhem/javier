import container
import world

#The player, or YOU!
class Player(container.Container):
    def __init__(self, name, description):
        super(Player, self).__init__(name, description)
        
    #go north, south, east, or west if possible
    def go_direction(self, direction):
        targetRoom = world.world.currentRoom.get_door(direction)

        if (targetRoom is None):
            print("Can't go there, kiddo")
        else:
            world.world.currentRoom = targetRoom
            print("You go into " + world.world.currentRoom.name + ".")
            world.world.currentRoom.print_doors()
            
    #take item from the current room
    def take_item(self, item):
        currentItem = world.world.currentRoom.find_elem(item)
        if(currentItem is not None):
            if (currentItem.is_mutable()):
                self.add_elem(currentItem)
                world.world.currentRoom.delete_elem(currentItem)
                print("You take the "+item+".")
                return
            else:
                print("You can't take the "+item+"!")
                return
        else:
            print("The "+item+" does not exist!")
            return
    
    #Drop the item from inventory in the current room
    def drop_item(self, item):
        self.set_item(item, world.world.currentRoom)
    
    #Give/place an item from inventory to/in specified location
    def set_item(self, item, location):
        currentItem = self.find_elem(item)
        if (currentItem is not None):
            if (isinstance(location, container.Container)):
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
    
    #prints what you are holding
    def print_inventory(self):
        print("You are holding:"),
        for i in range(len(self.items)):
            print (self.items[i].name + ","),
        if (len(self.items) == 0):
            print("your intangible hatred towards Javier")
        else:
            print("your intangible hatred towards Javier")
        return
        
#Initialize player (so navigation doesn't do funny stuff)        
player = Player("", "")