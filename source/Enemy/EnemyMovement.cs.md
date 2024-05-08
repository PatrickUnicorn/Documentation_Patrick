# Documentation de la Classe `EnemyMovement`

## Description

`EnemyMovement` est un script conçu pour gérer les déplacements de base d'une entité ennemie dans un jeu. Ce script contrôle le suivi du joueur et la gestion des réactions à des impacts externes, tels que les reculs (knockbacks).

## Fonctionnalités

- **Poursuite du joueur** : L'ennemi se déplace vers la position du joueur en utilisant une interpolation linéaire pour simuler un mouvement fluide.
- **Gestion du recul** : L'ennemi peut être repoussé par une force externe, interrompant temporairement sa poursuite normale.

## Composants

- **EnemyStats** : Ce composant est utilisé pour accéder aux statistiques de l'ennemi, telles que la vitesse de déplacement.
- **PlayerMovement** : Détermine la position du joueur pour diriger le mouvement de l'ennemi.

## Propriétés

- **knockbackVelocity (Vector2)** : Vitesse et direction du recul actuel.
- **knockbackDuration (float)** : Durée restante pendant laquelle l'effet de recul est actif.

## Méthodes

### Start

Initialise les composants nécessaires. Elle récupère les références aux statistiques de l'ennemi et à la position du joueur.

### Update

Gère la logique de mouvement à chaque frame. Si un recul est en cours, l'ennemi est déplacé en fonction de la `knockbackVelocity`. Sinon, l'ennemi se déplace vers le joueur à sa vitesse de déplacement actuelle.

### Knockback

Applique un vecteur de vitesse et une durée de recul à l'ennemi. Si un recul est déjà en cours, la méthode retourne immédiatement sans appliquer un nouveau recul.

```csharp
public void Knockback(Vector2 velocity, float duration)
{
    if (knockbackDuration > 0) return; 
    knockbackVelocity = velocity; 
    knockbackDuration = duration; 
}
```

## Utilisation

Attachez ce script à n'importe quel GameObject ennemi qui nécessite un mouvement contrôlé vers le joueur et une réponse aux reculs. Assurez-vous que l'ennemi a un composant `EnemyStats` et que le joueur a un composant `PlayerMovement` accessible dans la scène.

### Configuration

- Ajoutez ce script à un GameObject ennemi dans votre scène.
- Assurez-vous que le joueur est identifiable par `FindObjectOfType<PlayerMovement>()`, typiquement en attachant `PlayerMovement` au GameObject du joueur.
