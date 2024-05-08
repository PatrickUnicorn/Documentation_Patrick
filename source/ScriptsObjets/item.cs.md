# Documentation de la Classe `Item`

La classe `Item` est conçue pour gérer des objets qui peuvent évoluer ou monter de niveau. Elle est abstraite, donc elle est faite pour être étendue par d'autres classes qui définiront des types d'objets spécifiques.

## Propriétés

- **currentLevel (int)**: Niveau actuel de l'objet.
- **maxLevel (int)**: Niveau maximal que l'objet peut atteindre.
- **data (ItemData)**: Contient les infos de l'objet, comme les niveaux et les évolutions. Cette propriété n'est pas visible dans l'éditeur pour éviter des changements accidentels.
- **evolutionData (ItemData.Evolution[])**: Liste des évolutions possibles pour l'objet.
- **inventory (PlayerInventory)**: Lien vers l'inventaire du joueur. C'est là que l'objet peut accéder à d'autres objets.
- **owner (PlayerStats)**: Lien vers les stats du joueur, utile pour des calculs basés sur les attributs du joueur.

## Fonctions Principales

### Initialise

```csharp
public virtual void Initialise(ItemData data)
```
Configure l'objet avec les données nécessaires. Cela inclut le niveau max, les données d'évolution, et fait le lien avec l'inventaire et les stats du joueur via les composants parents.

### CanEvolve

```csharp
public virtual ItemData.Evolution[] CanEvolve()
```
Renvoie une liste des évolutions possibles en ce moment pour l'objet, en vérifiant si les conditions pour chaque évolution sont remplies. pour l'instant qu'une seule évolution a été programmée

### CanEvolve (Surcharge)

```csharp
public virtual bool CanEvolve(ItemData.Evolution evolution, int levelUpAmount = 1)
```
Vérifie si l'objet peut évoluer en suivant les critères spécifiques d'une évolution donnée et en prenant en compte un potentiel niveau supplémentaire.

### AttemptEvolution

```csharp
public virtual bool AttemptEvolution(ItemData.Evolution evolutionData, int levelUpAmount = 1)
```
Essaie de faire évoluer l'objet selon les règles définies. Si les conditions sont bonnes, l'objet évolue, les objets nécessaires sont consommés, et le nouvel objet est ajouté à l'inventaire.

### CanLevelUp

```csharp
public virtual bool CanLevelUp()
```
Vérifie si l'objet peut encore monter de niveau en comparant le niveau actuel au niveau max.

### DoLevelUp

```csharp
public virtual bool DoLevelUp()
```
Fait monter l'objet d'un niveau et tente les évolutions automatiques prévues.

### OnEquip et OnUnequip

Ces fonctions sont appelées quand l'objet est équipé ou retiré. Elles sont vides par défaut et peuvent être personnalisées dans les classes dérivées pour ajouter des effets spéciaux ou des changements de stats.

## Utilisation

La classe `Item` sert de base pour créer différents types d'objets. on peut créer des sous-classes pour définir des armes, des armures, ou d'autres objets interactifs, en utilisant les mécanismes de base fournis par `Item`.
