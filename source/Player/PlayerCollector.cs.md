# Documentation de la Classe `PlayerCollector`

## Description

La classe `PlayerCollector` sert à gérer la collecte automatique d'objets par le joueur dans un jeu Unity. Elle utilise un `Collider2D` pour détecter et collecter les objets de type `Pickup` qui entrent dans son champ d'action. Cette classe est particulièrement utile pour des jeux où les joueurs peuvent attirer et collecter des objets à distance, comme des pièces, des power-ups, ou d'autres collectibles.

## Composants Requis

- **Collider2D**: Nécessaire pour détecter les entrées en collision avec des objets `Pickup`. Doit être configuré en tant que Trigger pour éviter les interactions physiques (collision).
- **PlayerStats**: Script qui doit être attaché au parent du GameObject pour accéder aux statistiques ou autres attributs du joueur.

## Propriétés

- **pullSpeed (float)**: Vitesse à laquelle les objets `Pickup` sont attirés vers le joueur une fois détectés.

## Méthodes

### Start

Initialise les composants en récupérant les références nécessaires :
- **PlayerStats**: Obtenu à partir du parent du GameObject pour accéder et manipuler les statistiques du joueur.

### SetRadius

```csharp
public void SetRadius(float r)
```

Ajuste le rayon du `CircleCollider2D` pour modifier la zone de détection autour du joueur. Utile pour dynamiquement augmenter ou diminuer la portée de collecte basée sur les power-ups ou d'autres conditions de jeu.

### OnTriggerEnter2D

```csharp
private void OnTriggerEnter2D(Collider2D col)
```

Déclenché lorsque d'autres colliders entrent en contact avec le collider de ce GameObject. Si le collider entrant est un objet de type `Pickup`, la méthode `Collect` de cet objet est appelée, passant les statistiques du joueur et la vitesse de collecte comme arguments.

## Utilisation

### Configuration

1. **Attachement du script**: Attachez ce script à un GameObject représentant le joueur ou un sous-objet dédié à la collecte.
2. **Configurer le Collider**: Assurez-vous que le GameObject a un `CircleCollider2D` configuré comme Trigger. Ajustez son rayon pour couvrir la zone désirée autour du joueur.
3. **Assignation des propriétés**: Définissez la `pullSpeed` dans l'inspecteur Unity pour contrôler la vitesse à laquelle les objets sont attirés vers le joueur.

### Interaction avec des objets `Pickup`

les objets collectables dans le jeu doivent utiliser le script `Pickup` et configurer correctement pour interagir avec `PlayerCollector`. Lorsque ces objets entrent dans la zone du collider, ils seront automatiquement attirés vers le joueur et collectés en fonction de la logique définie dans leur propre script.
