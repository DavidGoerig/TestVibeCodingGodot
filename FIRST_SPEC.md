# Direction de design du projet

## Vision globale : Tactical Grid MOBA

Le projet ne doit plus être perçu comme un simple générateur de roster ou un ensemble de champions isolés. Il s’agit d’un jeu de type Tactical Grid MOBA, où la bataille se déroule sur une carte en lanes, avec :

- un terrain découpé en cases jouables,
- des voies de pression (lanes) avec objectif et push,
- des vagues de mobs qui avancent après chaque tour de personnage,
- des éléments qui modifient les cases, les routes et le contrôle de la lane,
- des objectifs passifs de type drake / Nash qui créent une progression dynamique,
- des cases neutres de progression (soin, buff, couverture, danger, ressource, terrain élémentaire),
- des hybrides qui changent la logique de terrain, pas seulement le damage direct.

Le but est de garder l’identité tactique de cases, tout en ajoutant la dynamique MOBA : pressure de lane, push, rotation, neutral objectives, objectifs courants, et terrain vivant.

## Règle de base du tour

Le système doit être construit ainsi :

1. un personnage joue son tour,
2. le terrain réagit selon les éléments actifs et les cases touchées,
3. les mobs de lane évaluent leur prochaine action,
4. les objectifs passifs (drake / neutral progression) se déclenchent ou évoluent,
5. la pression de lane est recalculée,
6. le prochain personnage agit.

L’idéal est que le monde continue à réagir après chaque action, pour garder une impression de dynamique sans perdre la lisibilité tactique.

## Lanes à forte valeur stratégique

Chaque lane doit être une mini-map, pas un simple couloir.

Une lane doit inclure :

- une zone de spawn / wave de départ,
- une zone de pression active,
- des cases de progression neutre,
- un point de contestation / flanc / rotation,
- une zone d’objectif final (tour, shrine, drake, point de contrôle).

Une bonne lane est une voie où le joueur doit prendre des décisions entre :

- avancer pour pousser,
- sécuriser une zone de progression,
- défendre la tour,
- stopper une wave,
- prendre un objectif passif,
- exploiter un terrain élémentaire favorable.

## Mobs passifs / drake / Nash-like

Les mobs ne doivent pas être seulement des unités d’occupation. Ils doivent jouer un rôle de progression et de pression.

Les objectifs de lane peuvent être de plusieurs types :

- drake de terrain : modifie les cases de la voie et active un buff de lane,
- neutral progressor : donne soin, buff, vitesse, ressource ou contrôle de zone,
- mob passif de pression : fixe un point de convergence sur la lane,
- objectif de rupture : force une décision entre push ou stop-push.

Le but est qu’un joueur puisse choisir entre :

- contrôler un objectif pour prendre l’avantage terrain,
- ignorer le neutre pour pousser plus vite,
- défendre une zone précieuse,
- sacrifier une voie pour créer un flanc ou un coup de rotation.

## Cases neutres de progression

Les cases du terrain doivent être des ressources actives, pas du simple décor.

Chaque case de progression peut apporter un type d’effet :

- soin / régénération,
- buff de puissance,
- buff de vitesse,
- couverture / blindage,
- danger / dégat sur zone,
- ressource / charge / mana,
- contrôle de lane,
- transformation de terrain.

Les éléments doivent être hétérogènes et jouer sur les cases :

- Feu = brûle, chauffe, presse et ouvre la voie par pression,
- Eau = inonde, ralentit, détourne et aide la mobilité,
- Électricité = relie les unités, crée des risques sur ligne,
- Plante = couvre, soigne, protège, crée le bush / la jungle,
- Glace = gel, mouvement glissant, verrouillage de zones,
- Terre = hauteur, blocage, refuge, couverture solide,
- Ombre = obscurité, ambush, flancs, vision cassée,
- Poison = zone toxique, attrition, pression progressive,
- Psychique = angles déformés, espace altéré,
- Métal = mur, armature, renforcement, barrières,
- Normal = improvisation, objets de terrain, adaptation.

## Rôle des éléments dans les lanes

Les éléments doivent modifier le comportement du terrain, pas seulement les dégâts:

- un feu peut créer une zone de burn sur la lane,
- de l’eau peut transformer un passage traversable en voie de contrôle,
- une glace peut créer une faille de mouvement,
- un poison peut fatiguier une zone et forcer la sortie de la voie,
- une plante peut créer un couvert ou une zone de soin,
- l’ombre peut rendre la zone dangereuse pour les unités exposées.

