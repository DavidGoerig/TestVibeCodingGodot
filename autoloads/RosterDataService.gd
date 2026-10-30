extends Node

var classes_data: Array = []
var elements_data: Array = []
var reactions_data: Array = []
var synergies_data: Array = []
var champion_template: Dictionary = {}
var generation_rules: Dictionary = {}

func _ready() -> void:
    load_all_data()

func load_all_data() -> void:
    classes_data = load_json("res://data/classes.json")
    elements_data = load_json("res://data/elements.json")
    reactions_data = load_json("res://data/reactions.json")
    synergies_data = load_json("res://data/synergies.json")
    champion_template = load_json("res://data/champion_template.json")
    generation_rules = load_json("res://data/generation_rules.json")

func load_json(path: String) -> Variant:
    var file := FileAccess.open(path, FileAccess.READ)
    if file == null:
        push_error("Could not open JSON file: %s" % path)
        return [] if path.ends_with(".json") else {}
    var text := file.get_as_text()
    file.close()
    var parsed = JSON.parse_string(text)
    if parsed == null:
        push_error("JSON parse failed: %s" % path)
        return [] if path.ends_with(".json") else {}
    return parsed

func get_class_count() -> int:
    return classes_data.size()

func get_element_count() -> int:
    return elements_data.size()

func get_by_id(data: Array, id: String) -> Dictionary:
    for item in data:
        if item.get("id") == id:
            return item
    return {}

func make_internal_synergy_summary(element_data: Dictionary) -> Dictionary:
    return {
        "theme": element_data.get("team_synergy_theme", "general"),
        "internal_synergy": element_data.get("internal_synergy", "no specific synergy"),
        "signature_gameplay": element_data.get("signature_gameplay", "generic"),
        "combo_signature": element_data.get("combo_signature", "generic")
    }

func same_element_bonus(class_data: Dictionary, element_data: Dictionary) -> Dictionary:
    var theme = element_data.get("team_synergy_theme", "general")
    var class_name = class_data.get("name", "Champion")
    var role_primary = class_data.get("role_primary", "support")
    var terrain_hint = class_data.get("terrain_mechanics", ["alters terrain"]).front()
    if terrain_hint == null:
        terrain_hint = "alters terrain"

    return {
        "trigger": "same_element_ally_bonus",
        "theme": theme,
        "description": element_data.get("internal_synergy", "adds tactical cohesion to the whole team"),
        "class_focus": "%s specializes in %s" % [class_name, role_primary],
        "terrain_hint": terrain_hint,
        "signature_gameplay": element_data.get("signature_gameplay", "generic")
    }

