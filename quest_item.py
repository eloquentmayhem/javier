# Doesn't cover all quest items, just the common case of a quest
# item that you take and then give to a person

import item

class QuestItem(item.Item):
    def __init__(self, name, description, on_set, on_take, combine):
        super(QuestItem, self).__init__(name, description, True, None, combine)
        self.on_set = on_set
        self.on_take = on_take
