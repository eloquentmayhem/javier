import npc
import quest
import world
import player
import objects.lecture_notes

class Zoey(npc.Npc):
    def on_talk(self):
        if quest.quest_zoey.stage_completed(quest.zoey_finish):
            print("*burp* Javier sounds cute! *burp*")
        elif quest.quest_zoey.stage_completed(quest.zoey_drink):
            quest.quest_zoey.complete_stage(quest.zoey_finish)
            print("Sure, I'll go out with him! Sounds *hic* adorable!")
        elif quest.quest_zoey.stage_completed(quest.zoey_give_evidence):
            print("Javier sounds gross! I would never go out with him... sober")
        elif quest.quest_zoey.stage_completed(quest.zoey_talk):
            notes = player.player.find_elem(objects.lecture_notes.lecture_notes.name)
            if notes is None:
                print("I'm sorry but I love Jerkface and won't betray hin.")
            else:
                player.player.give_to(notes.name, self.name)
        else:
            print("You approach Zoey, having no idea what Javier sees in her. "
                  "But you know he's obsessed, so you ask her to date him in "
                  "order to let him embarass himself. She replies \"I would "
                  "think about it, but I'm already dating Jerkface Sr. And I "
                  "know he loves me so I could never walk away from that.\"")
            quest.quest_zoey.complete_stage(quest.zoey_talk)
