# Documentation de la Classe `ProjectileWeapon`

## Description

`ProjectileWeapon` est une sous-classe de `Weapon` spécialisée dans la gestion des armes qui tirent des projectiles. Elle gère les intervalles entre les attaques, les angles de lancement, et la position de spawn des projectiles, tout en maintenant un suivi du nombre d'attaques restantes.

## Propriétés

- **currentAttackInterval (float)**: Durée restante avant la prochaine attaque autorisée. Utilisé pour gérer le délai entre les tirs successifs.
- **currentAttackCount (int)**: Nombre d'attaques restantes dans une rafale ou séquence avant de devoir recharger ou attendre un cooldown.

## Méthodes

### Update

Override de la méthode `Update` de la classe parent `Weapon`. Cette méthode décompte le temps jusqu'à la prochaine attaque possible et déclenche une attaque lorsque l'intervalle atteint zéro.

### CanAttack

Détermine si l'arme est actuellement capable d'attaquer. Cette méthode prend en compte `currentAttackCount` pour permettre les attaques multiples dans une rafale avant de nécessiter un cooldown.

### Attack

Implémente la logique spécifique à l'attaque pour les armes de type projectile. Cette méthode gère la création et la configuration des instances de projectile, incluant leur position, orientation, et lien avec l'arme et son propriétaire.

```csharp
protected override bool Attack(int attackCount = 1)
```

- **Validation du prefab**: Vérifie que le prefab du projectile est défini avant de continuer.
- **Gestion des attaques multiples**: Permet d'attaquer plusieurs fois en succession rapide selon le nombre spécifié par `attackCount`.
- **Création du projectile**: Instancie le projectile à la position calculée avec un angle de tir déterminé.

### GetSpawnAngle

Calcule l'angle de spawn du projectile en fonction de la dernière direction de mouvement. Cette méthode peut être surchargée pour ajuster le comportement basé sur des critères spécifiques de l'arme.

```csharp
protected virtual float GetSpawnAngle()
```

### GetSpawnOffset

Calcule un décalage de position pour le spawn du projectile. Ce décalage peut inclure une variance aléatoire pour rendre les tirs moins prévisibles.

```csharp
protected virtual Vector2 GetSpawnOffset(float spawnAngle = 0)
```


