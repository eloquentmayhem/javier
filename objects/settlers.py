import item
import quest_item
import quest
import world
import peeps.russell
import player
import descriptions

def on_set(location):
    if isinstance(location, peeps.russell.Russell):
        # Give $$$
        print("Great, you found a copy! Here's the $20! Look we can be done here right now if you want, but I must say I'd like to settle your Catan.")
        player.player.add_elem(item.Item("Money", descriptions.money, True, None, []))
        player.player.delete_elem("Settlers of Catan")
        quest.quest_sisenor.complete_stage(quest.sisenor_moneys)

        item.Item("Settlers of Catan", 
                  descriptions.settlers, True,
                                descriptions.settlersTake,[])

def on_take():
    if not (quest.quest_sisenor.stage_completed(quest.sisenor_moose)):
        return False
    quest.quest_sisenor.complete_stage(quest.sisenor_catan)
    print("You take the Settlers of Catan game. It was yours to begin with anyhow.")
    return True

settlers = quest_item.QuestItem("Settlers of Catan", descriptions.settlers, on_set, on_take, [])
