import item

# Usability constants: names aren't perfect, change them if you have better
# This item can only be used once and then disappears
CONSUMABLE = 1
# This item can be used more than once but its effect only happens once
USABLE = 2
# This can be used multiple times and the effect happens every time
REUSABLE = 3

class UsableItem(item.Item):
    # on_use is called when trying to use the item, and returns a bool saying whether
    # the usage succeeded.
    def __init__(self, name, description, takeable, nTakeDesc, on_use, reusability, combine):
        super(UsableItem, self).__init__(name, description, takeable, nTakeDesc, combine)
        self.on_use = on_use
        if (isinstance(nTakeDesc, str) == False):
            self.on_take = nTakeDesc
        self.reusability = reusability
        self.used = False

    def use_from(self, location):
        if self.reusability == CONSUMABLE:
            if self.on_use():
                location.delete_elem(self.name)
        elif self.reusability == USABLE:
            if self.used:
                print("You use it again. Nothing interesting happens.")
            else:
                self.used = self.on_use()
        elif self.reusability == REUSABLE:
            self.on_use()
