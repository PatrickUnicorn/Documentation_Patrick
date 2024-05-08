# Documentation de la Classe `TreasureChest`

## Description

La classe `TreasureChest` gère le comportement des coffres au trésor dans le jeu. Elle utilise `MonoBehaviour` pour interagir avec les joueurs lorsqu'ils entrent en collision avec un coffre.

## Méthode Principale

### OnTriggerEnter2D

```csharp
private void OnTriggerEnter2D(Collider2D col)
```

Cette méthode est appelée automatiquement par Unity lorsque un autre objet entre dans le collider 2D du coffre au trésor. Elle vérifie si l'objet est un joueur avec un inventaire valide. Si c'est le cas, elle tente d'ouvrir le coffre au trésor, puis détruit le coffre.

### OpenTreasureChest

```csharp
public void OpenTreasureChest(PlayerInventory inventory, bool isHigherTier)
```

Ouvre le coffre et interagit avec l'inventaire du joueur pour potentiellement évoluer des objets, spécifiquement des armes, en fonction des conditions prédéfinies dans les données d'évolution de chaque arme. L'évolution se fait uniquement si l'arme est prête à évoluer sous la condition spéciale `treasureChest`.

- **inventory (PlayerInventory)**: L'inventaire du joueur contenant les objets qui peuvent être affectés.

## Comportement de l'Évolution

La méthode `OpenTreasureChest` itère sur chaque emplacement d'arme dans l'inventaire du joueur. Pour chaque arme, elle vérifie si l'arme a des données d'évolution applicables sous la condition `treasureChest`. Si une telle évolution est possible, elle tente de l'appliquer. Si l'évolution réussit, elle interrompt immédiatement la boucle, ce qui signifie qu'un seul objet peut évoluer à chaque ouverture de coffre.

## Utilisation

1. Attachez ce script à un objet de jeu avec un collider 2D configuré pour détecter les collisions avec le joueur.
2. Assurez-vous que les objets du joueur sont bien configurés pour répondre aux conditions d'évolution spécifiées dans leurs données respectives.