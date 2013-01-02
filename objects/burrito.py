#TODO: Insert burrito mechanics here

import quest_item
import quest
import world
import descriptions

def on_set(location):
    pass

def on_take():
    pass

burrito = quest_item.QuestItem("Burrito", descriptions.burrito, on_set, on_take, [])
