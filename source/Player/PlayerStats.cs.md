# Documentation de la Classe `PlayerStats`

## Description

La classe `PlayerStats` est conçue pour gérer toutes les statistiques pertinentes du joueur, incluant la santé, l'expérience, le niveau, et d'autres attributs comme la défense et la vitesse. Elle interagit avec divers systèmes pour mettre à jour et répondre aux changements dans les stats du joueur.

## Propriétés

- **CharacterData**: Les données de base du personnage, contenant les statistiques initiales et les configurations.
- **actualStats**: Statistiques actuelles du joueur qui peuvent évoluer en fonction des objets équipés ou d'autres effets de jeu.
- **health**: Santé actuelle du joueur.
- **experience, level, experienceCap**: Gère l'expérience accumulée, le niveau actuel du joueur et le seuil d'expérience pour le prochain niveau.

## Composants Requis

- **PlayerInventory**: Gère l'inventaire du joueur, incluant les armes et les objets passifs.
- **PlayerCollector**: Permet au joueur de collecter des objets à distance en fonction du rayon spécifié par l'attribut `magnet` des stats.

## Méthodes Principales

### Awake & Start

Initialise les composants, récupère les données du personnage et configure les valeurs initiales des stats et de la santé. Met également en place l'arme de départ du personnage.

### Update

Vérifie et gère le temps d'invincibilité après avoir subi des dégâts. Appelle la fonction de récupération de santé si nécessaire.

### RecalculateStats

Recalcule les stats du joueur en fonction des bonus fournis par les objets passifs équipés.

### IncreaseExperience

Augmente l'expérience du joueur et vérifie si cela entraîne une montée de niveau.

### LevelUpChecker

Vérifie si le joueur a atteint le seuil pour monter de niveau et ajuste les valeurs en conséquence.

### TakeDamage

Calcule les dégâts reçus après la défense, applique les effets visuels appropriés, et gère la santé du joueur.

### UpdateHealthBar, UpdateExpBar, UpdateLevelText

Met à jour les éléments d'interface utilisateur correspondants pour refléter les stats actuelles du joueur.

## Utilisation

Attachée à l'objet joueur, cette classe est essentielle pour la gestion des statistiques du joueur en interaction directe avec le jeu.
