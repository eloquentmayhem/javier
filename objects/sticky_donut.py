import descriptions
import quest
import quest_item
import world
import peeps.marla
import player
import room

def on_set(location):
    if isinstance(location, peeps.marla.Marla):
        print("You give the neon pink doughnut to Marla and her eyes light up.  She snatches it from your hand and it disappears into her mouth.  \"That was good!\" she exclaimed, \"The icing was thick and gooey and perfect.  I've never tasted anything like it.  Where did you find this?\"  \n\"Err...\" you smile sheepishly, \"That's a secret\" \nYou watch as Marla licks the doughnut residue off of her fingers and hopes that she doesn't get sick until after she teaches Javier's recitation. ")
        quest.quest_ta.complete_stage(quest.ta_doughnut)
        return
    elif isinstance(location, room.Room):
        print("You drop the sticky neon pink doughnut. It sticks to the ground.")
    else:
        print("You try to give the doughnut to "+location.name+", but your doughnut is easily seen for what it was, a moldy doughnut covered with neon pink paint and glue. \"Ew, gross!\" "+location.name+" screamed, throwing your doughnut onto the floor. \"Why would you give me something like this?\"")
        world.world.currentRoom.add_elem(sticky_donut)
        
def on_take():
    print("You take the sticky neon pink doughnut. It almost looks edible.")
    world.world.currentRoom.delete_elem("Sticky Neon Pink Doughnut")
    return True


sticky_donut = quest_item.QuestItem("Sticky Neon Pink Doughnut", descriptions.sticky_donut, on_set, on_take, [])