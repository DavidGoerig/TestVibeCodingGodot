
FICHE MASTER DE CHAMPION : VERSION FINALE (MASTER TEMPLATE)


📇 1. IDENTIFIANTS & METADATA

• ID UNIQUE : CHAMP-XXX (Monolithe, ex: CHAMP-042) ou HYB-XXX (Hybride, ex: HYB-012)
• NOM DU CHAMPION : [Nom du Héros / Titre]
• RARETÉ DE LA CARTE : [Commune / Rare / Épique / Légendaire]
• NIVEAU D'ÉVOLUTION : [⭐ à ⭐⭐⭐⭐⭐] (Détermine le nombre de compétences actives disponibles)
• CLAN ÉLÉMENTAIRE : [Nom de la faction liée à l'Élément Principal]

🎭 2. ARCHÉTYPE ARCHITECTURAL (La Matrice de Jeu)

• CLASSE PRINCIPALE : [L'une des 18 classes] (Gouverne le rapport physique au terrain, la modification de la grille et les stats de base)
• ÉLÉMENT PRINCIPAL : [L'un des 12 éléments] (Gouverne les propriétés physiques, chimiques et logiques de la matière voxel appliquée)
• ÉLÉMENT SECONDAIRE : [L'un des 11 autres éléments / Aucun si champion pur]
• GROUPE DE COMPOSITION : [Profil Lourd / Profil Agile / Profil de Flux / Profil de Lien / Profil d'Ingénierie]

📊 3. MATRICE DES STATISTIQUES (Formule Dynamique)

Toutes les statistiques en match sont calculées selon la formule stricte : Valeur Actuelle = Base (1000 PV, 8 PA, 4 PM, 1000 Init, 100 Dmg Phys, 100 Dmg Élem, 100 Tacle, 0% Crit) + Modificateur Classe + Modificateur Élément.
Caractéristique	Valeur de Base	Modificateur Classe	Modificateur Élément	Valeur Actuelle (En Match)	Règle d'Impact sur la Grille Voxel
PV (Points de Vie)	1000	+/- X	+/- X	XXXX	Durabilité de la chair du personnage avant K.O.
PA (Points d'Action)	8	+/- X	+/- X	X	Ressource par tour pour lancer des compétences/sorts.
PM (Points de Mouvement)	4	+/- X	+/- X	X	Distance maximale franchissable horizontalement (1 PM = 1 Case).
INIT (Initiative)	1000	+/- X	+/- X	XXXX	Détermine l’ordre d'action dans la timeline du tour de jeu.
DMG PHYS	100	+/- X	+/- X	XXX	Puissance des attaques brutes, des impacts de blocs et démolitions.
DMG ÉLEM	100	+/- X	+/- X	XXX	Puissance des altérations au sol, magies et réactions en chaîne.
TACLE	100	+/- X	+/- X	XXX	Capacité à immobiliser un ennemi adjacent (Bloque ses PM).
CRITIQUE	0%	+ X%	+ X%	X%	Probabilité de doubler l’impact d'un sort ou d'une démolition.

🔩 4. CONSTANTES PHYSIQUES ET REPERES DE VERTICALITÉ

Ces variables fixes empêchent les champions d'enfreindre la physique de votre monde en voxel :
• CAPACITÉ DE SAUT MAX (Hauteur) : [Par défaut : 1 Voxel] (Définit la hauteur maximale qu'un champion peut escalader à la verticale par lui-même en dépensant 1 PM. Le Voltigeur est l'exception).
• MASSE GÉOMÉTRIQUE : [Léger / Moyen / Lourd / Monolithe] (Définit la résistance aux compétences de poussée cinétique/attraction et le comportement face à la gravité. Un champion Monolithe enfonce les dalles fragiles).
• INDICE DE PERFORATION DE BLOC : [Dureté 1 (Herbe) / Dureté 2 (Roche) / Dureté 3 (Acier)] (Définit quel type de voxel créé par l'ennemi le champion peut détruire avec ses compétences physiques de base).
• PORTÉE DE VISION (Ligne de vue) : [Par défaut : 5 cases] (Réduite par le brouillard de guerre, les écrans de fumée du Feu ou les zones d'Ombre).

🧩 5. COMPORTEMENTS INTRINSÈQUES (Passifs de Grille)

• PASSIF DE CLASSE (L'Outil) : [Effet lié au style de jeu] (ex: Le Sapeur inflige +50% de dégâts aux dalles de fondation).
• PASSIF ÉLÉMENTAIRE (La Matière) : [Effet lié au type de voxel] (ex: L'Hydro gagne +2 PM s'il marche sur une dalle inondée).
• INTERACTION VOXEL UNIQUE : [La règle mécanique signature du champion] (ex: "Atomise le sol sous les pieds pour provoquer des chutes verticaux", "Projette les débris des blocs cassés comme des munitions").

🗂️ 6. CONFIGURATION DE L'ARBRE DE COMPÉTENCES (Les 10 Attaques)

Structure adaptative débloquée par les Étoiles de la carte. Chaque sort doit obligatoirement être défini par 4 balises logiques : Coût (PA) | Portée (PO) | Zone d'Effet (AoE) | Cible (Unité ou Voxel).
• ⭐ 1 ÉTOILE :
	• [A1] ATTAQUE DE BASE (Coût: 0 PA | PO: Corps-à-corps | AoE: Mono) : Attaque physique ou harcèlement de base, indexé sur les Dmg Phys.
	• [A2] INFUSION ÉLÉMENTAIRE (Coût: Moyen | PO: Distance | AoE: Mono) : Sort appliquant la matière élémentaire sur une dalle et infligeant de légers Dmg Élem.
• ⭐⭐ 2 ÉTOILES :
	• [A3] OUTIL DE TRANSITION TACTIQUE (Coût: Faible | PO: Variable) : Compétence de mobilité ou d'ajustement de relief (Saut, charge, glissade, TP, construction miniature).
	• [A4] RÉACTION DE MATIÈRE (Passif) : S'active automatiquement lorsque le champion interagit avec son élément spécifique sur la grille.
• ⭐⭐⭐ 3 ÉTOILES :
	• [A5] SATURATION DE ZONE (Coût: Élevé | PO: Moyenne | AoE: Zone) : Inonde, embrase, sature ou gèle un grand groupe de voxels de la grille (ex: 3x3 cases).
	• [A6] ALTÉRATION / MAÎTRISE DU TACLE (Coût: Moyen | PO: Courte) : Utilise la matière environnante pour entraver, paralyser ou bloquer le mouvement ennemi.
• ⭐⭐⭐⭐ 4 ÉTOILES :
	• [A7] MANIPULATION LOURDE DE TOPOGRAPHIE (Coût: Élevé | PO: Moyenne) : Compétence majeure d'ingénierie. Soulève des piliers de roche, fait s'effondrer des plafonds, liquéfie des dalles.
	• [A8] CAPACITÉ DE RIPOSTE OU DE CONTRE (Effet déclenché) : S'active de manière passive si une fortification alliée adjacente est détruite ou si un fluide ennemi s'approche.
• ⭐⭐⭐⭐⭐ 5 ÉTOILES :
	• [A9] ULTIME CATACLYSME (Coût: Très Élevé | PO: Longue | AoE: Massive) : Le sort signature du champion. Rase une forteresse ou érige instantanément une citadelle.
	• [A10] SYNERGIE DE COHÉSION (Passif Ultime) : Modifie globalement les règles de la grille pour toute l'équipe (ex: Connecte toutes les dalles conductrices en un réseau partagé).

🤝 7. PROTOCOLES DE SYNERGIE EN MATCH (La Meta 4v4)

• SYNERGIE DE CLASSE SYSTÉMIQUE : [Classe] + Pourquoi (ex: Le Maçon pour façonner les piliers de visée du Chasseur).
• CONDUCTIVITÉ ÉLÉMENTAIRE DIRECTE : [Élément] + Pourquoi (ex: L'Eau pour étendre instantanément le courant de l'Électricité).
• CONTRE GÉOMÉTRIQUE NATUREL : [Classe/Élément ennemi] + Pourquoi (ex: L'Écorcheur qui détruit le high-ground créé par le Maçon, provoquant une chute mortelle).