# Documentation de la Classe `Pickup`

## Description

La classe `Pickup` est conçue pour gérer le comportement des objets collectables dans le jeu. Elle utilise `MonoBehaviour` pour intégrer des animations et des interactions dans Unity. Les objets de cette classe peuvent se déplacer vers un joueur, fournir des bonus et utiliser une animation de flottement pour améliorer l'esthétique visuelle.

## Propriétés

- **lifespan (float)**: Durée de vie du collectable avant qu'il ne soit automatiquement détruit.
- **target (PlayerStats)**: Cible (joueur) vers laquelle le collectable se déplace.
- **speed (float)**: Vitesse à laquelle le collectable se déplace vers la cible.
- **initialPosition (Vector2)**: Position initiale du collectable utilisée pour l'animation de flottement.
- **initialOffset (float)**: Décalage initial utilisé pour l'animation de flottement pour éviter que tous les collectables ne bougent en synchronisation parfaite.

### BobbingAnimation (Structure)

- **frequency (float)**: Fréquence de l'animation de flottement.
- **direction (Vector2)**: Direction et amplitude du flottement.

## Bonuses

- **experience (int)**: Quantité d'expérience que le collectable fournit lorsqu'il est ramassé.
- **health (int)**: Quantité de santé que le collectable restaure lorsqu'il est ramassé.

## Méthodes

### Start

Initialise les propriétés de base de l'objet collectable, en définissant sa position initiale et un décalage aléatoire pour l'animation de flottement.

### Update

Contrôle le comportement du collectable à chaque image rendue. Si une cible est définie, le collectable se déplace vers cette cible. S'il n'y a pas de cible, il effectue une animation de flottement autour de sa position initiale.

### Collect

```csharp
public virtual bool Collect(PlayerStats target, float speed, float lifespan = 0f)
```

Définit la cible et la vitesse de déplacement du collectable, et ajuste éventuellement sa durée de vie. Détruit l'objet après la durée spécifiée. Retourne `true` si le collectable n'avait pas déjà une cible, sinon `false`.

### OnDestroy

S'assure que les bonus (expérience et santé) sont appliqués à la cible lorsque l'objet collectable est détruit, si une cible est présente.

## Utilisation

- Créez un prefab pour l'objet collectable et attachez-y ce script.
- Configurez les propriétés exposées dans l'inspecteur, telles que `experience`, `health`, `speed`, et les paramètres de `BobbingAnimation`.
- Utilisez la méthode `Collect` pour activer le collectable lorsqu'un joueur interagit avec lui, lui permettant ainsi de se diriger vers le joueur et d'appliquer les bonus.