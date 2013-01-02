import npc
import quest
import world
import player

class Javier(npc.Npc):
    def on_talk(self):
        if not quest.quest_ta.stage_completed(quest.ta_observe):
            print("Javier is lecturing his matrices recitation. \"Hey, Javier,\" you ask, \"What are eigenvectors?\"  To your surpsie, Javier answers your question correctly.  You ask another question, and he knows the answer to that as well!  This is problematic.  Thankfully, you remember, just in time, your old matrices TA's lectures.  Perhaps you can sabotage Javier's TAing job after all!")
            quest.quest_ta.complete_stage(quest.ta_observe)
            return
        else:
            print("Javier is actually not terrible at teaching, you think as you listen to him. You'll soon fix that!")
            return
            
