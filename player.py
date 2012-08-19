import container
import usable_item
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
            targetRoom.print(not targetRoom.visited)
            targetRoom.visited = True
        
    #take item from the current room
    def take_item(self, item):
        currentItem = world.world.currentRoom.find_elem(item)
        if(currentItem is not None):
            if (currentItem.is_takeable()):
                self.add_elem(currentItem)
                world.world.currentRoom.delete_elem(item)
                print("You take the "+item+".")
                return
            else:
                currentItem.print_nTakeDesc()
                return
        else:
            print("The "+item+" does not exist!")
            return
    
    #Drop the item from inventory in the current room
    def drop_item(self, item):
        self.set_item(item, world.world.currentRoom)

    #Use an object either in the inventory or world
    def use_item(self, item_name):
        room = world.world.currentRoom
        if self.have_elem(item_name):
            location, item = self, self.find_elem(item_name)
        elif room.have_elem(item_name):
            location, item = room, room.find_elem(item_name)
        else:
            print("I don't know what that is.")
            return
        
        if not isinstance(item, usable_item.UsableItem):
            print("Can't use dat.")
            return
        
        item.use_from(location)


    #Give/place an item from inventory to/in specified location
    def set_item(self, item, location):
        currentItem = self.find_elem(item)
        if (currentItem is not None):
            if (isinstance(location, container.Container)):
                self.delete_elem(item)
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
