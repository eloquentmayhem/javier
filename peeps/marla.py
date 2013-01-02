import npc
import quest
import world
import player

class Marla(npc.Npc):
    def on_talk(self):
        if quest.quest_ta.stage_completed(quest.ta_finish):
            print("\"Blah, blah, blah, blah!\" Marla says, \"The identity matrix is the matrix with all twos!\"")
        elif quest.quest_ta.stage_completed(quest.ta_leave_marla):
            print("'Javier' is teaching matrices when you walk in. \"What's an eigenvalue?\" you ask. \n\"Ugh,\", 'he' responds, \"An eigenvalue is clearly a value that needs ironing.\"  \nYou nod and smile as you listen to the rest of the lecture. Javier's teaching has been foiled at last!")
            quest.quest_ta.complete_stage(quest.ta_finish)
        elif quest.quest_ta.stage_completed(quest.ta_outfit):
            print("Marla slips on Javier's outfit.  It's a little tight, and her hair is a shade too dark, but other than that she looks almost exactly like Javier!  \"I'm off to teach Javier's... er... my recitation!\" Neon pink 'icing' still smudged on her lips, she skips away happily.")
            world.world.classroom.delete_elem("Javier Vazquez-Trejo")
            world.world.office.delete_elem(self.name)
            world.world.classroom.add_elem(self)
            quest.quest_ta.complete_stage(quest.ta_leave_marla)
        elif quest.quest_ta.stage_completed(quest.ta_doughnut):
            print("\"Now that I've had my fill, I'd be happy to help you,\" Marla said, wiping her neon-pink stained face, \"But I'm afraid I can't pass for Javier.  You see he's a man, and I'm a woman.  Now, I have a boyfriend, but if you could change me into a man for an hour or two...\"")
            quest.quest_ta.complete_stage(quest.ta_marla_again)
        elif quest.quest_ta.stage_completed(quest.ta_marla):
            print("\"Oh, if only I weren't so hungry!\" Marla looks sadly up at you.")
        elif quest.quest_ta.stage_completed(quest.ta_observe):
            print("\"Hello Marla, do you remember me?\" You ask as you approach Marla's desk.  She looks up from the youtube video of cats that she had been watching. \n\"Er, of course I remember you... er...\" \n \"I'm "+player.player.name+",\" you remind her, \"I was in your matrices class.\" \n\"Ah,\" she replies, though she still seems a little confused, \"Can I help you?\" \n\"Yes, actually,\" you smile, trying your best to sound convincing, \"You see, my friend Javier isn't feeling so well, and so he can't TA his matrices recitation. I remember how good of a TA you were.  Could you teach for him?\" \n\"Oh,\" Marla smiled, \"I would, but I haven't eaten from two hours, and I'm hungry.  If only I had something to eat, then I would be happy to oblige!\"")
            quest.quest_ta.complete_stage(quest.ta_marla)
        else:
            print("You try to talk to Marla, but she seems too mesmerized by her cat videos to notice you.")
