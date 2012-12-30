""" Here be where we parse commands entered by the player and run the matching
function. There are lots of fancy things we could do here but for now I tried
to keep it simple. Look at "commands" below for the syntax to add a new command
"""

import player
import quest
import world

""" Each command is a format string, followed by a function to call, followed by
extra arguments to give to that function. For example the command ("n", player.player.go_direction, ["north"])
means that if the player types "n" we will execute player.player.go_direction("north")

A format string is some text the player has to type in, with a wildcard (dollar sign) in places where
they can substitute in arbitrary text. For example the take command could be "take $", because you
can take a whole bunch of different things. When we call the function for a command, we add in an
argument for each wildcard. These arguments all go after the ones specified in the command.

Do not put two wildcards right next to each other, though separating them by a space is ok.
"""

commands = [
            # Navigation commands
            ("n", player.player.go_direction, ["north"]),
            ("e", player.player.go_direction, ["east"]),
            ("w", player.player.go_direction, ["west"]),
            ("s", player.player.go_direction, ["south"]),
            ("north", player.player.go_direction, ["north"]),
            ("east", player.player.go_direction, ["east"]),
            ("west", player.player.go_direction, ["west"]),
            ("south", player.player.go_direction, ["south"]),
            ("go $", player.player.go_direction, []),
            
            # Object manipulation
            ("take $", player.player.take_item, []),
            ("drop $", player.player.drop_item, []),
            ("use $", player.player.use_item, []),

            # Information-viewing commands
            ("info $", world.world.print_info, []),
            ("info", world.world.print_info, [None]),
            ("examine $", world.world.print_info, []),
            ("examine", world.world.print_info, [None]),
            ("look $", world.world.print_info, []),
            ("look", world.world.print_info, [None]),
            ("inventory", player.player.print_inventory, []),
            ("i", player.player.print_inventory, []),
            ("quests", quest.print_quests, []),
            ("quest", quest.print_quests, []),
            ("quit", exit, [])]

# Given a line of input, look for and execute a matching command. If you can't,
# might as well make fun of the player.
def do_command(line):
    for command in commands:
        if (try_command(command, line)):
            return
    # Mock mock mock
    print("rofl")

# Given a command definition and a line of input, check whether that line
# is trying use that command. If so, use the command!
def try_command(command, line):
    # Break it up into format string, function and default args.
    pattern, func, args = command
    # Do a split on the wildcard character to find all the bits of text that have
    # to match exactly
    literals = pattern.split("$")
    # Check if the beginning of the line matches our command
    if (not line.startswith(literals[0])):
        return False
    # Strip off the matching text
    line = line[len(literals[0]):]
    literals = literals[1:]
    for literal in literals:
        # This should only happen if we have a wildcard at the end of the command
        # so everything should be "before" the wildcard
        if (literal == ""):
            before, match, after = line, "", ""
        else:
            before, match, after = line.partition(literal)
        # match is empty if the match failed, or the literal if it succeeded
        if (match != literal):
            return False
        # Extract the wildcard text
        args = args + [before]
        line = after
    if line != "":
        return False
    # Finished parsing. Now call the command's function with all the args we found.
    func(*args)
    return True
