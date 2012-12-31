import container
import usable_item
import world
import npc

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
                if(hasattr(currentItem, "on_take")):
                    if not (currentItem.on_take()):
                        print("I don't see any use for that.")
                        return
                else:
                    print("You take the "+item+".")               
 
                self.add_elem(currentItem)
                world.world.currentRoom.delete_elem(item)
                return
            else:
                currentItem.print_nTakeDesc()
                return
        else:
            print("The "+item+" does not exist!")
            return
    
    #Drop the item from inventory in the current room
    def drop_item(self, item):
        self.set_item(item, world.world.currentRoom,
                      "You drop the "+item+".")

    #Give a thing to a person
    def give_to(self, item_name, target_name):
        room = world.world.currentRoom
        if room.have_elem(target_name):
            target = room.find_elem(target_name)
            self.set_item(item_name, target, "You give the "
                          +item_name+ " to " + target_name +".")
        else:
            print("You're giving the what to the who now?")

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

    #Talk to an actor in the world
    def talk_to(self, actor_name):
        room = world.world.currentRoom
        if not room.have_elem(actor_name):
            print("Who's that?")
            return
        target = room.find_elem(actor_name)
        if not isinstance(target, npc.Npc):
            print("That's going to look awfully silly, now isn't it?")
            return
        target.on_talk()

    #Give/place an item from inventory to/in specified location
    def set_item(self, item, location, display_text):
        currentItem = self.find_elem(item)
        if (currentItem is not None):
            assert (isinstance(location, container.Container))
            self.delete_elem(item)
            location.add_elem(currentItem)
            if(currentItem.on_set is not None):
                currentItem.on_set(location)
            else:
                print(display_text)
            return
        else:
            print("You don't have this item!")
            return

    def combine_item(self, item1, item2):
        currentItem1 = self.find_elem(item1)
        currentItem2 = self.find_elem(item2)
        if (currentItem1 is not None and currentItem2 is not None
            and currentItem1.is_combinable(currentItem2)):
            self.delete_elem(item1)
            self.delete_elem(item2)
            self.add_item(world.combine_dict[(item1,item2)])
        elif (currentItem1 is None or currentItem2 is None):
            print("You don't have the things you're trying to combine!")
        else:
            print("Fool! You can't combine those items!")
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
