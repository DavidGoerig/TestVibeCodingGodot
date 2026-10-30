extends Node

# Godot-ready roster builder with deliberate drafting rules.
# It keeps the generation data-driven while enforcing the same-element synergy
# and unique gameplay constraints required for tactical roster design.

var classes_data: Array = []
var elements_data: Array = []
var reactions_data: Array = []
var champion_template: Dictionary = {}

func _ready() -> void:
    load_data()
    print("Roster builder ready.")

func load_data() -> void:
    classes_data = load_json("res://data/classes.json")
    elements_data = load_json("res://data/elements.json")
    reactions_data = load_json("res://data/reactions.json")
    champion_template = load_json("res://data/champion_template.json")

func load_json(path: String) -> Variant:
    var file := FileAccess.open(path, FileAccess.READ)
    if file == null:
        push_error("Could not open JSON: %s" % path)
        return [] if path.ends_with(".json") else {}
    var content := file.get_as_text()
    file.close()
    return JSON.parse_string(content)

func get_by_id(data: Array, id: String) -> Dictionary:
    for item in data:
        if item.get("id") == id:
            return item
    return {}

func same_element_bonus(class_data: Dictionary, element_data: Dictionary) -> Dictionary:
    return {
        "trigger": "same_element_ally_bonus",
        "theme": element_data.get("team_synergy_theme", "general"),
        "description": element_data.get("internal_synergy", "binds the team around a shared terrain plan"),
        "class_focus": class_data.get("role_primary", "support"),
        "signature_gameplay": element_data.get("signature_gameplay", "generic")
    }

func build_passives(class_data: Dictionary, element_data: Dictionary) -> Dictionary:
    var terrain_hint = class_data.get("terrain_mechanics", ["alters terrain"]).front()
    if terrain_hint == null:
        terrain_hint = "alters terrain"
    return {
        "class_passive": "%s thrives on %s" % [class_data.get("name", "Champion"), terrain_hint],
        "element_passive": element_data.get("internal_synergy", "creates a shared battlefield identity"),
        "terrain_interaction": "%s + %s" % [terrain_hint, element_data.get("terrain_modified", ["terrain"]).front()]
    }

func build_base_stats(class_data: Dictionary, element_data: Dictionary) -> Dictionary:
    var group = class_data.get("group", "general")
    var role = class_data.get("role_primary", "support")
    var pv := 1000
    var pa := 8
    var pm := 4
    var initiative := 1000
    var dmg_phys := 100
    var dmg_elem := 100
    var tacle := 100
    var crit := 5

    if group == "heavy":
        pv = 1250
        dmg_phys = 130
        tacle = 120
    elif group == "agile":
        pv = 900
        pm = 5
        initiative = 1100
        dmg_phys = 110
        crit = 10
    elif group == "flux":
        pv = 980
        pa = 9
        dmg_elem = 130
        initiative = 1050
    elif group == "link":
        pv = 1050
        pa = 8
        dmg_elem = 120
    elif group == "engineering":
        pv = 1100
        dmg_elem = 115
        tacle = 110

    if role.find("tank") != -1 or role == "guardian":
        pv += 150
        dmg_phys += 10
    if role.find("assassin") != -1 or role == "skirmisher_vertical":
        pm += 1
        initiative += 100
    if role.find("mage") != -1 or role.find("zone") != -1:
        dmg_elem += 30
        pa += 1

    return {
        "pv": pv,
        "pa": pa,
        "pm": pm,
        "initiative": initiative,
        "dmg_phys": dmg_phys,
        "dmg_elem": dmg_elem,
        "tacle": tacle,
        "crit": crit
    }

