# Documentation de la Classe `WeaponDataEditor`

## Description

La classe `WeaponDataEditor` est un éditeur personnalisé pour Unity, conçu pour améliorer l'interface de l'inspecteur pour les objets `WeaponData`. Cet éditeur offre une interface utilisateur plus intuitive pour sélectionner et assigner des comportements spécifiques aux armes dans le jeu, en utilisant une liste déroulante pour choisir parmi les sous-types d'armes disponibles.

## Fonctionnalités

- **Sélection dynamique de sous-types** : Permet de choisir parmi des sous-classes de `Weapon` disponibles dans le projet, facilitant l'assignation de comportements spécifiques aux armes.
- **Liste déroulante pour les comportements** : Fournit une interface claire pour sélectionner le comportement de l'arme, améliorant ainsi l'expérience de configuration des données de l'arme.

## Propriétés

- **weaponData (WeaponData)** : Référence à l'objet `WeaponData` actuellement sélectionné dans l'éditeur.
- **weaponSubtypes (string[])** : Tableau contenant les noms des sous-types de `Weapon` disponibles pour assignation.
- **selectedWeaponSubtype (int)** : Index du sous-type sélectionné dans `weaponSubtypes`.

## Méthodes

### OnEnable

Initialise le `WeaponDataEditor` en récupérant et listant toutes les sous-classes de `Weapon`. Cette méthode est appelée lorsque l'éditeur est activé, ce qui inclut les moments où l'objet ciblé est sélectionné ou lorsque Unity est démarré.

### OnInspectorGUI

Définit l'interface utilisateur personnalisée pour l'inspecteur. Cette méthode remplace l'inspecteur par défaut pour `WeaponData` et affiche une liste déroulante permettant de sélectionner le comportement de l'arme. Elle permet également de sauvegarder les modifications directement, garantissant que les changements sont persistants.

### Configuration

1. **Attachement à `WeaponData`** : Le script `WeaponDataEditor` doit être placé dans un dossier `Editor` dans votre projet Unity pour qu'il soit correctement reconnu comme un éditeur de script.
2. **Sélection des sous-types d'arme** : Utilisez la liste déroulante dans l'inspecteur pour sélectionner le comportement désiré pour l'arme.

