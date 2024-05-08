# Documentation de la Classe `CharacterSelector`

## Description

`CharacterSelector` sert à gérer la sélection des données de personnage. Il utilise le motif de conception Singleton pour assurer une instance unique de sélectionneur de personnage à travers les scènes, permettant un accès facile aux données de personnage sélectionnées de manière globale.

## Fonctionnalités

- **Singleton Pattern**: Assure qu'une seule instance de `CharacterSelector` est active à tout moment. Si une instance existe déjà lors de la création d'une nouvelle, la nouvelle instance est détruite.
- **Sélection de personnage**: Permet de sélectionner et de stocker les données d'un personnage à travers les sessions de jeu.
- **Chargement dynamique**: Charge et sélectionne les données de personnage depuis les ressources du projet si aucune instance n'est disponible.

## Propriétés

- **instance (CharacterSelector)**: Référence statique à l'instance unique de ce composant.
- **characterData (CharacterData)**: Les données du personnage actuellement sélectionné.

## Méthodes

### Awake

Initialise le Singleton, en préservant l'instance existante ou en configurant une nouvelle instance tout en s'assurant que l'objet ne soit pas détruit au chargement de nouvelles scènes.

### GetData

Renvoie les données du personnage sélectionné. Si aucune instance n'est disponible, elle tente de charger les données de personnage depuis les ressources du projet.

```csharp
public static CharacterData GetData()
```

### SelectCharacter

Permet de définir manuellement les données de personnage à utiliser.

```csharp
public void SelectCharacter(CharacterData character)
```

### DestroySingleton

Détruit l'instance du Singleton, permettant la création d'une nouvelle instance à l'avenir.

```csharp
public void DestroySingleton()
```

### Configuration

1. **Attachement du script**: Attachez ce script à un GameObject dans la scène principale de votre jeu, idéalement dans une scène qui charge au démarrage.
2. **Sélection des personnages**: Utilisez `SelectCharacter` pour définir le personnage choisi par l'utilisateur.
3. **Accès aux données**: Utilisez `GetData` pour récupérer les données du personnage depuis n'importe quel script dans votre projet.
