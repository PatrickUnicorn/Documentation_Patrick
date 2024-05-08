# Documentation de la Classe `Aura`

## Description

La classe `Aura` étend `WeaponEffect` pour implémenter un effet d'aura qui affecte les ennemis à proximité. L'aura inflige des dégâts de manière répétée aux ennemis qui entrent et restent dans son rayon d'action.

## Propriétés

- **affectedTargets (Dictionary<EnemyStats, float>)**: Stocke les ennemis actuellement affectés par l'aura ainsi que le temps restant avant le prochain dégât qu'ils subiront.
- **targetsToUnaffect (List<EnemyStats>)**: Liste des ennemis qui sont sortis de l'aura et doivent être désaffectés après un délai.

## Méthodes

### Update

À chaque frame, cette méthode vérifie chaque ennemi dans `affectedTargets` pour réduire le délai avant la prochaine application de dégâts. Si le temps est écoulé, l'ennemi reçoit des dégâts et le compteur est réinitialisé en fonction du cooldown de l'arme ajusté par les stats du propriétaire de l'arme.

### OnTriggerEnter2D

Déclenché lorsque n'importe quel `Collider2D` entre dans le trigger de l'aura. Si le collider appartient à un ennemi (`EnemyStats`), il est ajouté à `affectedTargets` s'il n'est pas déjà suivi, ou retiré de `targetsToUnaffect` s'il était marqué pour être désaffecté mais est revenu dans l'aura.

### OnTriggerExit2D

Déclenché lorsque n'importe quel `Collider2D` sort du trigger de l'aura. Si le collider appartient à un ennemi qui est actuellement affecté, cet ennemi est ajouté à `targetsToUnaffect`, indiquant qu'il devrait être retiré de `affectedTargets` une fois le délai de cooldown passé.


## Utilisation

Cette classe peut être utilisée pour créer des armes ou des objets qui ont un effet dans une zone, influençant les ennemis qui entrent et sortent de cette zone. Elle est particulièrement utile pour les scénarios où une position défensive doit être maintenue ou pour des personnages qui ont des capacités de contrôle de foule.


