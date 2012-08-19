import descriptions
import objects.amp
import player
import quest
import usable_item
import world

def on_use():
    practice = world.world.practice
    if (world.world.currentRoom != practice
        or not quest.quest_piano.stage_active(quest.piano_give_ashes)):
        print ("There's nothing interesting to do with that here.")
        return False

    print("The metalhead sees the pile of hipster ashes you retrieved. 'Woah, man! That shit is" +
          " so metal!' he exclaims. He goes for a high five but you're still holding the ashes." +
          " He takes them from you. 'As promised, here's a little something to help in your " +
          "quest. It's up to you what to do with it, but knowing Javier you can find something "+
          "to do with it.' he hands you an amplifier.")
    quest.quest_piano.complete_stage(quest.piano_give_ashes)
    player.player.add_elem(objects.amp.amp)
    return True

hipster_ashes = usable_item.UsableItem("Hipster Ashes", descriptions.hipsterAshes, True,
                                    descriptions.hipsterAshesTake, on_use, usable_item.CONSUMABLE)
