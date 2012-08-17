class Item(object):
    def __init__(self, name, description, mutable):
        self.description = description
        self.name = name
        #true if mutable, else false
        self.mutable = mutable
    
    #True if item can be moved, False otherwise
    def is_mutable(self):
        return self.mutable
        
    def print_description(self):
        print(self.description)
