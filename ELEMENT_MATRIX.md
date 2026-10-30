# Matrice de génération des éléments

## Objectif
Cette matrice sert à donner à chaque élément une identité claire, exploitable par les classes, et utilisable pour la génération des champions Purs et Hybrides.

Chaque élément doit être défini avec ces 8 champs :
- matière dominante
- terrain modifié
- mobilité
- contrôle
- réaction élémentaire principale
- forces tactiques
- faiblesse tactique
- combo signature

---

## 1. Normal
- matière dominante : matière brute, objets, matière neutre
- terrain modifié : blocs non spécialisés, objets de décor, barricades improvisées
- mobilité : polyvalente, adaptable, improvisation
- contrôle : interruption légère, repositionnement, jeu d’objets
- réaction élémentaire principale : neutralisation / adaptation / conversion de terrain
- forces tactiques : multitool, objets, terrain improvisé, flexibilité
- faiblesse tactique : peu de spécialisation pure, dépend de la situation
- combo signature : transforme un objet ou un bloc en avantage tactique immédiat

## 2. Fire
- matière dominante : chaleur, ignition, combustion
- terrain modifié : blocs enflammés, cendres, fumée, zones ardentes
- mobilité : explosion, pression, zone de danger
- contrôle : brule, pousse, force les lignes, rend le terrain instable
- réaction élémentaire principale : ignition / propagation / explosion
- forces tactiques : zone damage, discrétion de l’attaque, pression, anti-vegetation
- faiblesse tactique : vulnérable aux zones humides, à la contre-pression et au contrôle de zone
- combo signature : allume une zone, fait exploser une structure ou un nuage toxique

## 3. Water
- matière dominante : liquide, humidité, flux, gravité
- terrain modifié : sols mouillés, inondation, zones de glisse, broderies de courant
- mobilité : glisse, redirection, déplacement assisté, flux
- contrôle : courant, injection de terrain, ralentissement, absorbtion
- réaction élémentaire principale : mouiller / geler / vaporiser / contaminer
- forces tactiques : contrôle de la carte, blocage, mobilité assistée, anti-feu
- faiblesse tactique : faible pression pure sur des structures très dures
- combo signature : inonde, connecte, puis active une réaction électrique ou glacée

## 4. Electric
- matière dominante : courant, impulsion, connectivité
- terrain modifié : dalles conductrices, fils, zones électrifiées
- mobilité : superposition de circuits, dash sur réseaux, mobilité sur terrain conducteur
- contrôle : chaîne, stun, réseau, décharge
- réaction élémentaire principale : conduction / surcharge / court-circuit
- forces tactiques : dégâts en chaîne, contrôle de la zone, endurance de réaction
- faiblesse tactique : dépend fortement des réseaux et du terrain
- combo signature : connecte plusieurs dalles ou unités, puis déclenche un arc ou une surcharge

## 5. Grass
- matière dominante : végétation, racines, croissance
- terrain modifié : buissons, plantes, barrières naturelles, zone de couverture
- mobilité : déplacement dans la végétation, camouflage, croissance de chemins
- contrôle : camouflage, entrave, buff / soins, contrôle territorial
- réaction élémentaire principale : croissance / pollution / guérison / obstruction
- forces tactiques : support, guérison, terrain couvert, contrôle d’angles
- faiblesse tactique : faible puissance brute, très dépendant du terrain
- combo signature : fait grandir une zone, puis l’alimente au feu ou au poison

## 6. Ice
- matière dominante : froid, solidification, glace, rigidité
- terrain modifié : murs, ponts, rampes, sols glissants, barrières gelées
- mobilité : glisse, court déplacement, contrôle de trajectoire
- contrôle : blocage, ralentissement, immobilisation, structure rigide
- réaction élémentaire principale : congélation / solidification / givre
- forces tactiques : terrain et mobilité de contrôle, fortification, blocage d’axes
- faiblesse tactique : faible adaptation dans des environnements très chauds ou très fluides
- combo signature : transforme le terrain en pont, mur, rampe ou piège de glace

## 7. Ground
- matière dominante : pierre, terre, gravité, stabilité
- terrain modifié : élévation, creusement, mur, tunnel, falaise, pente, sous-sol
- mobilité : dominateur de hauteur, routes, accès, terrain capable de changer
- contrôle : blocage de passages, hauteur, mur de terre, séisme
- réaction élémentaire principale : compression / élévation / écrasement / terrain modifié
- forces tactiques : contrôle de la topographie, fortification, efficacité sur l’axe et la hauteur
- faiblesse tactique : peu de mobilité pure, assez lent à répondre sur l’instant
- combo signature : crée une hauteur, une falaise ou un mur, puis exploite le gain d’avantage