Le terrain est donc un acteur à part entière du jeu.

## Principe de direction artistique et fonctionnelle

Les éléments ne doivent pas être seulement des étiquettes de damage. Ils doivent être des familles de gameplay complètes et cohérentes avec :

- les formes de combats,
- les flux de lane,
- les effets de terrain,
- les objectifs passifs,
- les personnages hybrides,
- et la manière dont les unités traversent, sécurisent, poussent et contrôlent la map.

C’est cette logique qui fera que les champions, les éléments et le système de cases s’alignent pour former un vrai Tactical Grid MOBA et non un simple combat à cases.

Oui. Là, je changerais légèrement le centre du design : **les 12 éléments ne doivent surtout pas correspondre à 12 rôles**. Chaque élément doit constituer une famille complète de créatures capable de couvrir plusieurs archétypes, mais avec une manière différente de remplir ces rôles.

Par exemple, Feu doit pouvoir avoir un support, un tank, un assassin, un zoner ou un bruiser — mais ils doivent tous « sentir » le Feu.

## 1. Structure fondamentale

Je partirais sur :

```text
12 ÉLÉMENTS
    ↓
~8-12 ENTITÉS / élément à terme
    ↓
Chaque entité
├── 1 ou 2 éléments
├── rôle principal
├── rôle secondaire
├── stats propres
├── mobilité propre
├── passive
└── 10 attaques débloquées avec les niveaux
```

Les rôles constituent des **tags**, pas des classes rigides :

```text
Tank
Bruiser
DPS mono
DPS zone
Assassin
Support
Healer
Controller
Zoner
Disruptor
Summoner
Terrain Manipulator
Artillery
Mobile
Trapper
```

Une créature peut donc être :

```text
Fire
Assassin / Mobile

Water
Support / Controller

Ground
Tank / Terrain Manipulator

Poison
Trapper / Zoner
```

Mais également :

```text
Fire
Support / Zoner

Water
Assassin / Mobile

Ground
Artillery / DPS

Poison
Tank / Controller
```

C'est cette diversité qui évite le classique :

> Feu = dégâts, Eau = soin, Sol = tank.

---

# 2. Le terrain est le deuxième roster

Je considérerais quasiment le terrain comme un ensemble d'entités.

Chaque case/bloc possède un état :

```text
Block
├── Material
├── HP
├── Height
├── ElementalState
├── Surface
├── Stability
└── Objects
```

Exemple :

```text
Stone Block
HP: 100
State: Wet
Surface: Poison
Height: 2
```

Une attaque peut donc cibler :

```text
ENTITY
CELL
BLOCK
SURFACE
OBJECT
```

Et surtout :

> **Chaque élément doit disposer d'au moins une façon particulière d'interagir avec le terrain.**

---

# 3. Les 12 éléments

Je garderais tes 12 types Pokémon :

```text
Normal
Fire
Water
Electric
Grass
Ice
Fighting
Poison
Ground
Flying
Psychic
Bug
```

La matrice faiblesse/résistance reste celle de Pokémon pour ces types.

Mais on ajoute par-dessus une **identité tactique**.

---

## NORMAL — Adaptation / objets / neutralité

Normal est l'élément polyvalent.

Identité :

```text
adaptation
objets
terrain neutre
copie
improvisation
carry / throw
```

Terrain :

- déplacer des blocs ;
- porter des objets ;
- jeter des objets ;
- construire des barricades ;
- détruire des obstacles ;
- utiliser les éléments du décor.

Archétypes possibles :

```text
Normal Tank
→ barricades / protection

Normal Assassin
→ mobilité + objets

Normal Support
→ repositionnement / buffs

Normal Artillery
→ lance des objets/blocs
```

Il devient le spécialiste de la **physique tactique**.

---

# 4. FIRE — Pression / propagation / destruction

Feu ne signifie pas simplement DPS.

Sa mécanique centrale :

```text
IGNITION
```

Il crée :

```text
Burning
Heat
Smoke
Ash
```

Interaction :

```text
Grass + Fire → Burning
Wood + Fire → Burning
Ice + Fire → Water
Poison Cloud + Fire → Explosion
Water + Fire → Steam
```

Fire DPS :

```text
propagation
explosions
AoE
```

Fire Assassin :

```text
dash through flames
teleport between burning cells
execute burning target
```

Fire Support :

```text
buff allies standing near fire
remove Ice
create smoke
give movement through Burning
```

Fire Tank :

```text
burning aura
fire walls
punish melee attackers
```