func build_passives(class_data: Dictionary, element_data: Dictionary) -> Dictionary:
    var terrain_list = class_data.get("terrain_mechanics", ["alters terrain"])
    var terrain_first = terrain_list[0] if terrain_list.size() > 0 else "alters terrain"

    return {
        "class_passive": "%s turns %s into a decisive advantage" % [class_data.get("name", "Champion"), terrain_first],
        "element_passive": element_data.get("internal_synergy", "adds tactical cohesion"),
        "terrain_interaction": "%s + %s" % [terrain_first, element_data.get("terrain_modified", ["terrain"]).front()]
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

    var element_bonus_rate = 1.0
    if element_data.get("id", "normal") == "fire" or element_data.get("id", "normal") == "electric" or element_data.get("id", "normal") == "shadow":
        element_bonus_rate = 1.1

    return {
        "pv": pv,
        "pa": pa,
        "pm": pm,
        "initiative": initiative,
        "dmg_phys": int(dmg_phys * element_bonus_rate),
        "dmg_elem": int(dmg_elem * element_bonus_rate),
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

    var synergy_summary = make_internal_synergy_summary(element_data)
    var passives = build_passives(class_data, element_data)
    var element_bonus = same_element_bonus(class_data, element_data)
    var base_stats = build_base_stats(class_data, element_data)
    var skills = build_skill_set(class_data, element_data)

    var champion = {
        "id": "pur_" + class_id + "_" + element_id,
        "name": class_data.get("name", "Unknown") + " • " + element_data.get("name", "Unknown"),
        "rarity": "common",
        "class_id": class_id,
        "primary_element": element_id,
        "secondary_element": null,
        "is_hybrid": false,
        "archetype_group": class_data.get("group", "general"),
        "role_primary": class_data.get("role_primary", "unknown"),
        "role_secondary": class_data.get("role_secondary", "unknown"),
        "terrain_mechanics": class_data.get("terrain_mechanics", []),
        "movement": class_data.get("movement", "standard"),
        "control": class_data.get("control", "none"),
        "element_control": element_data.get("control", ""),
        "unique_gameplay": element_data.get("signature_gameplay", "generic"),
        "internal_synergy": synergy_summary["internal_synergy"],
        "team_synergy_theme": synergy_summary["theme"],
        "combo_signature": synergy_summary["combo_signature"],
        "signature_combo": synergy_summary["combo_signature"],
        "strengths": class_data.get("strengths", []),
        "weaknesses": class_data.get("weaknesses", []) + element_data.get("weaknesses", []),
        "passives": passives,
        "same_element_bonus": element_bonus,
        "base_stats": base_stats,
        "skills": skills,
        "synergies": [synergy_summary["theme"], element_data.get("id", "general")],
        "tag_lines": [
            class_data.get("name", "Champion"),
            element_data.get("name", "Element"),
            synergy_summary["theme"]
        ]
    }

    var validation = validate_champion(champion)
    champion["validation"] = validation
    return champion

func generate_monolithes() -> Array:
    var roster: Array = []
    for class_item in classes_data:
        for element_item in elements_data:
            var champion = generate_pur_champion(class_item.get("id"), element_item.get("id"))
            if not champion.is_empty() and champion.get("validation", {}).get("valid", false):
                roster.append(champion)
    return roster

func generate_hybrid_pair(a_element_id: String, b_element_id: String) -> Dictionary:
    if a_element_id == b_element_id:
        return {}

    var element_a = get_by_id(elements_data, a_element_id)
    var element_b = get_by_id(elements_data, b_element_id)

    if element_a.is_empty() or element_b.is_empty():
        return {}

    var pair_key = a_element_id + "_" + b_element_id
    var pair_desc = "" + element_a.get("name", "") + " + " + element_b.get("name", "")
    var hybrid_theme = "hybrid_" + element_a.get("team_synergy_theme", "mixed") + "_" + element_b.get("team_synergy_theme", "mixed")

    var hybrid = {
        "id": "hyb_" + pair_key,
        "name": pair_desc,
        "primary_element": a_element_id,
        "secondary_element": b_element_id,
        "is_hybrid": true,
        "team_synergy_theme": hybrid_theme,
        "unique_gameplay": element_a.get("signature_gameplay", "mixed") + " + " + element_b.get("signature_gameplay", "mixed"),
        "internal_synergy": element_a.get("internal_synergy", "") + " / " + element_b.get("internal_synergy", ""),
        "signature_combo": element_a.get("combo_signature", "") + " + " + element_b.get("combo_signature", ""),
        "passives": {
            "class_passive": "combo_pressure",
            "element_passive": element_a.get("internal_synergy", "") + " and " + element_b.get("internal_synergy", ""),
            "terrain_interaction": element_a.get("terrain_modified", ["terrain"]).front() + " + " + element_b.get("terrain_modified", ["terrain"]).front()
        },
        "same_element_bonus": {
            "trigger": "pair_synergy_bonus",
            "theme": hybrid_theme,
            "description": "The pair transforms the terrain into a layered tactical trigger zone."
        }
    }

    hybrid["validation"] = validate_champion(hybrid)
    return hybrid

func generate_hybrids() -> Array:
    var roster: Array = []
    for i in range(elements_data.size()):
        for j in range(i + 1, elements_data.size()):
            var a = elements_data[i].get("id")
            var b = elements_data[j].get("id")
            var hybrid = generate_hybrid_pair(a, b)
            if not hybrid.is_empty() and hybrid.get("validation", {}).get("valid", false):
                roster.append(hybrid)
    return roster

func generate_full_roster() -> Dictionary:
    var monolithes = generate_monolithes()
    var hybrids = generate_hybrids()
    return {
        "monolithes": monolithes,
        "hybrids": hybrids,
        "stats": {
            "monolithes_total": monolithes.size(),
            "hybrids_total": hybrids.size(),
            "overall_total": monolithes.size() + hybrids.size()
        }
    }
