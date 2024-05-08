# Documentation de la Classe `PlayerMovement`

## Description

La classe `PlayerMovement` gère les déplacements d'un personnage joueur, en utilisant le système de physique de Unity avec un `Rigidbody2D`. Elle contrôle le mouvement en réponse aux entrées de l'utilisateur et applique une vitesse de déplacement en fonction des statistiques du joueur.

## Propriétés

- **DEFAULT_MOVESPEED (int)**: La vitesse de base de déplacement du joueur, utilisée comme multiplicateur de base pour le calcul de la vitesse de déplacement réelle.
- **moveDir (Vector2)**: La direction actuelle de déplacement du joueur, basée sur les entrées de l'utilisateur.
- **lastHorizontalVector (float)**: La dernière valeur enregistrée pour le mouvement horizontal.
- **lastVerticalVector (float)**: La dernière valeur enregistrée pour le mouvement vertical.
- **lastMovedVector (Vector2)**: Le dernier vecteur de mouvement enregistré, utilisé pour conserver la direction du joueur lors de changements dans les entrées.

## Composants

- **rb (Rigidbody2D)**: Composant physique utilisé pour appliquer des forces de mouvement au joueur.
- **player (PlayerStats)**: Référence aux statistiques du joueur, utilisée pour ajuster la vitesse de mouvement selon les attributs du joueur.

## Méthodes

### Start

Initialise les références et configure les valeurs initiales. Elle récupère les composants nécessaires et initialise le vecteur de mouvement initial.

### Update

Gère les entrées utilisateur en continu et ajuste les vecteurs de mouvement en conséquence. La méthode vérifie également l'état du jeu pour arrêter les mouvements si le jeu est terminé.

### FixedUpdate

Applique le mouvement au joueur en utilisant le `Rigidbody2D`. Cette méthode est appelée à chaque pas de la simulation physique pour garantir un mouvement fluide dans le jeu.

### InputManagement

Traite les entrées de l'utilisateur pour déterminer la direction du mouvement. Elle ajuste les vecteurs de mouvement en fonction des touches pressées et met à jour les vecteurs de direction historiques pour garder une trace de la dernière direction de mouvement.

### Move

Applique la vitesse de déplacement au `Rigidbody2D` en fonction de la direction déterminée et des statistiques de vitesse du joueur.

## Utilisation

Attachez ce script à l'objet joueur dans votre scène Unity qui possède un composant `Rigidbody2D` et `PlayerStats`. Assurez-vous que le `Rigidbody2D` est configuré pour fonctionner avec des forces (par exemple, avec une gravité adaptée). Configurez les contrôles utilisateur pour correspondre aux axes "Horizontal" et "Vertical" utilisés dans `Input.GetAxisRaw`.