Donc même élément, gameplay totalement différent.

---

# 5. WATER — Flux / déplacement / contrôle

Identité :

```text
FLOW
```

L'eau modifie les cases :

```text
Dry → Wet
```

Elle peut éventuellement descendre selon l'altitude.

Interactions :

```text
Water + Electricity → Conductive
Water + Ice → Frozen
Water + Fire → Steam
Water + Ground → Mud
```

Water Support :

```text
heal
cleanse
Wet allies
movement assistance
```

Water Controller :

```text
currents
push/pull
flood
```

Water Assassin :

```text
move through Wet cells
emerge from water
```

Water Tank :

```text
redirect attacks
create water barriers
```

---

# 6. ELECTRIC — Réseau / burst / mobilité

Concept :

```text
CONDUCTION
```

L'électricité recherche des connexions.

```text
Wet Cell
   │
Wet Cell
   │
Enemy
```

→ propagation.

Elle peut également utiliser :

```text
metal
water
conductive objects
```

Electric Assassin :

```text
dash between conductive cells
```

Electric AoE :

```text
chain lightning
```

Electric Support :

```text
AP / initiative manipulation
energize allies
```

Electric Controller :

```text
electrified zones
stuns
network denial
```

---

# 7. GRASS — Croissance / contrôle territorial

Concept :

```text
GROWTH
```

Grass peut transformer une arène vide :

```text
turn 1     🌱
turn 3     🌿
turn 5     🌳
```

Il crée :

```text
vines
trees
roots
flowers
vegetation
```

Grass Tank :

```text
grow cover
roots
regeneration
```

Grass Assassin :

```text
hide in vegetation
root target
strike
```

Grass Support :

```text
healing plants
buff zones
```

Grass Summoner :

```text
plants / spores
```

Et le Feu peut réellement détruire son écosystème.

---

# 8. ICE — Construction / contrôle géométrique

Probablement un des éléments les plus intéressants avec ton terrain.

Ice peut :

```text
freeze Water
create Block
create Wall
create Bridge
create Ramp
make Slippery
```

Ice Tank :

```text
fortress
walls
armor
```

Ice Assassin :

```text
slide
high mobility
shatter
```

Ice Controller :

```text
freeze
block corridors
```

Ice Artillery :

```text
icicles
destroy frozen structures
```

Tu peux littéralement reconstruire la map.

---

# 9. FIGHTING — Physique / projection

C'est l'élément qui exploite le mieux ton système de physique.

Concept :

```text
FORCE
```

Il excelle en :

```text
Push
Pull
Carry
Throw
Collision
Jump
Ground Slam
```

Exemple :

```text
grab enemy
↓
jump
↓
throw enemy
↓
enemy hits wall
↓
wall breaks
↓
enemy falls
```

Fighting Support existe aussi :

```text
carry ally
throw ally onto high ground
intercept
bodyguard
```

Fighting Assassin :

```text
grapple
jump
isolated-target combo
```

---

# 10. POISON — Préparation / contamination

Concept :

```text
CONTAMINATION
```

Il crée :

```text
Poison Surface
Poison Cloud
Toxic Object
Disease
```

Poison Trapper :

```text
hidden traps
```

Poison Support :

```text
debuff
anti-heal
weakness
```

Poison Assassin :

```text
stack poison
execute at threshold
```

Poison Tank :

```text
toxic aura
damage attackers
```

Interaction particulièrement intéressante :

```text
Poison Cloud
      +
Fire
      ↓
EXPLOSION
```

---

# 11. GROUND — Architecture / destruction

L'un des éléments centraux du jeu.

Concept :

```text
TERRAFORMING
```

Il peut :

```text
Raise Block
Lower Block
Create Wall
Destroy Block
Create Pillar
Tunnel
Create Ramp
```

Donc :

```text
Enemy Archer
     A
    ███
    ███
████████

Earthquake
     ↓

     A
     ↓
████████
```

Ground Tank :

```text
fortification
```

Ground Assassin :

```text
burrow
emerge
```

Ground Support :

```text
create high ground for allies
```

Ground Controller :

```text
reshape battlefield
```

Ground Artillery :

```text
throw rocks / collapse terrain
```

---

# 12. FLYING — Position / altitude

Concept :

```text
AIRSPACE
```

Il ignore une partie de la topographie.

Mais il ne faut pas simplement lui donner « ignore terrain ».

Flying joue avec :

```text
wind
altitude
knockback
air currents
```

Flying Support :

