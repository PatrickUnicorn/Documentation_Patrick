# Documentation de la Classe `PropRandomizer`

## Description

La classe `PropRandomizer` est conçue pour placer aléatoirement des objets décoratifs (props) à des points prédéfinis dans la scène. Cela permet de varier l'aspect visuel des environnements de jeu sans nécessiter une configuration manuelle pour chaque instance de jeu.

## Propriétés

- **propSpawnPoints (List<GameObject>)**: Liste des points où les props peuvent être générés. Ces points déterminent les positions auxquelles les props seront placés.
- **propPrefabs (List<GameObject>)**: Liste des prefabs de props qui peuvent être instanciés. Un prefab sera choisi aléatoirement pour chaque point de spawn lors de la génération.

## Méthodes

### Start

La méthode `Start` est appelée lors de l'initialisation de l'instance de script. Elle appelle la méthode `SpawnProps` pour commencer la génération des props dès que le jeu commence.

### SpawnProps

```csharp
void SpawnProps()
```

Cette méthode parcourt tous les points de spawn listés dans `propSpawnPoints` et, pour chaque point, elle sélectionne aléatoirement un prefab de prop à partir de `propPrefabs`. Un prop est ensuite instancié à la position du point de spawn.

## Utilisation

### Configuration

1. **Attachement du script**: Attachez ce script à un GameObject dans votre scène Unity, idéalement à un objet qui sert de conteneur pour tous les points de spawn.
2. **Assignation des points de spawn**: Ajoutez les GameObjects qui servent de points de spawn à la liste `propSpawnPoints`. Ces objets déterminent où les props seront placés dans la scène.
3. **Ajout des prefabs de props**: Assurez-vous que tous les prefabs de props que vous souhaitez utiliser sont ajoutés à la liste `propPrefabs`. Ces prefabs sont les objets qui seront instanciés aléatoirement aux points de spawn.


