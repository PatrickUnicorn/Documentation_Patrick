# Documentation de la Classe `WhipWeapon`

## Description

`WhipWeapon` est une sous-classe de `ProjectileWeapon` spécifiquement conçue pour simuler le comportement d'une arme de type fouet. Cette arme lance des projectiles qui peuvent alterner entre différents angles et hauteurs, imitant le mouvement d'un fouet.

## Propriétés

- **currentSpawnCount (int)**: Compteur indiquant le nombre de projectiles lancés durant la séquence d'attaque actuelle.
- **currentSpawnYOffset (float)**: Décalage vertical appliqué progressivement aux projectiles pour simuler le mouvement vertical du fouet.

## Méthodes

### Attack

Override de la méthode `Attack` pour implémenter la logique spécifique du fouet, incluant la gestion des décalages et des angles de spawn des projectiles.

```csharp
protected override bool Attack(int attackCount = 1)
```

- **Validation du prefab** : Vérifie si le prefab du projectile est configuré. Si non, un avertissement est affiché et un cooldown est activé.
- **Vérification de la capacité d'attaque** : S'assure que l'arme peut attaquer selon le cooldown.
- **Calcul du décalage** : Détermine le décalage horizontal et vertical pour le spawn du projectile, alternant la direction du lancement pour simuler le mouvement du fouet.
- **Création et configuration du projectile** : Instancie le projectile avec le décalage approprié et ajuste l'échelle pour les projectiles lancés dans la direction opposée.
- **Gestion des séquences d'attaque** : Incrémente les compteurs et ajuste le décalage vertical après un certain nombre de tirs.

## Utilisation

Cette classe est adaptée aux armes qui ont des comportements uniques. `WhipWeapon` peut être utilisée par des personnages qui utilisent des fouets ou des armes similaires, offrant une expérience de combat intéressante et variée.

### Configuration

Pour utiliser cette classe :
1. Attachez ce script à un GameObject représentant une arme dans votre jeu.
2. Assurez-vous que le GameObject a un prefab de projectile configuré correctement.
3. Ajustez les valeurs de `spawnVariance` pour contrôler la variabilité des points de spawn des projectiles.
