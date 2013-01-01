import descriptions
import player
import quest
import usable_item
import world

def on_use():
    print ("You splash the paint onto yourself while trying to open the bottle. Oops.")
    
    
def on_take():
    if not (quest.quest_ta.stage_completed(quest.ta_marla)):
        print("Although neon pink might be a dashing color, you ultimately conclude that it does not go with your skin tone and put it back on the shelf.")
        return False
    else:
        print("You grab the neon pink paint off the shelf and stuff it into the pocket.  They have so many bottles.  They'd never be able to tell the difference!")
        return True

paint = usable_item.UsableItem("Neon Pink Paint", descriptions.paint, True, on_take, on_use, usable_item.CONSUMABLE, ["Glue"])