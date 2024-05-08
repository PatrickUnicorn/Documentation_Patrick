# Documentation de la Classe `Projectile`

## Description

La classe `Projectile` étend `WeaponEffect` pour gérer le comportement des projectiles dans un jeu. Elle contrôle le mouvement, l'orientation, la détection des cibles, et les interactions de collision des projectiles, tels que des balles ou des flèches, en utilisant les statistiques fournies par l'arme parente.

## Propriétés

- **damageSource (DamageSource)**: Enumération indiquant si les dégâts sont infligés par le projectile lui-même ou par son propriétaire (lanceur de l'arme).
- **hasAutoAim (bool)**: Indique si le projectile doit ajuster automatiquement sa trajectoire vers une cible.
- **rotationSpeed (Vector3)**: Vitesse de rotation appliquée au projectile, utile pour les projectiles qui doivent tourner en vol.
- **rb (Rigidbody2D)**: Référence au Rigidbody2D pour la gestion des propriétés physiques du projectile.
- **piercing (int)**: Nombre de fois que le projectile peut traverser des ennemis avant d'être détruit.

## Méthodes

### Start

Initialise les propriétés du projectile, ajuste sa vitesse et sa direction basées sur les statistiques de l'arme, et configure sa taille en fonction de la zone d'effet de l'arme. Si le projectile a une durée de vie limitée, il est programmé pour se détruire après cette période.

### AcquireAutoAimFacing

Ajuste la rotation du projectile pour viser automatiquement une cible ennemie. Si aucune cible n'est disponible, le projectile peut choisir une direction aléatoire.

### FixedUpdate

Gère le mouvement continu du projectile, appliquant la vitesse de translation et la rotation basées sur les statistiques de l'arme.

### OnTriggerEnter2D

Gère les interactions lors des collisions avec des ennemis ou des objets cassables. Applique les dégâts, joue des effets visuels, et réduit le compteur de percement. Si le projectile a fini son nombre de percements, il est détruit.

## Utilisation

Attachez ce script à un prefab de projectile destiné à être instancié par une arme. Configurez les propriétés `damageSource`, `hasAutoAim`, et `rotationSpeed` dans l'inspecteur Unity selon les besoins spécifiques du projectile. Assurez-vous que le prefab possède un `Rigidbody2D` configuré correctement pour le type de mouvement désiré (dynamique pour des projectiles affectés par la physique, cinématique pour des mouvements contrôlés par script).
