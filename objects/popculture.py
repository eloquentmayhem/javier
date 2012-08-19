import descriptions
import objects.hipster_ashes
import quest
import usable_item
import world

def on_use():
    tazza = world.world.tazza
    if (world.world.currentRoom != tazza
        or not quest.quest_piano.stage_active(quest.piano_defeat_hipster)):
        print ("There's nothing interesting to do with that here.")
        return False

    print("You throw the pop culture at the hipster. They wail like a banshee as they melt " +
          "under the unbearable mainstreamness. They vanish into a pile of ashes. You should give " +
          "it to the metalhead as proof.")
    quest.quest_piano.complete_stage(quest.piano_defeat_hipster)
    tazza.delete_elem("Hipster") # This is kinda fragile but SSHHH
    tazza.add_elem(world.objects.hipster_ashes.hipster_ashes)
    return True

popculture = usable_item.UsableItem("Pop Culture", descriptions.popCulture, True,
                                    descriptions.popCultureTake, on_use, usable_item.CONSUMABLE)
