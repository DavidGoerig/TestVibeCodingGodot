extends Node

func _ready() -> void:
    print("Roster prototype started")
    var roster = RosterDataService
    if roster:
        print("Loaded classes: ", roster.get_class_count())
        print("Loaded elements: ", roster.get_element_count())
        var sample = roster.generate_pur_champion("briseur", "fire")
        print("Sample champion: ", sample)
