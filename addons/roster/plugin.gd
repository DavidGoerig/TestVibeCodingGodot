@tool
extends EditorPlugin

func _enter_tree() -> void:
    print("RosterBuilder plugin loaded")

func _exit_tree() -> void:
    print("RosterBuilder plugin unloaded")
