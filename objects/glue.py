import descriptions
import player
import quest
import usable_item
import world

def on_use():
    print ("You squeeze the bottle, hard, and suddenly find that your clothes and your skin are spotted with sticky, white glue.  Great.")
    
    
def on_take():
    print("taking glue...?")
    if not (quest.quest_ta.stage_completed(quest.ta_marla)):
        print("God no! You'd never be able to afford that!")
        return False
    else:
        print("As you eye the glue bottle suspiciously, you see that, under the $5,000 sign, there is a tiny label writing in Ultra Thin Sharpie.  You squint, and can make out the words, 'Today's special - 100% off!'  The words Sharpied below it seem to be 'Just Kidding', but you conclude that you are just misreading the phrase. However, just in case, you grab the glue and shuttle it hurriedly into your pocket before the store owners notice.")
        return True

glue = usable_item.UsableItem("Glue", descriptions.glue, True, on_take, on_use, usable_item.CONSUMABLE, ["Neon Pink Paint"])