class Container(object):
    def __init__(self, name, description):
        self.items = []
        self.name = name
        self.description = description

    #add item to container
    def add_elem(self, item):
        self.items += [item]
    
    #delete item from container
    def delete_elem(self, item):
        if (self.have_elem(item)):
            self.items.remove(currentItem)
            return
        #not in container
        else:
            pass
    
    #True if item in container, False otherwise
    def have_elem(self, item):
        currentItem = self.find_elem(item)
        if (currentItem is not None):
            return True
        return False
    
    #If item is in the container get it
    def find_elem(self, item):
        for i in range(len(self.items)):
            currentItem = self.items[i]
            if (currentItem.name.lower() == str(item).lower()):
                return currentItem
        return None
        
    def print_description(self):
        print(self.description)
            
