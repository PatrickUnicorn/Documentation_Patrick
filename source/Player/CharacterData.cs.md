# Documentation de la Classe `CharacterData`

## Description

La classe `CharacterData` est un `ScriptableObject` dans Unity, conçu pour stocker des données configurables pour des personnages dans des jeux de type rogue-like. Cela permet de facilement ajuster et réutiliser les configurations de personnages sans modifier le code.

## Propriétés

### Générales

- **Icon (Sprite)**: Icône représentative du personnage, visible dans l'UI du jeu.
- **Animator (RuntimeAnimatorController)**: Contrôleur d'animation qui gère les animations du personnage.
- **Name (string)**: Nom du personnage.
- **StartingWeapon (WeaponData)**: Arme initiale que le personnage possède au début du jeu.

### Statistiques

- **Stats (struct)**: Structure contenant diverses statistiques qui définissent les capacités et les attributs du personnage. Ces statistiques incluent :

  - **maxHealth (float)**: Santé maximale du personnage.
  - **recovery (float)**: Taux de récupération de santé.
  - **armor (float)**: Valeur de l'armure pour la réduction des dégâts.
  - **moveSpeed (float)**: Vitesse de déplacement du personnage.
  - **might (float)**: Puissance d'attaque ou d'impact.
  - **area (float)**: Taille de l'aire d'effet des attaques.
  - **speed, duration, amount, cooldown (float)**: Attributs divers affectant la vitesse, la durée des effets, le nombre d'attaques ou d'effets simultanés, et les temps de recharge.
  - **luck, growth, greed, curse (float)**: Statistiques spéciales influençant la chance, la progression, l'acquisition de ressources et les malédictions. (Pas tous implémenter)
  - **magnet (float)**: Portée d'attraction pour collecter des objets à distance.
  - **revival (int)**: Capacité de résurrection ou nombre de vies supplémentaires. (pas implémenter)

### Opérateur

- **operator + (Stats, Stats)**: Un opérateur surchargé qui permet d'additionner deux structures `Stats`, facilitant la mise à jour et la combinaison des statistiques du personnage avec des équipements ou des bonus.

## Utilisation

### Création de `CharacterData`

1. **Création d'une instance**: Dans Unity, cliquez droit dans l'onglet 'Asset' , sélectionnez "Create -> Rogue-like/Character Data" pour créer une nouvelle instance de `CharacterData`.
2. **Configuration**: Assignez les valeurs des propriétés via l'inspecteur Unity, telles que l'icône, le nom, l'arme de départ, et initialisez les valeurs des statistiques comme désiré.


## Configuration dans Unity

Pour faciliter la création et la gestion de ces données, `CharacterData` est décoré avec l'attribut `CreateAssetMenu`, permettant de créer facilement des instances de ce type via le menu de l'éditeur Unity.

