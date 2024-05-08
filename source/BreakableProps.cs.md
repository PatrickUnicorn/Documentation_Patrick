# Documentation de la Classe `BreakableProps`

## Description

La classe `BreakableProps` est conçue pour gérer les propriétés destructibles dans un jeu comme des éléments de l'environnement qui peuvent être endommagé et détruit. Cette classe fournit une méthode simple pour infliger des dégâts et gérer la destruction de ces objets.

## Propriétés

- **health (float)**: Santé actuelle de l'objet. Une fois que cette valeur atteint zéro ou descend en dessous, l'objet est considéré comme détruit.

## Méthodes

### TakeDamage

Cette méthode permet d'infliger des dégâts à l'objet :

```csharp
public void TakeDamage(float dmg)
{
    health -= dmg;

    if (health <= 0) 
    {
        Kill();
    }
}
```

### Kill

Détruit l'objet lorsque sa santé est épuisée :

```csharp
public void Kill()
{
    Destroy(gameObject);
}
```

### Configuration

1. **Créer un GameObject** : Créez un GameObject dans Unity qui représente un élément destructible.
2. **Attacher le script** : Attachez le script `BreakableProps` à ce GameObject.
3. **Configurer la santé** : Définissez la propriété `health` dans l'inspecteur Unity pour déterminer combien de dégâts l'objet peut supporter avant d'être détruit.
