# Documentation de la Classe `ItemData`

La classe `ItemData` est un type de ScriptableObject dans Unity, conçu pour stocker des données relatives à des objets, tels que des armes ou d'autres objets interactifs. Cette classe sert de modèle pour les attributs et les comportements que les objets peuvent avoir, notamment leur évolution.

## Propriétés

- **icon (Sprite)**: Icône représentant l'objet dans l'interface utilisateur.
- **maxLevel (int)**: Niveau maximal que l'objet peut atteindre.

## Évolutions

La structure `Evolution` détermine comment et quand un objet peut évoluer en une nouvelle forme.

- **name (string)**: Nom de l'évolution.
- **condition (Condition)**: Condition nécessaire pour que cette évolution se produise. Les conditions possibles sont définies par l'énumération `Condition`, qui inclut `auto` pour une évolution automatique ou `treasureChest` pour une évolution déclenchée par l'interaction avec un coffre au trésor.
- **consumes (Consumption)**: Spécifie les types d'objets qui sont utilisés et perdus lors de l'évolution. Les valeurs possibles sont des drapeaux, avec `passives` pour les objets passifs et `weapons` pour les armes.
- **evolutionLevel (int)**: Niveau requis de l'objet pour que l'évolution puisse se produire.
- **catalysts (Config[])**: Tableau de configurations définissant les objets nécessaires pour que l'évolution se produise.
- **outcome (Config)**: Configuration de l'objet résultant de l'évolution.

### Config

Structure utilisée pour définir un type d'objet et le niveau requis pour les catalyseurs et le résultat de l'évolution.

- **itemType (ItemData)**: Référence à un autre `ItemData` qui représente le type d'objet requis.
- **level (int)**: Niveau requis de cet objet.

## Méthodes

- **GetLevelData (int level)**: Méthode abstraite destinée à être implémentée par des sous-classes pour retourner les données de niveau spécifiques, comme le nom et la description, basées sur le niveau d'un objet.


