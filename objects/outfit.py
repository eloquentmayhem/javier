import descriptions
import quest
import quest_item
import world
import peeps.marla
import player
import room

def on_set(location):
    if isinstance(location, peeps.marla.Marla):
        print("You give the clothes to Marla and she, struggling, slips them on.  They look much too too tight on her. You wonder whether Javier will still be able to wear the clothing afterwards.  Marla seems incredibly pleased with herself, though, so you don't say anything.")
        quest.quest_ta.complete_stage(quest.ta_outfit)
    elif isinstance(location, room.Room):
        print("You succumb to your nose and your sanity and fling Javier's clothes on the ground")
    else:
        print("You try to give the clothing to "+location.name+", but the scent is too strong and "+location.name+" throws it back at you.")
        player.player.add_elem(outfit)
    
def on_take():
    if not (quest.quest_ta.stage_completed(quest.ta_marla_again)):
        print("You pick up Javier's clothing, but the stench of whiskey is too strong and you hurriedly drop it again.")
        return False
    else:
        print("You take Javier's black CMU hoodie and shorts and sling them over your shoulder, trying to ignore the disgustingly strong scent of whiskey. You have to remind yourself that it's all for the sake of revenge in order to not fling the clothes away.")
        return True

outfit = quest_item.QuestItem("Javier's Clothes", descriptions.outfit, on_set, on_take, [])