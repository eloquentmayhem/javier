# Most container methods operate on the item names because that makes
# it easy to hook them up to text commands. However add_elem uses the
# actual item, because, um, it has to.
class Container(object):
    def __init__(self, name, description):
        self.items = []
        self.name = name
        self.description = description

    #add item to container
    def add_elem(self, item):
        self.items += [item]
    
    #delete item from container
    def delete_elem(self, item_name):
        item = self.find_elem(item_name)
        if (item is not None):
            self.items.remove(item)
            return
        #not in container
        else:
            pass
    
    #True if item in container, False otherwise
    def have_elem(self, item_name):
        item = self.find_elem(item_name)
        return item is not None
    
    #If item is in the container get it
    def find_elem(self, item_name):
        assert item_name is not None
        for i in range(len(self.items)):
            currentItem = self.items[i]
            if (currentItem.name.lower() == item_name.lower()):
                return currentItem
        return None
        
    def print_description(self):
        print(self.description)
            
