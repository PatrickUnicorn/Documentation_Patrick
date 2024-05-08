# Documentation de la Classe `LightningRingWeapon`

## Description

La classe `LightningRingWeapon` étend `ProjectileWeapon` pour gérer un type d'arme qui crée des effets de zone affectant plusieurs ennemis simultanément, en particulier en imitant un anneau de foudre. Cette classe est conçue pour infliger des dégâts à un groupe d'ennemis sélectionnés autour d'une position ciblée.

## Fonctionnalités Principales

- **Sélection d'ennemis** : Sélectionne des ennemis visibles à portée pour être ciblés par l'attaque.
- **Attaque en zone** : Inflige des dégâts à tous les ennemis dans une certaine zone autour du point d'impact.
- **Gestion des effets visuels** : Utilise des effets prédéfinis pour visualiser l'impact sur les cibles.

## Méthodes

### Attack

Override de la méthode `Attack` pour lancer une attaque de type invocation de foudre. Cette méthode s'occupe de vérifier si l'arme est prête à attaquer, de sélectionner les ennemis, et d'appliquer les dégâts.

```csharp
protected override bool Attack(int attackCount = 1)
```
- **Validation des prérequis** : Vérifie si un effet visuel pour les impacts est configuré.
- **Activation de la fréquence d'attaque** : Gère les délais entre les attaques successives.
- **Sélection et attaque des cibles** : Sélectionne une cible aléatoire visible et inflige des dégâts à l'aire autour de sa position.

### PickEnemy

Sélectionne une cible aléatoire parmi les ennemis disponibles qui sont visibles à l'écran. Si un ennemi sélectionné n'est pas visible, il est retiré de la liste des candidats.

```csharp
EnemyStats PickEnemy()
```

### DamageArea

Applique des dégâts à tous les ennemis situés dans un rayon donné autour d'une position spécifiée.

```csharp
void DamageArea(Vector2 position, float radius, float damage)
```

## Utilisation

### Configuration

- **Attachement du script**: Attachez ce script à un GameObject dans Unity qui représente l'arme.
- **Configuration des effets**: Assurez-vous que les effets visuels pour les impacts sont correctement configurés dans les statistiques de l'arme (`currentStats.hitEffect`).