func build_skill_set(class_data: Dictionary, element_data: Dictionary) -> Array:
    var class_name = class_data.get("name", "Champion")
    var element_id = element_data.get("id", "normal")
    var element_name = element_data.get("name", "Element")
    var terrain_hint = class_data.get("terrain_mechanics", ["alters terrain"]).front()
    if terrain_hint == null:
        terrain_hint = "alters terrain"

    var element_keywords = {
        "fire": ["Brasier", "Cendre", "Flamme", "Fournaise", "Pyro"],
        "water": ["Flux", "Vague", "Courant", "Source", "Tide"],
        "electric": ["Étincelle", "Circuit", "Foudre", "Arc", "Charge"],
        "grass": ["Verdure", "Racine", "Feuille", "Croissance", "Vigne"],
        "ice": ["Givre", "Cristal", "Glace", "Souffle", "Prisme"],
        "ground": ["Dune", "Roche", "Mur", "Terre", "Élévation"],
        "flying": ["Vent", "Vitesse", "Altitude", "Courant", "Aile"],
        "poison": ["Toxine", "Nuit", "Miasme", "Pourriture", "Sève"],
        "psychic": ["Distorsion", "Onde", "Portail", "Illusion", "Rêve"],
        "metal": ["Acier", "Masses", "Lame", "Forge", "Magnétisme"],
        "shadow": ["Ombre", "Silence", "Blindage", "Vortex", "Nuit"],
        "normal": ["Tactique", "Support", "Adaptation", "État", "Équilibre"]
    }

    var keyword_pool = element_keywords.get(element_id, ["Tactique", "Support", "Adaptation", "État", "Équilibre"])
    var skill_names = [
        "%s de %s" % [class_name, element_name],
        "%s %s" % [keyword_pool[0], class_name],
        "Ligne de %s" % [keyword_pool[1]],
        "Marque de %s" % [terrain_hint],
        "%s de l'ombre" % [keyword_pool[2]],
        "%s de rupture" % [keyword_pool[3]],
        "Zone %s" % [keyword_pool[4]],
        "Courant de %s" % [element_name],
        "Pression %s" % [element_name],
        "Finale %s" % [element_name]
    ]

    var ranges = ["melee", "melee", "medium", "medium", "self", "line", "zone", "long", "medium", "long"]
    var aoes = ["single", "single", "zone", "line", "self", "line", "burst", "single", "cone", "burst"]
    var targets = ["unit_or_tile", "unit_or_tile", "tile_area", "tile_area", "self", "unit_or_tile", "tile_area", "unit_or_tile", "unit_or_tile", "tile_area"]
    var effect_tags_base = [
        class_data.get("role_primary", "support"),
        element_data.get("reaction_primary", "adaptation"),
        "terrain",
        element_data.get("control", "zone_control"),
        "mobility",
        "interrupt",
        "zone_control",
        "burst",
        "reposition",
        "finisher"
    ]

    var skills: Array = []
    for slot in range(1, 11):
        var base_tags = []
        base_tags.append(effect_tags_base[slot - 1])
        if slot >= 2:
            base_tags.append(element_data.get("signature_gameplay", "generic"))
        skills.append({
            "slot": slot,
            "name": skill_names[slot - 1],
            "cost": 1 + (slot / 3),
            "range": ranges[slot - 1],
            "aoe": aoes[slot - 1],
            "target": targets[slot - 1],
            "effect_tags": base_tags,
            "description": "%s applique son thème %s sur le champ de bataille." % [class_name, element_data.get("team_synergy_theme", "combat_theme")]
        })
    return skills

func validate_champion(champion: Dictionary) -> Dictionary:
    var issues: Array = []
    if champion.get("role_primary", "") == "":
        issues.append("missing_role")
    if champion.get("signature_combo", "") == "":
        issues.append("missing_signature_combo")
    if champion.get("same_element_bonus", {}).get("description", "") == "":
        issues.append("missing_same_element_bonus")
    if champion.get("weaknesses", []).is_empty():
        issues.append("missing_weaknesses")
    if champion.get("passives", {}).get("terrain_interaction", "") == "":
        issues.append("missing_terrain_interaction")
    if champion.get("base_stats", {}).is_empty():
        issues.append("missing_base_stats")
    if champion.get("skills", []).size() < 10:
        issues.append("missing_skill_set")

    return {
        "valid": issues.is_empty(),
        "issues": issues,
        "score": clamp(6 - issues.size(), 0, 6)
    }

func generate_pur_champion(class_id: String, element_id: String) -> Dictionary:
    var class_data = get_by_id(classes_data, class_id)
    var element_data = get_by_id(elements_data, element_id)

    if class_data.is_empty() or element_data.is_empty():
        push_error("Unknown class or element: %s / %s" % [class_id, element_id])
        return {}

    var champion = {
        "class_id": class_id,
        "primary_element": element_id,
        "secondary_element": null,
        "is_hybrid": false,
        "role_primary": class_data.get("role_primary", "unknown"),
        "role_secondary": class_data.get("role_secondary", "unknown"),
        "terrain_mechanics": class_data.get("terrain_mechanics", []),
        "element_control": element_data.get("control", ""),
        "signature_combo": element_data.get("combo_signature", "generic"),
        "unique_gameplay": element_data.get("signature_gameplay", "generic"),
        "team_synergy_theme": element_data.get("team_synergy_theme", "general"),
        "internal_synergy": element_data.get("internal_synergy", "general cohesion"),
        "weaknesses": class_data.get("weaknesses", []) + element_data.get("weaknesses", []),
        "same_element_bonus": same_element_bonus(class_data, element_data),
        "passives": build_passives(class_data, element_data),
        "base_stats": build_base_stats(class_data, element_data),
        "skills": build_skill_set(class_data, element_data),
    }

    champion["validation"] = validate_champion(champion)
    return champion
