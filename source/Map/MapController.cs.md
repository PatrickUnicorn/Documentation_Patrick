# Documentation de la Classe `MapController`

## Description

La classe `MapController` est conçue pour gérer la génération dynamique et l'optimisation des morceaux de terrain (chunks) dans un jeu. Elle s'occupe de charger de nouveaux terrains à proximité du joueur et de désactiver ceux qui sont éloignés pour optimiser les performances.

## Propriétés

- **terrainChunks (List<GameObject>)**: Liste des préfabriqués de terrain qui peuvent être générés.
- **player (GameObject)**: Référence à l'objet joueur.
- **checkerRadius (float)**: Rayon utilisé pour vérifier l'existence de terrains autour d'une position donnée.
- **terrainMask (LayerMask)**: Masque de calque utilisé pour identifier les terrains dans les vérifications de collision.
- **currentChunk (GameObject)**: Terrain actuellement actif où le joueur se trouve.
- **spawnedChunks (List<GameObject>)**: Liste des terrains actuellement générés dans le jeu.
- **maxOpDist (float)**: Distance maximale à partir de laquelle un terrain est considéré comme trop éloigné pour rester actif.
- **optimizerCooldownDur (float)**: Durée du cooldown pour l'optimiseur de terrains, afin de limiter la fréquence des optimisations.

## Méthodes

### Start

Initialise la position initiale du joueur.

### Update

Appelle les méthodes `ChunkChecker` et `ChunkOptimizer` à chaque frame pour vérifier et gérer les terrains.

### ChunkChecker

Vérifie la position du joueur par rapport à sa dernière position enregistrée et détermine la direction du mouvement. Sur la base de cette direction, elle vérifie s'il est nécessaire de générer de nouveaux terrains et les génère si nécessaire.

### CheckAndSpawnChunk

```csharp
void CheckAndSpawnChunk(string direction)
```

Vérifie l'absence de terrain dans la direction spécifiée par rapport au `currentChunk`. Si aucun terrain n'est présent, un nouveau terrain est généré à cette position.

### GetDirectionName

```csharp
string GetDirectionName(Vector3 direction)
```

Calcule la direction normalisée du mouvement du joueur et la convertit en une chaîne de caractères qui indique la direction générale (par exemple, "Right Up", "Left Down").

### SpawnChunk

```csharp
void SpawnChunk(Vector3 spawnPosition)
```

Génère un nouveau terrain à la position spécifiée en choisissant aléatoirement parmi la liste `terrainChunks`.

### ChunkOptimizer

Gère l'activation et la désactivation des terrains générés en fonction de leur distance par rapport au joueur. Cette méthode optimise les performances en désactivant les terrains qui ne sont plus visibles ou nécessaires.

## Utilisation

Attachez ce script à un objet contrôleur dans votre scène Unity qui ne sera pas détruit (par exemple, un objet de gestion de niveau). Configurez les propriétés via l'inspecteur Unity, en particulier la liste `terrainChunks` avec les préfabriqués de terrain souhaités, et assurez-vous que le joueur et les terrains sont correctement identifiés par leurs Layer Masks (Dans Unity, chaque objet peut être assigné à un Layer (calque). Vous pouvez ensuite utiliser des Layer Masks pour spécifier quels layers doivent être pris en compte ou ignorés dans certaines opérations, comme les détections de collisions).
