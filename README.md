# Roster Design Structure

This project stores the roster logic in a clean data-first structure.

## Core gameplay mode

This project is now explicitly designed as a Tactical Grid MOBA hybrid.

The game is not a pure turn-based roster generator only. The roster, elements, synergies, terrain, and mob logic are built to support a lane-based tactical arena where:

- combat happens on a grid of playable cells
- lanes are tactical corridors with pressure, objectives and terrain shifts
- player-controlled champions fight in a structured lane / objective rhythm
- enemy waves push automatically after each character action
- elemental cells and neutral progression zones change lane state and map control
- passive lane mobs and drake-like objectives create strategic decision points

## Folder layout

- data/classes.json : the 18 class definitions
- data/elements.json : the 18 element definitions
- data/reactions.json : reaction rules between elements
- data/synergies.json : synergy profiles for specific pairs
- data/champion_template.json : champion schema used to generate content
- data/generation_rules.json : roster generation constraints
- data/generated_roster.json : current generated roster snapshot
- scripts/ChampionRosterBuilder.gd : Godot-ready generation entry point

## Design principle

The roster is generated from rules, not handcrafted one by one.

- Class = how the champion plays
- Element = what the champion changes in the terrain
- Hybrid pair = what kind of tactical combo the champion is
- Champion instance = final runtime data
- Lane = a strategic pressure corridor with objective states and terrain progression
- Mob wave = autonomous push logic reacting after player turns
- Neutral tile = a growth / buff / danger cell that changes route decisions

## Tactical lane rules

The lane system is a first-class gameplay loop:

- each lane has pressure, push state, and objective threat
- after each character turn, nearby mobs and wave units evaluate their next move
- terrain cells may be altered by elemental effects
- progression cells create buffs, heal, cover, hazard, or resource gain
- passive lane mobs behave like drake / Nash-style objectives: they create pressure and grant temporary strategic advantage

## Elemental terrain expectations

Every element in the roster must be able to influence map flow, not only direct combat:

- Fire: burning cells, pressure zones, ignition routes
- Water: flooded lanes, slow/redirect effects, fluid movement paths
- Electric: chained danger, conductive lines, charge windows
- Grass: cover, regen, bush growth, ambush zones
- Ice: frozen routes, slowed movement, control locks
- Ground: fortified terrain, high ground, hard cover
- Poison: toxic zones, attrition, contamination pathing
- Shadow: obscured lanes, stealth windows, flanking pressure
- Psychic: warped paths, disrupted sight lines, angle manipulation
- Metal: reinforced structures, magnetic barriers, hardened push paths
- Normal: improvised tactical objects, neutral adaptation cells

## Gameplay loop target

The intended gameplay loop is:

1. Champion acts on a grid tile
2. Terrain and elemental cells react immediately
3. Lane pressure updates and mob push resolves
4. Passive objectives or drake-like mobs react
5. The next character resolves actions in initiative order
6. The lane state evolves as a living tactical map

This ensures the game remains dynamic, readable, and decisively MOBA-like without abandoning the grid-based tactical identity.
