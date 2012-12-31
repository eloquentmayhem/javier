import descriptions
import quest
import usable_item
import world

def on_use():
    practice = world.world.practice
    if (world.world.currentRoom != practice
        or not quest.quest_piano.stage_active(quest.piano_install_amp)):
        print ("There's nothing interesting to do with that here.")
        return False

    print("That'll show Javier! Next time he tries to use his beloved piano, all he'll get is a " +
          "pile of distortion. Now on to your next mission!")
    quest.quest_piano.complete_stage(quest.piano_install_amp)
    return True

sticky_donut = usable_item.UsableItem("Amp", descriptions.amp, True,
                                    descriptions.ampTake, on_use, usable_item.CONSUMABLE,[])
