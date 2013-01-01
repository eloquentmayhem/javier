import npc
import quest
import world
import player
import objects.settlers

class Russell(npc.Npc):
    def on_talk(self):
        # Don't need money yet
        if not quest.quest_sisenor.stage_completed(quest.sisenor_try_order):
            print("Hey Baby, I'm Russell, the Womanizing Moose. Do you believe in source control? Because I'd like to CHECK YOU OUT!")
        # Tell them about settlers
        elif not quest.quest_sisenor.stage_completed(quest.sisenor_moose):
            print("Sweetheart, I heard you need money, and I think we could work out a deal... OH GOD NOTHING LIKE THAT. No, you see I really like Settlers of Catan, but one of my grad students stole my set after an, ummm, \"conference\". If you can find me another copy, I'd gladly pay you for it.")
            quest.quest_sisenor.complete_stage(quest.sisenor_moose)
        elif (not quest.quest_sisenor.stage_completed(quest.sisenor_moneys)
              and quest.quest_sisenor.stage_completed(quest.sisenor_catan)):
            settlers = player.player.find_elem(objects.settlers.settlers.name)
            if settlers is None:
                print("Hey there beautiful, I want to publish a paper with you. Namely, our marriage certificate.")
            else:
                player.player.give_to(settlers.name, self.name)
        else:
            # Already gave $$$
            print("Hey girl, let's hurry up and unify already: I know you're my type.")

