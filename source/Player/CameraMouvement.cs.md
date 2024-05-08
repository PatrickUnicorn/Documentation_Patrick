# Documentation de la Classe `CameraMovement`

## Description

La classe `CameraMovement` est responsable de maintenir la caméra centrée sur un objet cible (généralement le joueur) dans un jeu Unity, avec un décalage (offset) configurable pour ajuster la perspective ou la position de la caméra par rapport à la cible.

## Propriétés

- **target (Transform)**: L'objet Transform que la caméra doit suivre. Ce sera généralement le joueur ou tout autre objet important que la caméra doit garder en vue.
- **offset (Vector3)**: Le vecteur de décalage entre la position de la caméra et la position de l'objet cible. Ce décalage permet de personnaliser la vue, par exemple pour avoir une vue légèrement surélevée ou décalée par rapport à la cible.

## Méthode

### Update

La méthode `Update` est appelée à chaque frame pour mettre à jour la position de la caméra. Elle ajuste la position de la caméra en fonction de la position de l'objet cible, tout en appliquant le décalage défini.

```csharp
void Update()
{
    transform.position = target.position + offset;
}
```

Dans cette méthode :
- La position de la caméra (`transform.position`) est définie comme étant égale à la position de la cible (`target.position`) plus le décalage (`offset`). Cela garantit que la caméra suit la cible tout en maintenant une distance ou perspective constante définie par le décalage.

## Utilisation

### Configuration

1. **Attachement du script** : Attachez ce script à l'objet de la caméra dans votre scène Unity.
2. **Assignation de la cible** : Définissez l'objet `target` dans l'inspecteur Unity en glissant le Transform de l'objet que vous souhaitez suivre (par exemple, le joueur).
3. **Réglage du décalage** : Ajustez le vecteur `offset` pour positionner la caméra relativement à la cible de manière à obtenir l'angle de vue désiré.

- **Décalage vertical** : Un décalage en y positif peut être utilisé pour donner une vue de dessus.
- **Décalage latéral** : Un décalage en x peut être utilisé pour créer une vue de côté ou pour suivre le personnage depuis un angle légèrement décalé
- **Décalage en profondeur** : Un décalage en z peut être utilisé pour ajuster la distance entre la caméra et l'objet
