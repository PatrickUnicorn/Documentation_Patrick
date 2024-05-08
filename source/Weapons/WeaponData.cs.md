# Documentation de `WeaponData`

## Description

`WeaponData` est une classe dérivée de `ItemData`, conçue pour stocker et gérer les informations de configuration des armes dans un jeu de type rogue-like. Cette classe est utilisée pour définir les statistiques de base de l'arme, ainsi que sa croissance linéaire et aléatoire au fur et à mesure que l'arme monte de niveau.

## Propriétés

- **behaviour (string)**: Identifie le type de comportement ou la classe spécifique de l'arme. Utilisé pour instancier dynamiquement des armes avec des comportements différents.
- **baseStats (Weapon.Stats)**: Statistiques de base de l'arme, utilisées au niveau 1.
- **linearGrowth (Weapon.Stats[])**: Tableau de croissance linéaire des statistiques de l'arme, appliqué à chaque niveau successif jusqu'à épuisement de la liste.
- **randomGrowth (Weapon.Stats[])**: Tableau de croissance aléatoire des statistiques qui peut être sélectionné une fois que la croissance linéaire est complète.

## Méthodes

### GetLevelData

Renvoie les données de l'arme pour un niveau spécifique. Cette méthode choisit entre les croissances linéaire et aléatoire basées sur le niveau actuel de l'arme :

```csharp
public override Item.LevelData GetLevelData(int level)
```

- **Niveau 1**: Retourne les `baseStats`.
- **Croissance Linéaire**: Utilisée pour les niveaux suivants tant qu'il y a des entrées dans `linearGrowth`.
- **Croissance Aléatoire**: Utilisée après l'épuisement de la croissance linéaire, si disponible. Sélectionne aléatoirement parmi `randomGrowth`.
- **Avertissement**: Si aucune donnée de croissance n'est disponible pour un niveau donné, un avertissement est généré et des statistiques par défaut sont retournées.

## Utilisation

1. **Création de l'Objet de Données** :
   - Créez un nouvel asset de type `WeaponData` via le menu "Create -> Rogue-like/Weapon Data" dans l'éditeur Unity.
   - Configurez les propriétés dans l'inspecteur Unity, y compris les `baseStats`, `linearGrowth`, et `randomGrowth`.

2. **Intégration avec des Armes** :
   - Lors de l'instanciation d'une arme dans le jeu, utilisez les données de `WeaponData` pour initialiser et configurer l'arme selon le niveau approprié.

3. **Gestion des Montées de Niveau** :
   - Lorsque l'arme monte de niveau, utilisez `GetLevelData` pour obtenir les nouvelles statistiques et appliquez-les à l'arme.
