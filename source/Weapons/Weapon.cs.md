# Documentation de la Classe `Weapon`

## Description

La classe `Weapon` est une classe abstraite pour différents types d'armes. Elle gère les statistiques de base de l'arme, son cycle de vie, et sa logique d'attaque. C'est une classe abstraite destinée à être héritée par des classes spécifiques d'armes qui implémentent divers comportements comme les projectiles ou les auras.

## Propriétés

- **Stats**: Structure interne contenant les attributs détaillés de l'arme, tels que la puissance, la durée de vie, les effets visuels, et d'autres paramètres spécifiques.
- **currentStats (Stats)**: Statistiques actuelles de l'arme qui peuvent évoluer avec des améliorations ou des niveaux.
- **currentCooldown (float)**: Temps restant avant que l'arme ne soit à nouveau prête à être utilisée.

## Méthodes

### Initialise

Configure l'arme avec les données spécifiques fournies. Cette méthode initialise également les mouvements du joueur associés à l'arme.

### Update

Diminue le `currentCooldown` et déclenche une attaque si l'arme est prête.

### CanAttack

Vérifie si l'arme peut attaquer en fonction du cooldown actuel.

### Attack

Méthode abstraite à surcharger, gère la logique spécifique d'attaque de l'arme.

### DoLevelUp

Augmente le niveau de l'arme si possible et met à jour les statistiques en conséquence. Affiche un avertissement si l'arme a atteint le niveau maximum.

### GetDamage

Calcule les dégâts infligés par l'arme, prenant en compte la puissance de base de l'arme et les modifications potentielles apportées par les statistiques du propriétaire.

### GetArea

Calcule la zone d'effet de l'arme, utile pour les armes qui affectent plusieurs cibles ou zones.

### ActivateCooldown

Active ou réinitialise le cooldown de l'arme, en ajustant le délai en fonction des statistiques du propriétaire de l'arme.

## Utilisation

Cette classe est destinée à être étendue par des classes spécifiques qui implémentent différents types d'armes. on peut personnaliser le comportement de base en surchargeant les méthodes fournies et en utilisant les propriétés de `Stats` pour configurer les caractéristiques détaillées de chaque type d'arme.

