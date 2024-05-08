# Documentation de la Classe `PassiveData`

La classe `PassiveData` étend `ItemData` et est utilisée pour définir les données des objets passifs dans Unity grâce à des ScriptableObjects.

## Attributs

- **baseStats (Passive.Modifier)**: Représente les statistiques de base de l'objet passif.
- **growth (Passive.Modifier[])**: Un tableau de modificateurs qui définissent comment les statistiques de l'objet passif évoluent avec chaque montée de niveau après le premier.

## Méthodes

### GetLevelData

```csharp
public override Item.LevelData GetLevelData(int level)
```

Renvoie les données correspondant au niveau spécifié de l'objet passif. Si le niveau est 1, renvoie `baseStats`. Pour les niveaux supérieurs, elle cherche dans le tableau `growth` pour trouver les statistiques correspondant au niveau donné. Si le tableau ne contient pas d'entrée pour le niveau demandé, un avertissement est généré et une instance vide de `Passive.Modifier` est retournée.

## Configuration dans Unity

Pour faciliter la création et la gestion de ces données, `PassiveData` est décoré avec l'attribut `CreateAssetMenu`, permettant de créer facilement des instances de ce type via le menu de l'éditeur Unity. Ces instances peuvent ensuite être remplies avec des données spécifiques dans l'éditeur.