```text
carry ally
move ally
wind corridors
```

Flying Assassin :

```text
dive
reposition
```

Flying Controller :

```text
tornado
push
redirect projectiles
```

Flying Artillery :

```text
high-ground attacks
```

---

# 13. PSYCHIC — Manipulation / règles

Psychic manipule davantage les **entités** que la matière.

Concept :

```text
CONTROL
```

Exemples :

```text
teleport
swap
attract
repel
illusion
copy
mind control
portal
```

Psychic Support :

```text
swap allies
give AP
teleport
```

Psychic Assassin :

```text
teleport behind target
isolate
```

Psychic Controller :

```text
portals
gravity zones
forced movement
```

Psychic Tank :

```text
barriers
redirect attacks
```

---

# 14. BUG — Réseau / infestation / essaim

Il faut éviter « Insecte = élément nul ».

Je lui donnerais une identité extrêmement systémique :

```text
SWARM
```

Il peut :

```text
spawn small entities
attach parasites
create webs
consume vegetation
build nests
```

Bug Controller :

```text
web
slow
terrain obstruction
```

Bug Assassin :

```text
climb
jump
ambush
```

Bug Support :

```text
hive buffs
symbiosis
```

Bug Summoner :

```text
swarm
```

Bug Tank :

```text
carapace
nest
```

Ça peut être un des éléments les plus originaux.

---

# 15. La matrice élément × rôle

C'est un document que je construirais explicitement.

| Element | Tank | Support | Mono | AoE | Assassin | Control | Mobility | Terrain |
|---|---|---|---|---|---|---|---|---|
| Normal | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Objects |
| Fire | ✓ | ✓ | ✓ | ★ | ★ | ✓ | ✓ | Burn |
| Water | ✓ | ★ | ✓ | ✓ | ✓ | ★ | ✓ | Flood |
| Electric | ✓ | ★ | ★ | ★ | ★ | ✓ | ★ | Conduct |
| Grass | ★ | ★ | ✓ | ✓ | ✓ | ★ | ✓ | Grow |
| Ice | ★ | ✓ | ★ | ✓ | ✓ | ★ | ✓ | Build |
| Fighting | ★ | ✓ | ★ | ✓ | ★ | ✓ | ★ | Break |
| Poison | ✓ | ★ | ★ | ✓ | ★ | ★ | ✓ | Contaminate |
| Ground | ★ | ✓ | ★ | ★ | ✓ | ★ | ✓ | Terraform |
| Flying | ✓ | ★ | ★ | ✓ | ★ | ★ | ★ | Wind |
| Psychic | ✓ | ★ | ★ | ✓ | ★ | ★ | ★ | Space |
| Bug | ★ | ★ | ✓ | ✓ | ★ | ★ | ★ | Swarm |

`★` signifie simplement **affinité naturelle**, pas « meilleur élément ».

Chaque colonne reste disponible à chaque élément.

---

# 16. C'est la combinaison des éléments qui doit devenir folle

À mon avis, c'est là que ton jeu peut vraiment avoir quelque chose.

Exemple :

```text
WATER
Flood
   ↓
ELECTRIC
Electrify
   ↓
FLYING
Push enemy into water
   ↓
GROUND
Raise walls around water
```

Tu viens de fabriquer une prison électrique.

Autre :

```text
GRASS
Grow forest
   ↓
POISON
Poison vegetation
   ↓
PSYCHIC
Teleport enemy inside
   ↓
FIRE
Ignite forest
```

Ou :

```text
ICE
Create bridge

FIGHTING
Throw enemy onto bridge

GROUND
Destroy support

FIRE
Melt bridge

        ↓

enemy falls
```

C'est exactement ce que je chercherais à obtenir.

---

# 17. Les équipes de 6 deviennent alors intéressantes

Je pense maintenant que **6 entités par joueur** peut être une très bonne cible, à condition de contrôler la durée des tours.

Parce que le team-building devient :

```text
6 slots
12 elements
roles
synergies
counters
terrain combos
```

Tu pourrais construire :

```text
RAIN TEAM

Water Controller
Water Support
Electric Assassin
Electric Artillery
Flying Controller
Grass Tank
```

ou :

```text
TERRAIN DESTRUCTION

Ground Controller
Ground Artillery
Fighting Bruiser
Flying Assassin
Fire Zoner
Psychic Support
```

ou :

```text
TRAP TEAM

Poison Trapper
Bug Controller
Psychic Manipulator
Fighting Thrower
Ice Controller
Electric Assassin
```

