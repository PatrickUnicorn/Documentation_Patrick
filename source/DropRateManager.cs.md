# Documentation de la Classe `DropRateManager`

## Description

La classe `DropRateManager` est conçue pour gérer la logique de distribution d'objets (drops) dans un jeu. Elle permet de spécifier différents objets avec leurs taux de chute respectifs et s'occupe de la génération d'objets à la destruction de l'entité à laquelle elle est attachée.

## Structure des Données

- **Drops**: Une classe interne qui contient les détails de chaque objet potentiel à larguer, y compris le nom de l'objet, le prefab correspondant, et le taux de chute (drop rate).

## Propriétés

- **drops (List<Drops>)**: Liste des objets potentiels à larguer, avec leurs taux de chute.

## Méthodes

### OnDestroy

Cette méthode est appelée lorsque l'objet auquel ce script est attaché est détruit. Elle effectue les actions suivantes :

1. **Vérification de la Scène**: Assure que l'objet est détruit dans une scène chargée pour éviter des comportements inattendus lors du changement de scène ou lors du déchargement.
2. **Sélection des Objets à Larguer**: Détermine quels objets peuvent être largués en fonction de leurs taux de chute et d'un nombre aléatoire généré.
3. **Instantiation de l'Objet**: Si un ou plusieurs objets sont éligibles pour être largués, un objet est choisi au hasard parmi eux et instancié à la position de l'objet détruit.


### Configuration

1. **Création d'Objets Drop** : Créez des instances de la classe `Drops` dans l'inspecteur Unity pour chaque objet que vous souhaitez potentiellement larguer. Configurez le nom, le prefab de l'objet, et son taux de chute.
2. **Attachement du Script** : Attachez ce script à l'objet dans votre scène qui doit larguer des objets à sa destruction.

### Exemple de Configuration

Dans l'inspecteur Unity, vous pouvez configurer les `drops` comme suit :

- Nom : "Potion de Santé"
- Item Prefab : Référence à un prefab de potion de santé.
- Drop Rate : 25.0 (représente une probabilité de 25% de chute après la destruction de l'objet)

