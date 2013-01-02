import descriptions
import player
import quest
import usable_item
import world

def on_use():
    print ("Ew, why would you try to eat that?")
    
    
def on_take():
    if not (quest.quest_ta.stage_completed(quest.ta_marla)):
        print("Ew, why would you even touch that?")
        return False
    else:
        print("You take the moldy doughnut, trying not to grimace.  Marla" +
        " would never eat something like this. Now if only there was a way to make it more appetizing...")
        return True

doughnut = usable_item.UsableItem("Moldy Doughnut", descriptions.doughnut, True, on_take, on_use, usable_item.CONSUMABLE, ["Neon Pink Glue"])