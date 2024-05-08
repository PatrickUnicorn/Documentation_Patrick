# Documentation de la Classe `Passive`

## Propriétés

- **currentBoosts (CharacterData.Stats)**: Stocke les améliorations ou bonus actuels que l'objet passif apporte.

## Classes Internes

### Modifier

`Modifier` est une sous-classe de `LevelData` qui contient des statistiques spécifiques que l'objet passif peut octroyer à chaque niveau.

- **boosts (CharacterData.Stats)**: Statistiques améliorées fournies par ce modificateur.

## Méthodes

### Initialise

```csharp
public virtual void Initialise(PassiveData data)
```

Initialise l'objet passif avec les données spécifiques, en configurant les statistiques de base. Cette méthode appelle `Initialise` de la classe parent `Item` pour inclure des configurations initiales pour les objets passifs.

### GetBoosts

```csharp
public virtual CharacterData.Stats GetBoosts()
```

Renvoie les statistiques actuelles fournies par l'objet passif.

### DoLevelUp

```csharp
public override bool DoLevelUp()
```

Réalise la montée de niveau de l'objet passif, en améliorant les statistiques selon les données du niveau suivant. Vérifie d'abord si une montée de niveau est possible. Si le niveau maximal est déjà atteint, affiche un avertissement et renvoie `false`. Si la montée de niveau est possible, applique les nouveaux boosts et renvoie `true`.