## 8. Flying
- matière dominante : vent, air, altitude, vitesse
- terrain modifié : zones aériennes, courants, hauteurs, massifs volants
- mobilité : déplacement rapide, saut vertical, dépassement de terrain
- contrôle : dans les airs, poussée, manipulation de ligne de vue, portage
- réaction élémentaire principale : vent / poussée / ascension / déviation
- forces tactiques : flanc, hauteurs, surprise, portage, anti-projectile
- faiblesse tactique : faible présence sur le sol, vulnérable à des zones de contrôle
- combo signature : prend l’altitude, contourne l’axe, puis frappe ou repositionne ailleurs

## 9. Poison
- matière dominante : toxine, décomposition, contamination
- terrain modifié : nuages, sols empoisonnés, zones de dégât continu
- mobilité : zone dangereuse, piège, empoisonnement, usure
- contrôle : diminution des capacités, anti-heal, contamination, zone de nuisance
- réaction élémentaire principale : contamination / corrosif / miasme / poison combiné
- forces tactiques : anti-heal, pression constante, vitesse de dégradation du terrain
- faiblesse tactique : faible puissance brute pure, dépend des zones et du temps
- combo signature : contamine, puis exploite un feu, une explosion ou une chute

## 10. Psychic
- matière dominante : énergie mentale, espace, distorsion, logique
- terrain modifié : téléportation, distorsion, altération de distance, illusion de terrain
- mobilité : positionnement mental, déplacement by swap / portails / téléport
- contrôle : téléport, swap, attraction, répulsion, manipulation de position
- réaction élémentaire principale : distorsion / inversion / déplacement d’entité / téléportation
- forces tactiques : contrôle des espaces, repositionnement, isolement, prise par surprise
- faiblesse tactique : plus faible si la cible est blindée ou si la zone est saturée
- combo signature : modifie la position d’une unité ou d’un bloc pour créer un avantage de terrain

## 11. Metal
- matière dominante : fer, acier, densité, rigidité, conductivité
- terrain modifié : murs renforcés, blocs lourds, structures métalliques, fortification
- mobilité : contrôlée par la masse, lente mais stable
- contrôle : blindage, projection de débris, contrôle des lignes de barrage
- réaction élémentaire principale : magnétisme / rigidité / blindage / impact lourd
- forces tactiques : protection, fortification, collisions, impacts massifs, structures solides
- faiblesse tactique : peu de flexibilité, très lent en déplacement, dépend de la structure
- combo signature : renforce un mur ou un bloc, puis projette une masse ou le transforme en zone défensive

## 12. Shadow
- matière dominante : obscurité, silence, flanc, ombre, distorsion de perception
- terrain modifié : zones sombres, zones d’anti-vision, blocs opaques, camouflages de terrain
- mobilité : infiltration, flanc, contournement, mobilité dans l’ombre
- contrôle : anti-vision, isolement, surprise, détour des lignes de vue
- réaction élémentaire principale : obscurcissement / dissimulation / corruption / noirceur
- forces tactiques : assassinat, flanc, manipulation visuelle, anti-vision, isolement
- faiblesse tactique : faible résistance pure et dépendance à l’environnement
- combo signature : utilise l’ombre pour passer derrière la ligne ou créer un angle mort

---

## 13. Règle de cohérence générale

Chaque élément doit avoir :
- une matière dominante claire
- un terrain qu’il modifie
- un type de mobilité propre
- un type de contrôle propre
- une réaction élémentaire facilement compréhensible
- une vraie force tactique
- une vraie faiblesse tactique
- un combo signature reconocissable

Si un élément ne répond pas à ces 8 points, il n’est pas assez clair pour produire des champions uniques.

---

## 14. Règle de génération hybride

Pour les champions hybrides, la logique ne doit pas être “deux éléments qui se cumulent”.
Elle doit être :
- Élément A = la matière / le terrain / la base du jeu
- Élément B = la réaction / la mobilité / le contrôle complémentaire

Donc :
- Fire + Water = vapeur, lave, zones instables
- Water + Electric = courant, conductivité, réseau
- Ice + Ground = ponts gelés, falaise durcie, terrain de glace
- Shadow + Poison = zone de corruption dans l’ombre
- Psychic + Flying = déplacement non-linéaire, téléportation aérienne
- Metal + Fire = mur fortifié + zone chaude

Les hybrides doivent produire un comportement de terrain ou de positionnement spécifique, pas juste un bonus.
