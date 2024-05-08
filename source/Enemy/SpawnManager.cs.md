# Documentation de la Classe `SpawnManager`

## Description

La classe `SpawnManager` est conçue pour gérer la génération d'ennemis, en utilisant des données spécifiques à chaque vague d'ennemis. Ce script utilise les informations contenues dans les objets `WaveData` pour déterminer quelles entités ennemies générer et à quelle intervalle.

## Fonctionnalités

- **Gestion des vagues**: Utilise un tableau de `WaveData` pour gérer différentes vagues d'ennemis.
- **Génération de position**: Calcule les positions de spawn basées sur la vue de la caméra pour s'assurer que les ennemis apparaissent à des endroits appropriés par rapport au champ de vision du joueur.
- **Singleton Pattern**: S'assure qu'une seule instance de `SpawnManager` est active en utilisant le pattern Singleton.

## Propriétés

- **data (WaveData[])**: Un tableau contenant les données de chaque vague d'ennemis.
- **currentWaveIndex (int)**: Index de la vague actuelle à partir de laquelle les ennemis sont générés.
- **referenceCamera (Camera)**: Référence à la caméra utilisée pour déterminer les positions de spawn basées sur le viewport.
- **spawnTimer (float)**: Compteur décroissant jusqu'au prochain spawn d'ennemis.

## Méthodes

### Start

Initialise l'instance du gestionnaire de spawn et avertit si plusieurs instances sont détectées dans la scène.

### Update

Vérifie le `spawnTimer` et déclenche la génération d'ennemis en utilisant les données de la vague actuelle lorsque nécessaire. Réinitialise le `spawnTimer` après chaque génération d'ennemis.

### GeneratePosition

Calcule une position aléatoire pour la génération des ennemis, en s'assurant que ces positions sont valides par rapport au viewport de la caméra. Affiche un avertissement si la caméra n'est pas orthographique, ce qui pourrait causer des problèmes de positionnement des ennemis.

### Configuration

1. **Attachement du script**: Attachez ce script à un GameObject dans votre scène.
2. **Référencement des Vagues**: Assurez-vous de référencer correctement les objets `WaveData` dans le tableau `data`.
3. **Configuration de la Caméra**: Référencez la caméra principale dans `referenceCamera`.
