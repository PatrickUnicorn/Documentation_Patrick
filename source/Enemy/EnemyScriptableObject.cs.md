# Documentation de la Classe `EnemyScriptableObject`

## Description

`EnemyScriptableObject` est une classe dérivée de `ScriptableObject`. Elle est conçue pour stocker des données réutilisables pour les ennemis dans un jeu, telles que la vitesse de déplacement, la santé maximale, et les dégâts qu'ils peuvent infliger. L'utilisation de `ScriptableObject` permet de créer des variations d'ennemis facilement modifiables et réutilisables sans dupliquer le code ou les ressources.

## Propriétés

- **MoveSpeed (float)** : Vitesse de déplacement de l'ennemi. Détermine à quelle vitesse l'ennemi peut se déplacer dans le jeu.
- **MaxHealth (float)** : Santé maximale de l'ennemi. Définit la quantité de dégâts que l'ennemi peut encaisser avant d'être vaincu.
- **Damage (float)** : Dégâts infligés par l'ennemi lorsqu'il attaque le joueur ou d'autres entités du jeu.

## Fonctionnalités

Chaque propriété est sérialisée avec `[SerializeField]` pour permettre sa modification dans l'éditeur Unity, mais est exposée publiquement via un accesseur `get` pour une lecture facile et un accesseur `private set` pour éviter des modifications non contrôlées par des scripts externes.

### Getters et Setters

Les propriétés fournissent des accès en lecture seule au reste du jeu, avec la capacité de modification restreinte uniquement à la définition initiale dans l'éditeur de Unity. Ceci assure que les attributs essentiels de l'ennemi restent cohérents et contrôlés.

## Utilisation

### Création d'une Instance de `ScriptableObject`

1. **Création dans l'Éditeur** :
   - Naviguez vers `Assets -> Create -> ScriptableObjects -> Enemy` pour créer une nouvelle instance de `EnemyScriptableObject`.
   - Nommez et configurez les propriétés de l'instance selon les besoins de votre jeu.

2. **Configuration des Propriétés** :
   - Définissez la `MoveSpeed`, la `MaxHealth`, et les `Damage` dans l'inspecteur de Unity pour personnaliser chaque type d'ennemi.

### Intégration avec des Entités Ennemies

- Attachez les données de `EnemyScriptableObject` à des ennemis dans votre jeu en référençant l'instance du `ScriptableObject` dans les scripts d'ennemis pour utiliser les valeurs de vitesse, santé, et dégâts.

```csharp
public class Enemy : MonoBehaviour
{
    public EnemyScriptableObject enemyData;

    void Start()
    {
        float speed = enemyData.MoveSpeed;
        float health = enemyData.MaxHealth;
        float damage = enemyData.Damage;
    }
}
```
