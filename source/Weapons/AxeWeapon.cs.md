# Documentation de la Classe `AxeWeapon`

## Description

`AxeWeapon` est une sous-classe de `ProjectileWeapon` qui spécifie le comportement d'armes de type hache, adapté pour des projectiles ayant une trajectoire ou une méthode de lancement particulière. Cette classe ajuste la manière dont les haches sont lancées, en tenant compte de l'angle et du décalage de spawn basé sur les interactions précédentes et la direction du mouvement du joueur.

## Méthodes

### GetSpawnAngle

Calcule l'angle de spawn du projectile (hache) en fonction du nombre d'attaques précédentes et de la direction de déplacement du joueur. Cette méthode permet d'ajuster dynamiquement l'angle de lancement.

```csharp
protected override float GetSpawnAngle()
{
    int offset = currentAttackCount > 0 ? currentStats.number - currentAttackCount : 0;
    return 90f - Mathf.Sign(movement.lastMovedVector.x) * (5 * offset);
}
```

- **offset**: Calculé en fonction du nombre d'attaques restantes. Cela influe sur l'angle de lancement, créant une variation selon la séquence d'attaque.
- **Mathf.Sign(movement.lastMovedVector.x)**: Détermine la direction du lancer basée sur le dernier mouvement horizontal du joueur, ajustant l'angle pour lancer l'arme soit à gauche soit à droite.

### GetSpawnOffset

Détermine un décalage aléatoire pour le point de spawn de chaque projectile, dans les limites définies par `currentStats.spawnVariance`. Cette méthode permet de varier légèrement la position d'apparition des haches pour un effet plus naturel et moins prédictible.

```csharp
protected override Vector2 GetSpawnOffset(float spawnAngle = 0)
{
    return new Vector2(
        Random.Range(currentStats.spawnVariance.xMin, currentStats.spawnVariance.xMax),
        Random.Range(currentStats.spawnVariance.yMin, currentStats.spawnVariance.yMax)
    );
}
```

- **Random.Range**: Sélectionne une valeur aléatoire entre les minimums et maximums définis pour x et y, offrant ainsi une variabilité dans le point de spawn de chaque hache lancée.

## Utilisation

Cette classe est idéale pour les armes et leur comportement qui doivent être distincts. le joueur peut choisir entre diverses armes avec des effets uniques, `AxeWeapon` est utilisée avec chaque lancer de hache.

### Configuration

Pour utiliser cette classe :
1. Attachez ce script à un GameObject représentant l'arme dans le jeu.
2. Assurez-vous que le GameObject a accès à une instance de `PlayerMovement` pour déterminer la dernière direction de déplacement du joueur.
3. Configurez les statistiques de l'arme, y compris `spawnVariance` et `number`, pour contrôler la variabilité et le nombre de projectiles générés.

