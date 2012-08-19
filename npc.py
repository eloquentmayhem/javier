import container

class Npc(container.Container):
    def __init__(self, name, description, takeable, nTakeDesc):
        super(Npc, self).__init__(name, description)
        #true if you can take obj at the moment, else false
        self.takeable = takeable
        #description if you try to take an obj that can't be
        #take at the moment
        self.nTakeDesc = nTakeDesc

    def is_takeable(self):
        return self.takeable
        
    def set_takeable(self, takeable):
        self.takeable = takeable        
        
    def print_nTakeDesc(self):
        print(self.nTakeDesc)
        
    def give_item(self, item):
        player.player.add_elem(item)
        self.delete_elem(item.name)
        
    def use_item(self, item):
        self.delete_elem(item)
