import quest_item
import quest
import world
import descriptions
import peeps.zoey

def on_set(location):
    if isinstance(location, peeps.zoey.Zoey):
        print("You give the lecture notes to Zoey. First she's confused - " +
              "she's one of the preeminent type theorists in Hollywood and " +
              "doesn't see what she could learn from them. Then she sees all"+ 
              " the bad jokes about \"Call Me Maybe\" evaluation and knows it"+
              " could only mean that her man has fallen for competing starlet"+
              " Carly Rae Jepsen. She breaks down in tears at the news - "+
              "\"How could he betray me like this???\"")
        quest.quest_zoey.complete_stage(quest.zoey_give_evidence)

def on_take():
    if not (quest.quest_zoey.stage_completed(quest.zoey_talk)):
        return False
    quest.quest_zoey.complete_stage(quest.zoey_evidence)
    print("You find Jerkface Sr.'s lecture notes - which betray his infidelity to Zoey!")
    return True

lecture_notes = quest_item.QuestItem("Lecture Notes", descriptions.lectureNotes, on_set, on_take, [])
