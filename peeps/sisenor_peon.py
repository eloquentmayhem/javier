import npc
import quest
import world
import player
import objects.burrito


class SisenorPeon(npc.Npc):
    def on_talk(self):
        if not quest.quest_sisenor.stage_completed(quest.sisenor_try_order):
            print("The Si Senor peon spends about 10 minutes jabbering with his coworkers until he notices your presence. \"Hey can I helps yous?\" he asks. You're about to tell him you want to order a burrito so you can make Javier sick, but you realize you're all out of blocks and DineX (silly freshman with your meal plan). You awkwardly mutter \"umm no actually I think I'm going to eat off campus today\". Now you need to find some money to get your burrito.")
            quest.quest_sisenor.complete_stage(quest.sisenor_try_order)
            return
        elif quest.quest_sisenor.stage_completed(quest.sisenor_moneys) and not quest.quest_sisenor.stage_completed(quest.sisenor_order):
            player.player.delete_elem("Money")
            player.player.add_elem(objects.burrito.burrito)
            quest.quest_sisenor.complete_stage(quest.sisenor_order)
            print("\"Does you want a burrito or doesn't chu?\" the Si Senor peon spits at you. You were tempted to complain about his service and then you remembered the part where you'd rather be attacked by a flock of wild zebras than work at campus dining. \"I'll take the burrito, yes,\" you tell him. \"Ok that's 20 bucks.\" You look in horror for a moment at how expensive it is, but you're not actually surprised since it's CMU. You fork over the money and a few hours later you're the proud new owner of a so-called \"burrito\".")
        else:
            print("You want fries with that?")
            return
            
