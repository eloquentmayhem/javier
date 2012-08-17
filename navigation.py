import module

def go(direction):
    module.player.go_direction(direction)
    
def take(item):
    module.player.take_item(item)
    
def drop(item):
    module.player.set_item(item, module.player.currentRoom)
    
def info(item):
    module.player.get_info(item)
    
def smite():
    print("God smites you! You are dead.")
    exit()