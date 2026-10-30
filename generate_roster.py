from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"

TOP_HYBRID_PAIRS = [
    ("fire", "water"),
    ("water", "electric"),
    ("water", "ice"),
    ("ground", "fire"),
    ("poison", "fire"),
    ("shadow", "poison"),
    ("metal", "electric"),
    ("psychic", "flying"),
    ("ground", "ice"),
    ("metal", "ground"),
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_by_id(items, item_id):
    for item in items:
        if item.get("id") == item_id:
            return item
    return {}


def champion_name(class_data, element_data):
    class_name = class_data["name"]
    element_name = element_data["name"]
    titles = {
        "fire": "du Brasier",
        "water": "du Flux",
        "electric": "de l'Éclair",
        "grass": "de la Verdure",
        "ice": "du Givre",
        "ground": "de la Terre",
        "flying": "du Vent",
        "poison": "du Venin",
        "psychic": "de la Distorsion",
        "metal": "d'Acier",
        "shadow": "de l'Ombre",
        "normal": "du Terrain",
        "dragon": "du Dragon",
        "fairy": "de la Fée",
        "ghost": "du Spectre",
        "rock": "de la Roche",
        "bug": "des Insectes",
        "fighting": "du Combat",
        "steel": "d'Acier"
    }
    suffix = titles.get(element_data.get("id", "normal"), "du Terrain")
    return f"{class_name} {suffix}"


def get_same_element_bonus(element_data):
    element_id = element_data.get("id", "normal")
    bonuses = {
        "normal": "turns any improvised object into a tactical pivot that keeps the team in control of the map.",
        "fire": "creates a burning front that amplifies ally burst damage and pressures the whole lane.",
        "water": "floods every connected route, letting allies slide, redirect, and keep pressure on the lane.",
        "electric": "links allies into a conductive chain, turning every nearby strike into a burst of voltage.",
        "grass": "grows living cover that heals and denies vision, turning the team into a relentless wall.",
        "ice": "locks the battlefield into rigid lanes, turning every ally into a geometry controller.",
        "ground": "raises the terrain beneath allies, granting cover, height advantage and crushing counter-pressure.",
        "flying": "opens unpredictable air lanes, letting allies reposition and control flanks from elevation.",
        "poison": "turns the whole zone into a lingering danger field that punishes every step and heal.",
        "psychic": "breaks enemy lines of sight and shifts positional logic, making every ally harder to read.",
        "metal": "fortifies the team into a dense shield wall that absorbs pressure and answers with impact.",
        "shadow": "hides the team in blind zones and amplifies flanks, ambushes and forced trades.",
        "dragon": "fills the battlefield with rage zones that reward aggressive sequencing but ban defensive casting.",
        "fairy": "wraps the squad in mystic mist and shields it from status effects while reducing physical damage taken.",
        "ghost": "lets the team ignore physical barriers and apply condemnation clocks to vulnerable enemies.",
        "rock": "builds pillars and rubble walls that seal sight-lines and narrow passages.",
        "bug": "anchors enemies in web zones and keeps pressure alive through swarm harassment.",
        "fighting": "converts positioning into impact, sending targets into walls, ledges, or crater zones.",
        "steel": "adds dense armor plating and magnetic counter-pressure against electric threats.",
    }
    return bonuses.get(element_id, bonuses["normal"])


def get_pair_synergy(element_a, element_b):
    a_id = element_a.get("id", "normal")
    b_id = element_b.get("id", "normal")
    pair_key = (a_id, b_id)
    reverse_key = (b_id, a_id)
    pairs = {
        ("fire", "water"): {
            "result": "steam_lattice",
            "terrain": "steam vents, vapor walls and blocked sight-lines",
            "description": "Steam and fire turn the lane into a blinding pressure corridor that locks vision and amplifies burst damage.",
            "combo_name": "Vapeur en fusion"},
        ("water", "electric"): {
            "result": "conductive_flood",
            "terrain": "charged puddles and electrified paths",
            "description": "The flood becomes a live conduit that chains current across the battlefield and punishes grouped enemies.",
            "combo_name": "Rivière de courant"},
        ("water", "ice"): {
            "result": "frozen_river",
            "terrain": "glacial lanes, bridges and frozen cutoffs",
            "description": "A flooded route freezes into a brutal choke point that locks movement and punishes forced advances.",
            "combo_name": "Ligne gelée"},
        ("ground", "fire"): {
            "result": "magma_trench",
            "terrain": "smoking cracks, magma ridges and collapsing stone",
            "description": "The earth turns molten under pressure, creating brutal collision zones and crushing line breaks.",
            "combo_name": "Tranchée de magma"},
        ("poison", "fire"): {
            "result": "toxic_burst",
            "terrain": "acidic ash, toxic fire and toxic smoke",
            "description": "Fire superheats poison into a rolling toxic blast that corrupts cover and punishes every step.",
            "combo_name": "Brasier empoisonné"},
        ("shadow", "poison"): {
            "result": "black_miasma",
            "terrain": "black cloud, hidden decay and blind toxic zones",
            "description": "The black mist hides the poison and turns the map into a foggy death trap that breaks attention and control.",
            "combo_name": "Miasme noir"},
        ("metal", "electric"): {
            "result": "magnetic_arc",
            "terrain": "metal rails, magnetic barriers and chained shocks",
            "description": "Metal turns current into a rail of destruction, creating huge burst windows and impossible lane control.",
            "combo_name": "Rail magnétique"},
        ("psychic", "flying"): {
            "result": "sky_distortion",
            "terrain": "warped air lanes, height flips and deceptive openings",
            "description": "Psychic distortion and wind create impossible positions, bending both terrain and sight around the target.",
            "combo_name": "Saut de ciel"},
        ("fire", "grass"): {
            "result": "burning_forest",
            "terrain": "burning roots, living fire and blinding heat",
            "description": "Plant growth and fire create a wild wall of heat that floods the field and leaves no safe lane.",
            "combo_name": "Forêt en feu"},
        ("ground", "ice"): {
            "result": "crystalline_ridge",
            "terrain": "glass ridges, frozen pillars and hard chokes",
            "description": "Ground and ice create a brutal ridge of control where every step becomes a tactical gamble.",
            "combo_name": "Crête cristalline"},
        ("shadow", "fire"): {
            "result": "smoke_blaze",
            "terrain": "smoke firewalls, obscured angles and flare zones",
            "description": "Shadow hides the blaze, creating blind-hot zones where enemies are attacked before they can react.",
            "combo_name": "Feu aveuglant"},
        ("metal", "ground"): {
            "result": "fortress_weight",
            "terrain": "reinforced ridges, broken fortifications and crushing walls",
            "description": "The duo turns the battlefield into a heavy fortress where every step is a threat and every wall is a weapon.",
            "combo_name": "Forteresse lourde"},
    }
    if pair_key in pairs:
        return pairs[pair_key]
    if reverse_key in pairs:
        return pairs[reverse_key]

    primary = element_a.get("signature_gameplay", "terrain")
    secondary = element_b.get("signature_gameplay", "terrain")
    return {
        "result": f"{a_id}_{b_id}_field",
        "terrain": f"mixed {a_id} and {b_id} control zones",
        "description": f"{primary} and {secondary} merge to create a brutal pressure lane that bends the battlefield around the target.",
        "combo_name": f"Rupture {element_a.get('name', a_id)}"
    }


def build_skill_bible(class_data, element_data):
    element_id = element_data.get("id", "normal")
    class_name = class_data.get("name", "Champion")
    slot_patterns = [
        {"name": "Impact direct", "effect_type": "single_hit", "map_impact": "damage_on_target", "control": "burst"},
        {"name": "Ligne de terrain", "effect_type": "line_pressure", "map_impact": "tile_reaction", "control": "lane_control"},
        {"name": "Zone de contrôle", "effect_type": "zone_field", "map_impact": "area_lock", "control": "zone_control"},
        {"name": "Mutation du sol", "effect_type": "terrain_transform", "map_impact": "tile_change", "control": "map_control"},
        {"name": "Bouclier local", "effect_type": "buff_self", "map_impact": "safe_zone", "control": "self_stability"},
        {"name": "Onde de choc", "effect_type": "wave_push", "map_impact": "route_disruption", "control": "push"},
        {"name": "Blocage de route", "effect_type": "route_lock", "map_impact": "path_block", "control": "movement_control"},
        {"name": "Chaîne / réseau", "effect_type": "chain_link", "map_impact": "multi_target", "control": "chain_control"},
        {"name": "Explosion composite", "effect_type": "burst_combo", "map_impact": "explosive_zone", "control": "burst"},
        {"name": "Fin de séquence", "effect_type": "finisher", "map_impact": "decisive_zone", "control": "finisher"},
    ]

    if element_id == "fire":
        slot_patterns[0]["name"] = "Impact enflammé"
        slot_patterns[1]["name"] = "Ligne de feu"
        slot_patterns[2]["name"] = "Brasier de zone"
        slot_patterns[3]["name"] = "Mutation en cendre"
        slot_patterns[4]["name"] = "Régénération brûlante"
        slot_patterns[5]["name"] = "Onde de flammes"
        slot_patterns[6]["name"] = "Route coupée"
        slot_patterns[7]["name"] = "Réseau de chaleur"
        slot_patterns[8]["name"] = "Explosion de foyer"
        slot_patterns[9]["name"] = "Fin du brasier"
    elif element_id == "water":
        slot_patterns[0]["name"] = "Impact aquatique"
        slot_patterns[1]["name"] = "Courant de ligne"
        slot_patterns[2]["name"] = "Zone de coulée"
        slot_patterns[3]["name"] = "Route inondée"
        slot_patterns[4]["name"] = "Protection liquide"
        slot_patterns[5]["name"] = "Onde de flux"
        slot_patterns[6]["name"] = "Détour forcé"
        slot_patterns[7]["name"] = "Chaîne hydrique"
        slot_patterns[8]["name"] = "Déluge composite"
        slot_patterns[9]["name"] = "Fin du flux"
    elif element_id == "electric":
        slot_patterns[0]["name"] = "Impact foudroyant"
        slot_patterns[1]["name"] = "Arc de ligne"
        slot_patterns[2]["name"] = "Circuit de zone"
        slot_patterns[3]["name"] = "Sol chargé"
        slot_patterns[4]["name"] = "Écran électrique"
        slot_patterns[5]["name"] = "Onde de courant"
        slot_patterns[6]["name"] = "Barrière conductrice"
        slot_patterns[7]["name"] = "Liaison en série"
        slot_patterns[8]["name"] = "Tempête de décharge"
        slot_patterns[9]["name"] = "Fin du circuit"
    elif element_id == "grass":
        slot_patterns[0]["name"] = "Impact enraciné"
        slot_patterns[1]["name"] = "Ligne de lianes"
        slot_patterns[2]["name"] = "Verdure de zone"
        slot_patterns[3]["name"] = "Terre vivante"
        slot_patterns[4]["name"] = "Garde de couvert"
        slot_patterns[5]["name"] = "Vague de sève"
        slot_patterns[6]["name"] = "Voie bouclée"
        slot_patterns[7]["name"] = "Réseau racinaire"
        slot_patterns[8]["name"] = "Explosion verte"
        slot_patterns[9]["name"] = "Fin de la sève"
    elif element_id == "ice":
        slot_patterns[0]["name"] = "Impact glacé"
        slot_patterns[1]["name"] = "Ligne de givre"
        slot_patterns[2]["name"] = "Aire gelée"
        slot_patterns[3]["name"] = "Mur de glace"
        slot_patterns[4]["name"] = "Parade de glace"
        slot_patterns[5]["name"] = "Onde de froid"
        slot_patterns[6]["name"] = "Passage figé"
        slot_patterns[7]["name"] = "Chaîne du gel"
        slot_patterns[8]["name"] = "Explosion de givre"
        slot_patterns[9]["name"] = "Fin du gel"
    elif element_id == "ground":
        slot_patterns[0]["name"] = "Impact de terre"
        slot_patterns[1]["name"] = "Ligne de dune"
        slot_patterns[2]["name"] = "Zone de sol"
        slot_patterns[3]["name"] = "Levée de mur"
        slot_patterns[4]["name"] = "Fortification de pierre"
        slot_patterns[5]["name"] = "Onde de secousse"
        slot_patterns[6]["name"] = "Tranchée fermée"
        slot_patterns[7]["name"] = "Chaîne de gravité"
        slot_patterns[8]["name"] = "Explosion de terre"
        slot_patterns[9]["name"] = "Fin du sol"
    elif element_id == "flying":
        slot_patterns[0]["name"] = "Impact aérien"
        slot_patterns[1]["name"] = "Ligne de vent"
        slot_patterns[2]["name"] = "Courant de zone"
        slot_patterns[3]["name"] = "Altitude modifiée"
        slot_patterns[4]["name"] = "Vol défensif"
        slot_patterns[5]["name"] = "Onde de souffle"
        slot_patterns[6]["name"] = "Angle ouvert"
        slot_patterns[7]["name"] = "Réseau de vent"
        slot_patterns[8]["name"] = "Tempête aérienne"
        slot_patterns[9]["name"] = "Fin du courant"
    elif element_id == "poison":
        slot_patterns[0]["name"] = "Impact toxique"
        slot_patterns[1]["name"] = "Ligne de miasmes"
        slot_patterns[2]["name"] = "Zone putride"
        slot_patterns[3]["name"] = "Terrain corrompu"
        slot_patterns[4]["name"] = "Garde empoisonnée"
        slot_patterns[5]["name"] = "Onde de poison"
        slot_patterns[6]["name"] = "Voie empoisonnée"
        slot_patterns[7]["name"] = "Réseau de spores"
        slot_patterns[8]["name"] = "Explosion toxique"
        slot_patterns[9]["name"] = "Fin du venin"
    elif element_id == "psychic":
        slot_patterns[0]["name"] = "Impact mental"
        slot_patterns[1]["name"] = "Ligne de distorsion"
        slot_patterns[2]["name"] = "Zone déformée"
        slot_patterns[3]["name"] = "Espace altéré"
        slot_patterns[4]["name"] = "Bouclier mental"
        slot_patterns[5]["name"] = "Onde psychique"
        slot_patterns[6]["name"] = "Visibilité cassée"
        slot_patterns[7]["name"] = "Chaîne de pensée"
        slot_patterns[8]["name"] = "Explosion mentale"
        slot_patterns[9]["name"] = "Fin de la distorsion"
    elif element_id == "metal":
        slot_patterns[0]["name"] = "Impact d'acier"
        slot_patterns[1]["name"] = "Ligne de débris"
        slot_patterns[2]["name"] = "Zone de blindage"
        slot_patterns[3]["name"] = "Mur de métal"
        slot_patterns[4]["name"] = "Renfort de fer"
        slot_patterns[5]["name"] = "Onde de marteau"
        slot_patterns[6]["name"] = "Route verrouillée"
        slot_patterns[7]["name"] = "Chaîne de massue"
        slot_patterns[8]["name"] = "Explosion d'acier"
        slot_patterns[9]["name"] = "Fin de l'armure"
    elif element_id == "shadow":
        slot_patterns[0]["name"] = "Impact noir"
        slot_patterns[1]["name"] = "Ligne d'ombre"
        slot_patterns[2]["name"] = "Zone obscure"
        slot_patterns[3]["name"] = "Terrain masqué"
        slot_patterns[4]["name"] = "Silence et flanc"
        slot_patterns[5]["name"] = "Onde de nuit"
        slot_patterns[6]["name"] = "Voie cachée"
        slot_patterns[7]["name"] = "Réseau obscur"
        slot_patterns[8]["name"] = "Explosion de nuit"
        slot_patterns[9]["name"] = "Fin de l'ombre"
    else:
        slot_patterns[0]["name"] = f"Impact {class_name}"

    for slot_index, pattern in enumerate(slot_patterns, start=1):
        pattern["slot"] = slot_index
        pattern["element_id"] = element_id
        pattern["class_id"] = class_data.get("id", "unknown")
        pattern["description"] = f"{class_name} exploite le schéma {pattern['name']} pour manipuler le terrain et contrôler la ligne de combat."
    return slot_patterns


def build_skill_set(class_data, element_data):
    element_id = element_data.get("id", "normal")
    element_name = element_data.get("name", "Terrain")
    class_name = class_data.get("name", "Champion")

    element_keywords = {
        "normal": ["Tactique", "Support", "Adaptation", "État", "Équilibre"],
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
        "dragon": ["Colère", "Fureur", "Énergie", "Rage", "Draconique"],
        "fairy": ["Brume", "Garde", "Éveil", "Lueur", "Merveille"],
        "ghost": ["Spectre", "Écho", "Linceul", "Phantom", "Condamnation"],
        "rock": ["Pierre", "Pilier", "Éboulement", "Fortification", "Mur"],
        "bug": ["Toile", "Essaim", "Harcèlement", "Ancrage", "Réseau"],
        "fighting": ["Impact", "Projection", "Choc", "Masse", "Slam"],
        "steel": ["Acier", "Armure", "Chaîne", "Magnétisme", "Forge"]
    }

    element_profiles = {
        "normal": {
            "verb": "réarrange",
            "terrain": "décale les blocs, les caisses et les barricades pour ouvrir un angle ou un passage",
            "damage": "40-70 dégâts physiques",
            "dot": "improvisation",
            "zone": "terrain improvisé",
            "actions": ["déplace un bloc ou une caisse", "ouvre une ligne de tir avec un objet", "transforme un objet en couverture de secours", "réoriente une barricade", "crée une ouverture de fuite"]
        },
        "fire": {
            "verb": "embrase",
            "terrain": "allume les blocs, la végétation et les objets en une zone brûlante",
            "damage": "60-90 dégâts de feu",
            "dot": "brûlure sur 2 tours",
            "zone": "brasier",
            "actions": ["allume un mur de bois", "provoque un feu de zone", "déclenche une chaîne d'ignition", "fait exploser de la végétation sèche", "crée un brasier qui chasse les ennemis"]
        },
        "water": {
            "verb": "inonde",
            "terrain": "mouille le sol, crée un courant et transforme les routes en zones liquides",
            "damage": "45-75 dégâts d'eau",
            "dot": "ralentissement",
            "zone": "courant",
            "actions": ["inonde une voie", "mouillé la zone pour ralentir les ennemis", "fait passer une route en zone glissante", "force un détour par la pluie", "renforce une zone de soutien par l'eau"]
        },
        "electric": {
            "verb": "électrifie",
            "terrain": "charge les blocs et propage des arcs entre plusieurs cibles sur la zone",
            "damage": "55-95 dégâts électriques",
            "dot": "étourdissement",
            "zone": "circuit",
            "actions": ["relie plusieurs cibles", "provoque un arc sur une route humide", "charge une zone de sol", "active un circuit de courant", "crée une décharge sur un groupe"]
        },
        "grass": {
            "verb": "enracine",
            "terrain": "fait pousser racines, buissons et couvert végétal pour verrouiller une zone",
            "damage": "35-60 dégâts de verdure",
            "dot": "régénération",
            "zone": "verdure",
            "actions": ["fait pousser un buisson de couverture", "enracine la ligne de vue", "bloque une voie avec des lianes", "crée un couvert pour les alliés", "grandit une zone défensive"]
        },
        "ice": {
            "verb": "gèle",
            "terrain": "solidifie le sol, crée des murs de glace et transforme les passages en glissières",
            "damage": "50-80 dégâts de glace",
            "dot": "fragilité glacée",
            "zone": "givre",
            "actions": ["gèle une route en mur", "crée un pont de glace", "bloque une zone avec un bloc gelé", "rend un passage glissant", "fige une ligne de fuite"]
        },
        "ground": {
            "verb": "terraforme",
            "terrain": "souligne le sol, lève des blocs et construit des murs ou des rampes de terre",
            "damage": "60-90 dégâts de terre",
            "dot": "déséquilibre",
            "zone": "dune",
            "actions": ["soulève un bloc pour fermer une route", "crée une rampe en hauteur", "réduit un passage en ruine", "ouvre une tranchée", "fait tomber un mur de terrain"]
        },
        "flying": {
            "verb": "souffle",
            "terrain": "décale les courants aériens, crée un vent de hauteur et change les angles de tir",
            "damage": "45-70 dégâts de vent",
            "dot": "souffle instable",
            "zone": "courant aérien",
            "actions": ["pousse l'ennemi hors d'une ligne", "donne de l'altitude à un allié", "contrarie le tir d'un adversaire", "traverse une zone de vent", "crée un angle aérien mortel"]
        },
        "poison": {
            "verb": "contamine",
            "terrain": "corrompt les blocs, remplit la zone de miasmes et laisse une zone toxique",
            "damage": "40-75 dégâts de poison",
            "dot": "poison sur 3 tours",
            "zone": "miasme",
            "actions": ["souille une zone de combat", "corrompt un bloc de couvert", "remplit une route de poison", "déclenche un nuage toxique", "retient un ennemi dans une zone pourrie"]
        },
        "psychic": {
            "verb": "distord",
            "terrain": "ouvre des portails, déplace des blocs et casse la logique des lignes de vue",
            "damage": "50-85 dégâts psychiques",
            "dot": "confusion",
            "zone": "distorsion",
            "actions": ["téléporte une unité hors de la ligne", "ouvre un portail de flanc", "change l'angle d'un bloc", "déforme la visibilité sur une zone", "swap un allié et un ennemi"]
        },
        "metal": {
            "verb": "renforce",
            "terrain": "solidifie les structures, projette des débris et transforme la zone en mur dense",
            "damage": "65-100 dégâts de métal",
            "dot": "impact lourd",
            "zone": "acier",
            "actions": ["renforce un mur par un bloc massif", "projette des débris dans une ligne", "transforme un obstacle en fortification", "crée une collision lourde", "forme une barrière de fer"]
        },
        "shadow": {
            "verb": "masque",
            "terrain": "noircit la zone, coupe la vision et crée un angle caché dans l'ombre",
            "damage": "55-85 dégâts d'ombre",
            "dot": "lenteur du flanc",
            "zone": "pénombre",
            "actions": ["cache une unité dans l'ombre", "casse une ligne de vue", "crée un angle de flanc", "réduit la détection d'une zone", "attaque depuis une zone noire"]
        },
        "ghost": {
            "verb": "phasage",
            "terrain": "traverse les barrières physiques, applique une condamnation et crée des passages éthérés",
            "damage": "50-80 dégâts spectrals",
            "dot": "condamnation sur 3 tours",
            "zone": "spectre",
            "actions": ["traverse un mur sans coût", "applique condamnation", "raccourcit la distance de phase", "ouvre un corridor fantomatique", "attaque en franchissant les obstacles"]
        },
        "fairy": {
            "verb": "protège",
            "terrain": "remplit la zone de brume mystique, immunise les alliés contre les altérations et réduit les dégâts physiques",
            "damage": "35-60 dégâts de brume",
            "dot": "immunité aux statuts",
            "zone": "brume",
            "actions": ["immunise un allié contre les statuts", "crée une zone de protection", "réduit les dégâts physiques subis", "garde la formation dans la brume", "renforce la stabilité de l'équipe"]
        },
        "rock": {
            "verb": "scelle",
            "terrain": "lève des piliers et des éboulements pour fermer des lignes de vue et des couloirs étroits",
            "damage": "60-95 dégâts de pierre",
            "dot": "blocage de terrain",
            "zone": "pierre",
            "actions": ["lève un pilier fermé", "bloque une ligne de vue", "crée une barrière de roches", "ferme un passage étroit", "déclenche un éboulement"]
        },
        "bug": {
            "verb": "enchevêtre",
            "terrain": "pose des toiles et des zones d'ancrage qui empêchent d'être poussé ou attiré",
            "damage": "45-70 dégâts de toile",
            "dot": "harcèlement de swarm",
            "zone": "toile",
            "actions": ["pose une toile", "ancre une cible en place", "bloque un mouvement de retrait", "harcèle un flanc avec des essaims", "empêche le repositionnement"]
        },
        "fighting": {
            "verb": "projette",
            "terrain": "envoie les adversaires contre les murs, les rebords et les cratères d'impact",
            "damage": "70-110 dégâts de choc",
            "dot": "dégâts de chute",
            "zone": "impact",
            "actions": ["projecte une cible dans un mur", "envoie au sol un adversaire", "génère un cratère de choc", "provoque un coup de masse", "décale le front par une collision brutale"]
        },
        "dragon": {
            "verb": "déchaîne",
            "terrain": "crée des zones de colère et de violence pure qui augmentent les dégâts sur le terrain", 
            "damage": "80-120 dégâts de rage",
            "dot": "zone de colère",
            "zone": "rage",
            "actions": ["crée une zone de colère", "augmente la puissance des alliés sur la zone", "bloque les sorts défensifs", "déclenche une furie destructrice", "surchauffe le terrain"]
        },
        "steel": {
            "verb": "armure",
            "terrain": "pose des armures métalliques et des barrières rigides qui réduisent les dégâts bruts",
            "damage": "60-90 dégâts de métal",
            "dot": "impact blindé",
            "zone": "acier",
            "actions": ["renforce une armure de structure", "pose une barrière d'acier", "réduit les dégâts bruts reçus", "réagit au courant électrique", "crée une contre-pression métallique"]
        },
    }
    profile = element_profiles.get(element_id, element_profiles["normal"])

    names = [
        f"{class_name} {profile['verb']}",
        f"{element_name} {class_name}",
        f"Zone de {profile['zone']}",
        f"Pont de {element_name}",
        f"{profile['verb'].capitalize()} de terrain",
        f"Ligne de {profile['zone']}",
        f"{class_name} en rupture",
        f"Flux {element_name}",
        f"Pression {element_name}",
        f"Finale de {element_name}",
    ]

    ranges = ["melee", "medium", "zone", "medium", "self", "line", "medium", "long", "zone", "long"]
    aoes = ["single", "single", "burst", "line", "self", "line", "zone", "single", "burst", "zone"]
    targets = ["unit_or_tile", "unit_or_tile", "tile_area", "tile_area", "self", "unit_or_tile", "tile_area", "unit_or_tile", "tile_area", "tile_area"]

    descriptions = [
        "{0} frappe une cible et {1} pour {2} ; {3}.",
        "{0} utilise {4} sur une ligne pour {1} et faire {2} ; {3}.",
        "{0} remplit une zone de {5} puis {1} pour {2} ; {3}.",
        "{0} modifie le sol avec {4} et {1} pour {2}.",
        "{0} active un état local et {1} pendant {6} ; {3}.",
        "{0} projette une onde de {5} qui {1} pour {2} ; {3}.",
        "{0} verrouille une route et {1} pour {2} dans une zone ; {3}.",
        "{0} relie les cibles et {1} pour {2} avec un effet de {5} ; {3}.",
        "{0} fait exploser la zone et {1} pour {2} ; {3}.",
        "{0} déclenche la fin de combo et {1} pour {2} ; {3}."
    ]

    skill_bible = build_skill_bible(class_data, element_data)
    skills = []
    for slot, name in enumerate(names, start=1):
        damage = profile["damage"]
        duration = "1 tour" if slot < 6 else "2 tours" if slot < 9 else "3 tours"
        terrain_effect = profile["terrain"]
        action = profile["actions"][(slot - 1) % len(profile["actions"])]
        zone_label = profile["zone"]
        template = descriptions[slot - 1]
        description = template.format(
            class_name,
            profile["verb"],
            damage,
            terrain_effect,
            action,
            zone_label,
            duration,
        )
        pattern = skill_bible[slot - 1]
        skills.append({
            "slot": slot,
            "name": name,
            "pattern_name": pattern["name"],
            "effect_type": pattern["effect_type"],
            "map_impact": pattern["map_impact"],
            "control_style": pattern["control"],
            "cost": 1 + (slot / 3),
            "range": ranges[slot - 1],
            "aoe": aoes[slot - 1],
            "target": targets[slot - 1],
            "effect_tags": [
                class_data.get("role_primary", "support"),
                element_data.get("reaction_primary", "adaptation"),
                element_id,
                "terrain",
                element_data.get("control", "zone_control"),
                element_data.get("signature_gameplay", "generic"),
            ],
            "description": description,
            "damage_type": element_id,
            "damage": damage,
            "terrain_change": terrain_effect,
            "status_effect": profile["dot"],
            "duration": duration,
        })
    return skills


def generate_pur_champion(class_data, element_data):
    base = {
        "id": f"pur_{class_data['id']}_{element_data['id']}",
        "name": champion_name(class_data, element_data),
        "class_id": class_data["id"],
        "primary_element": element_data["id"],
        "secondary_element": None,
        "is_hybrid": False,
        "rarity": "common",
        "role_primary": class_data.get("role_primary", "unknown"),
        "role_secondary": class_data.get("role_secondary", "unknown"),
        "archetype_group": class_data.get("group", "general"),
        "terrain_mechanics": class_data.get("terrain_mechanics", []),
        "movement": class_data.get("movement", "standard"),
        "control": class_data.get("control", "none"),
        "element_control": element_data.get("control", ""),
        "unique_gameplay": element_data.get("signature_gameplay", "generic"),
        "team_synergy_theme": element_data.get("team_synergy_theme", "general"),
        "internal_synergy": element_data.get("internal_synergy", "general cohesion"),
        "signature_combo": element_data.get("combo_signature", "generic"),
        "strengths": class_data.get("strengths", []),
        "weaknesses": class_data.get("weaknesses", []) + element_data.get("weaknesses", []),
        "same_element_bonus": {
            "trigger": "same_element_ally_bonus",
            "theme": element_data.get("team_synergy_theme", "general"),
            "description": get_same_element_bonus(element_data),
            "signature_gameplay": element_data.get("signature_gameplay", "generic")
        },
        "passives": {
            "class_passive": f"{class_data.get('name', 'Champion')} profite de {class_data.get('terrain_mechanics', ['terrain'])[0]}",
            "element_passive": element_data.get("internal_synergy", "general cohesion"),
            "terrain_interaction": f"{class_data.get('terrain_mechanics', ['terrain'])[0]} + {element_data.get('terrain_modified', ['terrain'])[0]}",
            "same_element_impact": get_same_element_bonus(element_data)
        },
        "base_stats": {
            "pv": 1000,
            "pa": 8,
            "pm": 4,
            "initiative": 1000,
            "dmg_phys": 100,
            "dmg_elem": 100,
            "tacle": 100,
            "crit": 5,
        },
        "skills": build_skill_set(class_data, element_data)
    }

    group = class_data.get("group", "general")
    role = class_data.get("role_primary", "support")
    if group == "heavy":
        base["base_stats"]["pv"] = 1250
        base["base_stats"]["dmg_phys"] = 130
        base["base_stats"]["tacle"] = 120
    elif group == "agile":
        base["base_stats"]["pv"] = 900
        base["base_stats"]["pm"] = 5
        base["base_stats"]["initiative"] = 1100
        base["base_stats"]["crit"] = 10
    elif group == "flux":
        base["base_stats"]["pv"] = 980
        base["base_stats"]["pa"] = 9
        base["base_stats"]["dmg_elem"] = 130
    elif group == "link":
        base["base_stats"]["pv"] = 1050
        base["base_stats"]["dmg_elem"] = 120
    elif group == "engineering":
        base["base_stats"]["pv"] = 1100
        base["base_stats"]["dmg_elem"] = 115

    if "tank" in role or role == "guardian":
        base["base_stats"]["pv"] += 150
    if "assassin" in role or role == "skirmisher_vertical":
        base["base_stats"]["initiative"] += 100
    if "mage" in role or "zone" in role:
        base["base_stats"]["dmg_elem"] += 30
        base["base_stats"]["pa"] += 1

    base["skill_bible"] = build_skill_bible(class_data, element_data)
    return base


def generate_hybrid_pair(element_a, element_b):
    pair_key = f"{element_a['id']}_{element_b['id']}"
    hybrid_name = f"{element_a['name']} + {element_b['name']}"
    effect_a = element_a.get("signature_gameplay", "terrain")
    effect_b = element_b.get("signature_gameplay", "terrain")
    pair_synergy = get_pair_synergy(element_a, element_b)
    description_core = f"{effect_a} + {effect_b} -> {pair_synergy['result']}"
    hybrid_skills = []
    for i in range(1, 11):
        primary = element_a.get("id", "normal")
        secondary = element_b.get("id", "normal")
        damage_a = element_a.get("reaction_primary", "adaptation")
        damage_b = element_b.get("reaction_primary", "adaptation")
        if i == 1:
            desc = f"Le duo {element_a['name']} + {element_b['name']} déclenche {pair_synergy['result']} : une réaction de terrain qui transforme une ligne en zone de pression, {pair_synergy['description'].lower()}."
            name = f"Liaison {element_a['name']}"
        elif i == 2:
            desc = f"Le duo crée une zone de réaction {pair_synergy['result']} qui remplit le terrain avec {pair_synergy['terrain']} et force l'ennemi à bouger ou se faire piéger."
            name = f"Zone {element_a['name']}"
        elif i == 3:
            desc = f"Le mélange {element_a['name']} / {element_b['name']} modifie le sol en {pair_synergy['terrain']} et coupe plusieurs routes d'attaque en même temps."
            name = f"Route {element_b['name']}"
        elif i == 4:
            desc = f"Le combo projette des impacts combinés, enchaînant {effect_a} puis {effect_b} sur une cible qui est déjà prise dans {pair_synergy['result']}."
            name = f"Impact {element_a['name']}"
        elif i == 5:
            desc = f"Le duo active une boucle défensive autour de {pair_synergy['result']} : il garde les alliés en sécurité, renforce les angles et transforme le terrain en fortification."
            name = f"Bouclier {element_b['name']}"
        elif i == 6:
            desc = f"Le champ se densifie avec {pair_synergy['result']} : dégâts, zone, déplacement forcé et disruption de route sont combinés dans un seul axe de menace."
            name = f"Champ {element_a['name']}"
        elif i == 7:
            desc = f"La réaction de terrain transforme l'espace en zone de menace composite : {pair_synergy['description']}"
            name = f"Rupture {element_b['name']}"
        elif i == 8:
            desc = f"Le duo verrouille une zone et crée une ligne de pression qui force la cible à choisir entre avancer, se cacher ou recevoir le coup de {pair_synergy['result']}."
            name = f"Verrou {element_a['name']}"
        elif i == 9:
            desc = f"La chaîne de terrain combine {effect_a} et {effect_b} pour produire {pair_synergy['result']} sur plusieurs cibles, en transformant la carte en piège en cascade."
            name = f"Chaîne {element_b['name']}"
        else:
            desc = f"La fin de combo mélange {element_a['name']} et {element_b['name']} en une zone décisive grâce à {pair_synergy['result']} : les routes, les angles et la sécurité du terrain sont tous renversés."
            name = f"Finale {element_a['name']}"

        hybrid_skills.append({
            "slot": i,
            "name": name,
            "cost": 1.5 + (i / 4),
            "range": ["melee", "medium", "zone", "line", "self", "medium", "long", "zone", "medium", "long"][i - 1],
            "aoe": ["single", "single", "burst", "line", "self", "zone", "burst", "line", "zone", "burst"][i - 1],
            "target": ["unit_or_tile", "tile_area", "tile_area", "unit_or_tile", "self", "tile_area", "unit_or_tile", "tile_area", "unit_or_tile", "tile_area"][i - 1],
            "effect_tags": [
                element_a.get("reaction_primary", "adaptation"),
                element_b.get("reaction_primary", "adaptation"),
                "terrain",
                "hybrid",
                "combo",
                "reaction_mixed"
            ],
            "description": desc,
            "damage_type": f"{primary}_{secondary}",
            "terrain_change": description_core,
            "status_effect": "combo reaction",
            "duration": "2 tours",
        })
    hybrid_bible = []
    for i in range(10):
        hybrid_bible.append({
            "slot": i + 1,
            "name": hybrid_skills[i]["name"],
            "pattern_name": hybrid_skills[i]["name"],
            "effect_type": ["single_hit", "line_pressure", "zone_field", "terrain_transform", "buff_self", "wave_push", "route_lock", "chain_link", "burst_combo", "finisher"][i],
            "map_impact": ["damage_on_target", "tile_reaction", "area_lock", "tile_change", "safe_zone", "route_disruption", "path_block", "multi_target", "explosive_zone", "decisive_zone"][i],
            "control_style": ["burst", "lane_control", "zone_control", "map_control", "self_stability", "push", "movement_control", "chain_control", "burst", "finisher"][i],
            "description": hybrid_skills[i]["description"],
        })

    return {
        "id": f"hyb_{pair_key}",
        "name": hybrid_name,
        "primary_element": element_a["id"],
        "secondary_element": element_b["id"],
        "is_hybrid": True,
        "team_synergy_theme": f"hybrid_{element_a.get('team_synergy_theme', 'mixed')}_{element_b.get('team_synergy_theme', 'mixed')}",
        "unique_gameplay": description_core,
        "internal_synergy": f"{element_a.get('internal_synergy', '')} / {element_b.get('internal_synergy', '')}",
        "signature_combo": f"{element_a.get('combo_signature', '')} + {element_b.get('combo_signature', '')}",
        "pair_synergy": {
            "result": pair_synergy["result"],
            "combo_name": pair_synergy["combo_name"],
            "terrain": pair_synergy["terrain"],
            "description": pair_synergy["description"],
        },
        "same_element_bonus": {
            "trigger": "pair_synergy_bonus",
            "theme": f"hybrid_{element_a.get('team_synergy_theme', 'mixed')}_{element_b.get('team_synergy_theme', 'mixed')}",
            "description": pair_synergy["description"]
        },
        "skill_bible": hybrid_bible,
        "skills": hybrid_skills,
        "base_stats": {
            "pv": 1200,
            "pa": 9,
            "pm": 5,
            "initiative": 1050,
            "dmg_phys": 110,
            "dmg_elem": 120,
            "tacle": 105,
            "crit": 8,
        }
    }


def main():
    classes = load_json(DATA / "classes.json")
    elements = load_json(DATA / "elements.json")
    element_map = {element["id"]: element for element in elements}

    monolithes = []
    for class_data in classes:
        for element_data in elements:
            monolithes.append(generate_pur_champion(class_data, element_data))

    hybrids = []
    seen_pairs = set()
    for pair in TOP_HYBRID_PAIRS:
        a_id, b_id = pair
        if a_id not in element_map or b_id not in element_map:
            continue
        if (a_id, b_id) in seen_pairs or (b_id, a_id) in seen_pairs:
            continue
        seen_pairs.add((a_id, b_id))
        hybrids.append(generate_hybrid_pair(element_map[a_id], element_map[b_id]))

    roster = {
        "hybrid_policy": {
            "mode": "elite_two_element_synergies",
            "selected_pairs": list(TOP_HYBRID_PAIRS),
            "notes": "Only the strongest 2-element pairings are kept to maximize map-changing, readable, and tactical gameplay.",
        },
        "monolithes": monolithes,
        "hybrids": hybrids,
        "stats": {
            "monolithes_total": len(monolithes),
            "hybrids_total": len(hybrids),
            "overall_total": len(monolithes) + len(hybrids),
        }
    }

    out = ROOT / "data" / "generated_roster.json"
    with out.open("w", encoding="utf-8") as f:
        json.dump(roster, f, ensure_ascii=False, indent=2)

    print(f"generated roster: {len(monolithes)} monolithes, {len(hybrids)} hybrids -> {out}")


if __name__ == "__main__":
    main()
