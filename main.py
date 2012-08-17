import parse
import classes
import module

def run_intro():
    print("Some introduction to the game here\m")
    #Raw input without enter/huge space after name
    name = raw_input("What's your name, friend?\n")
    return name

def continue_intro(name):
    description = raw_input("Ah, so your name is "+name+". \
                    So tell us more about yourself!\n")
    return description
    
def main():
    name = run_intro()
    description = continue_intro(name)
    module.player = classes.Player(name, description)
    while (True):
        parse.do_command(input())
    return

# Voodoo hillbilly magic so main() runs automagically if you do "python main.py" at the shell
if __name__ == "__main__":
    main()