import quest_item
import quest
import world
import peeps.zoey
import descriptions

def on_set(location):
    if isinstance(location, peeps.zoey.Zoey):
        print("You give Zoey the bottle of wine. Without pausing, she chugs it in " +
              "its entirety, tears of heartbreak streaming down her face. She " +
              "gives out a loud belch and stares at you, inebriated. She looks " +
              "like she might be ready to date Javier now, but she hasn't said " +
              "anything yet.")
        quest.quest_zoey.complete_stage(quest.zoey_drink)

def on_take():
    if not (quest.quest_zoey.stage_completed(quest.zoey_give_evidence)):
        return False
    quest.quest_zoey.complete_stage(quest.zoey_booze)
    print("You take the bottle, before the bottle takes you")
    return True

wine = quest_item.QuestItem("Wine Bottle", descriptions.wine, on_set, on_take)
