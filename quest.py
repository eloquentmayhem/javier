class Quest:
    def __init__(self, name, all_stages):
        self.name = name
        self.completed_stages = []
        self.active_stages = []
        self.all_stages = all_stages
        self.is_complete = False

    # Assumes stage is active and quest is not complete
    def complete_stage(self, stage):
        assert not self.is_complete
        for active_stage in self.active_stages:
            if active_stage == stage:
                self.active_stages.remove(stage)
        # active_stages == [] means the quest hasn't started.
        # if we're completing a non-active stage, it had better
        # be to start a quest
        else:
            assert self.active_stages == []

        self.is_complete = stage.completes_quest
        self.completed_stages += [stage]
        self.active_stages += stage.next_stages

        if stage.on_complete is not None:
            stage.on_complete()
    
    def stage_active(self, stage):
        return stage in self.active_stages

    def stage_completed(self, stage):
        return stage in self.completed_stages

class Stage:
    # Args: desc: Brief description of this stage
    #  on_complete: function to call when it's completed
    #  completes_quest: whether the quest is finished when the stage completes
    #  next_stages: stages that become active when this one completes.
    def __init__(self, desc, next_stages=[], completes_quest=False, on_complete=None):
        self.desc = desc
        self.on_complete = on_complete
        self.completes_quest = completes_quest
        self.next_stages = next_stages

# The piano quest (note: stages are defined in reverse order so the next stage is already
# defined when we refer to it)
piano_install_amp = Stage("Install the piano amplifier", [], True)
piano_give_ashes = Stage("Return the ashes to lewd soloist", [piano_install_amp])
piano_defeat_hipster = Stage("Defeat the hipster in Tazza D'oro", [piano_give_ashes])
piano_start = Stage("Talk to the soloist about getting revenge", [piano_defeat_hipster])

quest_piano = Quest("Piano Sabotage",
                [piano_start,
                 piano_defeat_hipster,
                 piano_give_ashes,
                 piano_install_amp])

# The Zoey quest
zoey_finish = Stage("Talk to Zoey again about Javier", [], True)
zoey_drink = Stage("Get Zoey drunk", [zoey_finish])
zoey_booze = Stage("Find some alcohol", [zoey_drink])
zoey_give_evidence = Stage("Return the evidence to Zoey", [zoey_booze])
zoey_evidence = Stage("Find the evidence of Jerkface's betrayal", [zoey_give_evidence])
zoey_talk = Stage("Talk to Zoey about dating Javier", [zoey_evidence])
quest_zoey = Quest("Zoey's Love", [zoey_talk, 
                                   zoey_evidence, 
                                   zoey_give_evidence, 
                                   zoey_booze, 
                                   zoey_drink, 
                                   zoey_finish])

quests = [quest_piano, quest_zoey]

# The quests that have already been completed
def complete_quests():
    return list(filter(lambda quest: quest.is_complete, quests))

# The quests that are in progress
def active_quests():
    return list(filter(lambda quest: len(quest.active_stages) > 0 and not quest.is_complete, quests))

# Display information about quest progress
def print_quests():
    active = active_quests()
    complete = complete_quests()
    
    print("Revenge Progress: " + str(len(complete)) + "/" + str(len(quests)))

    if len(active) == 0:
        print("You have no active quest! Get one!")
    else:
        print("Active Quests:")
        for quest in active:
            print("  Quest: " + quest.name)
            for stage in quest.completed_stages:
                print("    " + stage.desc + " (Done)")
            for stage in quest.active_stages:
                print("    " + stage.desc)
    print()

    if len(complete) == 0:
        print("You have no completed quests. Are you a lazy Mexican like Javier?")
    else:
        print("Completed Quests:")
        for quest in complete:
            print(quest.name)
