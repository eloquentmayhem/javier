import descriptions
import player
import quest
import usable_item
import world

def on_use():
    print ("The neon pink glue gets everywhere, in your hands,on your clothes, in your hairs... Brilliant idea, Sherlock.")
    
def on_take():
    print ("You take the neon pink glue")
    
neon_glue = usable_item.UsableItem("Neon Pink Glue", descriptions.neon_glue, True, on_take, on_use, usable_item.CONSUMABLE, ["Moldy Doughnut"])