import descriptions
import quest
import usable_item

def on_use():
    print("As you rawk out on the piano, the metalhead next to you is broken from his " +
          "trance by your mad skillz (none of which Javier posesses). 'Woah, where'd you " +
          "learn to play like that?' He asks. Before you can answer, he says, 'Hey, I need " +
          "a favor. Can you go over to Tazza and show their stupid hipster a lesson for me? If " +
          "you do I can help you with with your quest for revenge")
    quest.quest_piano.complete_stage(quest.piano_start)

piano = usable_item.UsableItem("Piano", descriptions.piano, False, descriptions.pianoTake,
                               on_use, usable_item.USABLE)
