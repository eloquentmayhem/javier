import parse
import player
#import world

#Introduces the game and gets name of player to mercilessly mock later
def run_intro():
    print("Some introduction to the game here\m")
    #Raw input without enter/huge space after name
    name = input("What's your name, friend?\n")
    return name

#Gets player's self introduction
def continue_intro(name):
    description = input("Ah, so your name is "+name+
                        ". So tell us more about yourself!\n")
    return description
    
def main():
    name = run_intro()
    description = continue_intro(name)
    player.player = player.Player(name, description)
 #   world.world = world.World()
    while (True):
        parse.do_command(input())
    return

# Voodoo hillbilly magic so main() runs automagically if you do "python main.py" at the shell
if __name__ == "__main__":
    main()