Ce n'est donc pas juste **6 Pokémon qui tapent**.

C'est une composition tactique.

---

# 18. Les 10 attaques par entité

Je ferais une progression du genre :

```text
Level 1      Skill 1
Level 3      Skill 2
Level 6      Skill 3
Level 10     Skill 4
Level 15     Skill 5
Level 20     Skill 6
Level 26     Skill 7
Level 32     Skill 8
Level 39     Skill 9
Level 47     Skill 10
```

Mais surtout, le kit devrait suivre une structure.

Par exemple :

```text
10 abilities

2 × basic / damage
2 × movement/manipulation
2 × element mechanics
1 × defensive
1 × utility
1 × combo/setup
1 × signature
```

Pas nécessairement exactement ces nombres pour chaque créature, mais ça force les kits à être tactiquement intéressants.

---

# 19. Double type

Et là ça devient encore plus intéressant.

Une créature :

```text
Water / Electric
```

peut être spécialisée dans :

```text
Wet
→ Conduct
→ Chain
```

Alors que :

```text
Water / Ice
```

joue :

```text
Wet
→ Freeze
→ Create terrain
```

et :

```text
Fire / Flying
```

joue :

```text
Burn
→ Wind
→ Spread fire
```

et :

```text
Ground / Fighting
```

joue :

```text
Create wall
→ Throw enemy into wall
→ Collision
→ Destroy wall
```

Le double type devient alors **un langage de gameplay**, pas seulement une matrice de multiplicateurs.

---

# 20. Règle de conception des créatures

Je mettrais une contrainte assez stricte dans le GDD.

Chaque nouvelle entité doit répondre à ces questions :

```text
1. Quel est son élément ?

2. Quel est son rôle principal ?

3. Quel est son rôle secondaire ?

4. Comment se déplace-t-elle différemment ?

5. Comment manipule-t-elle les unités ?

6. Comment manipule-t-elle le terrain ?

7. Quel état élémentaire crée-t-elle ?

8. Quel état élémentaire exploite-t-elle ?

9. Quel allié crée une synergie avec elle ?

10. Quelle est sa faiblesse tactique ?

11. Quel est son combo signature ?

12. Pourquoi la choisir plutôt qu'une autre
    créature du même élément et du même rôle ?
```

Si on ne sait pas répondre au **12**, la créature n'est probablement pas suffisamment intéressante.

---

# 21. Et surtout : terrain entièrement destructible

Je rendrais ça absolument central dans le moteur.

Pas :

```text
certaines cases sont destructibles
```

mais :

> **Toute case physique possède une structure et peut potentiellement être modifiée ou détruite, sauf exception explicitement déclarée par la map.**

Donc :

```text
████████████
████████████
████████████

         ↓ combat

████   █████
██      █████
████       ██
```

La map de fin de combat peut n'avoir quasiment plus rien à voir avec celle du début.

Ça implique dès le départ :

```text
dynamic pathfinding
dynamic LoS
dynamic height
falling
support
terrain HP
terrain material
terrain states
element reactions
```

et pas un GridMap Godot considéré comme statique.

---

## La vraie architecture du jeu devient donc

```text
             BATTLE CORE
                  │
       ┌──────────┴──────────┐
       │                     │
    ENTITIES              WORLD
       │                     │
  ┌────┴────┐          ┌─────┴─────┐
  │         │          │           │
Types     Roles      Blocks      Surfaces
  │         │          │           │
Skills   Movement   Materials    Elements
  │         │          │           │
  └─────────┴─────┬────┴───────────┘
                  │
             INTERACTIONS
                  │
          Reaction Engine
                  │
       ┌──────────┼──────────┐
       │          │          │
   Damage    Displacement   Terrain
       │          │          │
       └──────────┼──────────┘
                  │
              New State
```

Et **JcJ et JcE ne sont que deux consommateurs différents de ce moteur** :

```text
Human → Commands ┐
                 ├→ Battle Core
AI → Commands ───┘
```

C'est cette architecture que je figerais avant de commencer à produire les créatures.

Ensuite, je ferais un **`ELEMENTS_AND_ENTITIES.md`** séparé du document technique : pour chacun des 12 éléments, identité tactique, interaction avec chaque matériau/surface, interactions avec les 11 autres éléments, archétypes disponibles, mécaniques signatures, puis **5 premières créatures prototypes par élément = 60 créatures**, chacune avec rôle, double-type éventuel, passif et concept de ses 10 attaques. Ce serait le vrai document de game design du roster.