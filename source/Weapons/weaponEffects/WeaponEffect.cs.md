# Documentation de la Classe `WeaponEffect`

## Description

La classe `WeaponEffect` sert de classe de base pour gérer les différents effets d'arme dans un jeu. Elle fournit un cadre pour définir les interactions communes à tous les types d'effets d'arme, tels que l'accès aux statistiques du propriétaire de l'arme et la détermination des dégâts infligés par l'arme.

## Propriétés

- **owner (PlayerStats)**: Référence aux statistiques du joueur qui possède l'arme. Cela permet aux effets d'arme de modifier ou de vérifier les attributs du joueur en fonction des besoins de l'effet.
- **weapon (Weapon)**: Référence à l'arme associée à cet effet. Cela permet d'accéder aux propriétés spécifiques de l'arme, comme les dégâts ou les autres caractéristiques pertinentes pour l'effet.

## Accesseurs

- **Owner**: Permet d'obtenir la référence aux statistiques du joueur propriétaire de l'arme. C'est un accès en lecture seule, car le propriétaire ne devrait pas changer une fois l'effet créé.

## Méthodes

### GetDamage

```csharp
public float GetDamage()
```
Renvoie la quantité de dégâts que l'arme est censée infliger. Cette méthode délègue simplement à la méthode `GetDamage` de l'objet `Weapon` associé, centralisant ainsi la logique de calcul des dégâts au niveau de l'arme elle-même.

## Utilisation

Cette classe doit être héritée par des classes spécifiques qui implémentent différents types d'effets d'arme, tels que les projectiles, les effets de zone, ou les buffs/debuffs. Elle fournit les méthodes et propriétés communes nécessaires pour que ces effets puissent interagir correctement avec le joueur et l'arme.

