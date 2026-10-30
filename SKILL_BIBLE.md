# Skill Bible

## 1. Principe directeur

Les compétences doivent toujours faire une chose claire et jouable :
- infliger des dégâts,
- contrôler une zone,
- modifier le terrain,
- forcer le déplacement,
- ou créer une réaction élémentaire.

Chaque sort doit répondre à 5 questions simples :
1. Qui touche ?
2. Ce que l’ennemi subit ?
3. Quel bloc / terrain change ?
4. Quelle ligne de combat est cassée ou ouverte ?
5. Quel est le combo qui suit ?

---

## 2. Les 10 archetypes de sort

1. Impact direct
   - dégâts ciblés,
   - bonus de précision,
   - souvent le premier coup du combo.

2. Ligne de terrain
   - zone en ligne,
   - pression sur une route,
   - contrôle de lane / angle.

3. Zone de contrôle
   - danger sur une surface,
   - blocage ou ralentissement,
   - visuel de zone élémentaire.

4. Mutation du sol
   - transformation de blocs,
   - création de couvert, de mur, de rampe, de zone liquide ou d’ombre.

5. Bouclier local
   - protection d’allié,
   - bonus de stabilité,
   - quasi toujours lié à la défense ou au soutien.

6. Onde de choc
   - push, knockback, inversion d’angle,
   - gestion de l’espace et des lignes d’attaque.

7. Blocage de route
   - fermeture d’un passage,
   - verrouillage d’un accès ou d’une sortie.

8. Chaîne / réseau
   - multi-cibles ou réaction sur plusieurs entités,
   - très fort dans les combos hybrides.

9. Explosion composite
   - zone de burst,
   - dégâts importants et map impact,
   - la vraie compétence de fin de séquence.

10. Fin de séquence
   - fin de combo,
   - souvent déclenche un effet terrain décisif,
   - transforme une bonne position en victoire.

---

## 3. Règles d’écriture d’une compétence

Une compétence est bonne quand elle décrit :
- le type de cible : unité, zone, ligne, sol, allié, ennemi,
- le type d’effet : dégâts, dot, ralentissement, buff, blind, push, mutation,
- le type de terrain modifié : liquide, glace, mur, cendre, poison, brouillard, ombre,
- la logique de combat : ouverture de ligne, blocage de route, angle de tir, fin de combo,
- la durée ou le cycle de contrôle.

Chaque description doit utiliser des mots concrets comme :
- brûle,
- inonde,
- gèle,
- corrompt,
- pousse,
- casse la ligne de vue,
- soulève,
- verrouille,
- relie,
- transforme.

---

## 4. Filtres de qualité

Un sort ne doit pas être validé s’il :
- ne dit pas s’il touche unité ou terrain,
- ne dit pas s’il crée une zone ou un debuff,
- ne dit pas ce qui change sur la map,
- ressemble à un “damage + flavor text” sans logique de mouvement,
- n’a pas de rôle dans le combo ou la réaction.

---

## 5. Résumé élémentaire

### Feu
- Gameplay : zone brûlante, pressure, burst.
- Terrain : charbon, cendre, végétation ignifée.
- Rôle : contrôle du front, punition d’espaces serrés.

### Eau
- Gameplay : route, ralentissement, pression de ligne.
- Terrain : eau, boue, route glissante.
- Rôle : contrôle du mouvement et des angles.

### Électricité
- Gameplay : chaîne, arcs, zones conductrices.
- Terrain : sol chargé, obstacles conducteurs.
- Rôle : multi-cible, punition de groupe.

### Plante
- Gameplay : couvert, densification, soutien.
- Terrain : lianes, mur de verdure, zone de régénération.
- Rôle : défense, contrôle des lignes de vue, endurance.

### Glace
- Gameplay : gel, blocage, immobilisation.
- Terrain : glace, murs gelés, passage glissant.
- Rôle : verrouillage et temp check.

### Terre
- Gameplay : mur, rampe, tranchée, hauteur.
- Terrain : collines, murets, blocs levés.
- Rôle : terrain et contrôle de la carte.

### Vent
- Gameplay : déplacement, altitude, ouverture d’angle.
- Terrain : courants, vents, lignes aériennes.
- Rôle : repositionnement et contrôle de la ligne de tir.

### Poison
- Gameplay : zone toxique, débuff, corruption.
- Terrain : miasmes, zones corrompues.
- Rôle : pression lente et mort sur zone.

### Psychique
- Gameplay : déformation d’espace, visibilités, swap.
- Terrain : portail, espace altéré, ligne cassée.
- Rôle : contrôle de la position et de la lecture du terrain.

### Métal
- Gameplay : mur, impacts lourds, fortification.
- Terrain : fer, blindage, débris.
- Rôle : front lourd, sécurité, punition de rupture.

### Ombre
- Gameplay : invisibilité, flanc, vision coupée.
- Terrain : zone noire, angle caché, demi-obscurité.
- Rôle : ambush, finisher, pression sur la profondeur.

### Normal
- Gameplay : improvisation, adaptation, objets du décor.
- Terrain : caisses, barricades, murs improvisés.
- Rôle : flexibilité, terrain organique.

---

## 6. Output attendu côté données

La sortie JSON doit contenir, pour chaque champion :
- le nom,
- les stats,
- les 10 sorts,
- les tags d’effet,
- la description du sort,
- le type d’effet,
- l’impact terrain,
- le style de contrôle,
- et un skill bible propre à l’élément.

C’est la structure qui permet ensuite de faire le gameplay dans Godot sans perdre les règles de conception.
