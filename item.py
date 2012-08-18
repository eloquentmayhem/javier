#Edits: Got rid of mutability and changed it to takeability (which can change)

class Item(object):
    def __init__(self, name, description, takeable, nTakeDesc):
        self.description = description
        self.name = name
        #true if you can take obj at the moment, else false
        self.takeable = takeable
        #description if you try to take an obj that can't be
        #take at the moment
        self.nTakeDesc = nTakeDesc
        
    #True if item can be moved, False otherwise
    
    def is_takeable(self):
        return self.takeable
        
    def set_takeable(self, takeable):
        self.takeable = takeable        
        
    def print_description(self):
        print(self.description)

    def print_nTakeDesc(self):
        print(self.nTakeDesc)