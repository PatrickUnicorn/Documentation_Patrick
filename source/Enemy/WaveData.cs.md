# Documentation de la Classe `WaveData`

## Description

La classe `WaveData` est un `ScriptableObject` destiné à définir et à gérer les configurations des vagues d'ennemis. Elle permet de paramétrer les détails relatifs à la génération d'ennemis, y compris le rythme de leur apparition, la durée de la vague, et les conditions nécessaires pour terminer une vague.

## Propriétés

- **possibleSpawnPrefabs (GameObject[])**: Un tableau de prefabs d'ennemis qui peuvent être générés pendant cette vague.
- **spawnInterval (Vector2)**: Intervalle de temps entre chaque spawn, exprimé par un minimum et un maximum.
- **spawnsPerTick (Vector2Int)**: Nombre d'ennemis générés à chaque intervalle.
- **waveDuration (float)**: Durée pendant laquelle la vague continue de générer des ennemis.
- **minSpawns (uint)**: Nombre minimum d'apparitions requises pour que la vague puisse se terminer, assurant un certain niveau de défi.
- **maxSpawns (uint)**: Nombre maximal d'ennemis que cette vague peut générer.
- **conditions (ExitCondition)**: Conditions qui déclenchent la fin de la vague, telles que la durée de la vague ou le nombre maximal d'apparitions.
- **mustKillAll (bool)**: Indique si tous les ennemis doivent être éliminés pour que la vague puisse progresser vers la suivante.
- **spawnCount (uint)**: Compteur pour le nombre d'ennemis générés, utilisé pour gérer le respect de `minSpawns` et `maxSpawns`.

## Méthodes

### GetPossibleSpawns

Cette méthode sélectionne un nombre aléatoire d'ennemis à générer à partir de `possibleSpawnPrefabs`, basé sur `spawnsPerTick`. Elle retourne un tableau des prefabs d'ennemis sélectionnés.

### GetSpawnInterval

Calcule un intervalle de temps aléatoire entre deux apparitions consécutives d'ennemis, en se basant sur `spawnInterval`.

## Utilisation

Cette classe peut être utilisée pour gérer de manière flexible les vagues d'ennemis dans un jeu, permettant une variété de configurations pour ajuster la difficulté et la dynamique des niveaux.

1. **Création de l'Instance**:
   - Utilisez le menu Unity pour créer une nouvelle instance de `WaveData` via `Assets -> Create -> ScriptableObjects -> Rogue-like/Wave Data`.
   
2. **Configuration des Vagues**:
   - Définissez les prefabs d'ennemis, les intervalles de spawn, la durée de la vague, et d'autres paramètres directement dans l'inspecteur Unity.

3. **Intégration dans le Gameplay**:
   - Utilisez un gestionnaire de niveau ou de vague qui référence l'instance de `WaveData` pour orchestrer les spawns et gérer la progression des vagues.

