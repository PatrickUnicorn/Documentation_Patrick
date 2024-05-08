# Documentation de la Classe `PlayerAnimator`

## Description

La classe `PlayerAnimator` contrôle les animations du joueur en fonction de ses mouvements et gère également la direction du sprite. Elle utilise le composant `Animator` pour activer ou désactiver les états d'animation basés sur les actions du joueur.

## Composants Requis

- **Animator (am)**: Gère les animations du joueur.
- **PlayerMovement (pm)**: Référence au script qui gère le mouvement du joueur, utilisé pour obtenir les directions et l'état de mouvement du joueur.
- **SpriteRenderer (sr)**: Utilisé pour modifier l'orientation du sprite en fonction de la direction du mouvement.

## Méthodes

### Start

Initialise les composants en récupérant les références nécessaires via `GetComponent`:
- `Animator` pour gérer les animations.
- `PlayerMovement` pour accéder aux informations de mouvement.
- `SpriteRenderer` pour ajuster visuellement le sprite en fonction de la direction.

### Update

Mise à jour des animations et de l'orientation du sprite à chaque frame, basée sur le mouvement du joueur :
- Si le joueur se déplace (`pm.moveDir.x` ou `pm.moveDir.y` différent de zéro), l'animation de mouvement est activée (`"Move"` est réglé sur `true`) et `SpriteDirectionChecker` est appelé pour ajuster l'orientation du sprite.
- Si le joueur ne se déplace pas, l'animation de mouvement est désactivée (`"Move"` est réglé sur `false`).

### SpriteDirectionChecker

Vérifie la dernière direction horizontale (`pm.lastHorizontalVector`) pour déterminer si le sprite doit être retourné :
- Si `lastHorizontalVector` est inférieur à zéro, le sprite est retourné horizontalement (`sr.flipX` est réglé sur `true`).
- Si `lastHorizontalVector` est supérieur ou égal à zéro, le sprite n'est pas retourné (`sr.flipX` est réglé sur `false`).

## Utilisation

Attachez ce script à l'objet joueur dans la scène Unity. Assurez-vous que l'objet possède également les composants `Animator`, `PlayerMovement`, et `SpriteRenderer`. Ce script fonctionne en tandem avec `PlayerMovement` pour répondre visuellement aux inputs du joueur et refléter ses actions via les animations et l'orientation du sprite.

