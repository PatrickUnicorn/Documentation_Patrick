# Documentation de la Classe `EnemyStats`

## Description

`EnemyStats` est une classe destinée à gérer les statistiques et les comportements de base des ennemis. Elle intègre les fonctionnalités de gestion de la santé, des dégâts, de la vitesse de mouvement, et des réactions aux dommages, tels que le clignotement lorsqu'ils sont touchés et une disparition progressive à leur mort.

## Fonctionnalités

- **Gestion de la santé et des dégâts** : Stocke et met à jour la santé et les dégâts de l'ennemi basés sur des données externes (`EnemyScriptableObject`).
- **Effets visuels de réaction aux dommages** : Change temporairement la couleur de l'ennemi pour indiquer un impact.
- **Animation de mort** : Fade out progressif de l'ennemi avant sa destruction.
- **Réaction au knockback** : Applique une force de recul lorsque l'ennemi subit des dégâts.

## Propriétés

- **enemyData (EnemyScriptableObject)** : Référence aux données statiques de l'ennemi, telles que la santé maximale, la vitesse de déplacement et les dégâts.
- **currentMoveSpeed, currentHealth, currentDamage (float)** : Valeurs actuelles de vitesse, santé, et dégâts de l'ennemi.
- **damageColor (Color)** : Couleur affichée lorsque l'ennemi est touché.
- **damageFlashDuration, deathFadeTime (float)** : Durées du clignotement lors d'un coup reçu et de la disparition à la mort.

## Méthodes

### TakeDamage

Inflige des dégâts à l'ennemi et gère les réactions:

```csharp
public void TakeDamage(float dmg, Vector2 sourcePosition, float knockbackForce = 5f, float knockbackDuration = 0.2f)
```

- Applique un effet de recul.
- Déclenche un effet de clignotement pour indiquer le coup reçu.
- Affiche la quantité de dégâts infligés au-dessus de l'ennemi.

### Kill

Gère la logique de destruction de l'ennemi, y compris un effet de disparition progressive.

### OnCollisionStay2D

Détecte les collisions continues avec le joueur et inflige des dégâts si l'ennemi touche le joueur.

## Utilisation

Cette classe doit être attachée à chaque objet ennemi dans la scène qui nécessite une gestion des statistiques et des interactions de base comme les dommages et la mort. Assurez-vous que chaque ennemi a une instance de `EnemyScriptableObject` configurée pour définir ses caractéristiques.

### Configuration

1. **Attachement du script** : Attachez ce script à un GameObject représentant un ennemi.
2. **Configuration de `EnemyScriptableObject`** : Associez un `EnemyScriptableObject` approprié dans l'inspecteur Unity pour définir les caractéristiques initiales de l'ennemi.
