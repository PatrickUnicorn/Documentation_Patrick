# Documentation de la Classe `ChunkTrigger`

## Description

La classe `ChunkTrigger` est conçue pour gérer les transitions entre différents "chunks" ou zones de carte dans un jeu utilisant Unity. Elle détecte la présence du joueur dans une zone spécifique et met à jour une référence à la carte actuelle dans un contrôleur de carte central.

## Propriétés

- **mc (MapController)**: Référence au contrôleur de carte principal qui gère l'état actuel de la carte ou du chunk dans le jeu.
- **targetMap (GameObject)**: Le GameObject de la carte ou du chunk que ce déclencheur représente.

## Méthodes

### Start

Initialise le script en trouvant et stockant une référence au `MapController` présent dans la scène. Ceci est crucial pour que le déclencheur puisse communiquer avec le contrôleur de carte et mettre à jour la carte ou le chunk actuel.

```csharp
void Start()
{
    mc = FindObjectOfType<MapController>();
}
```

### OnTriggerStay2D

Cette méthode est appelée chaque fois qu'un Collider2D reste à l'intérieur de ce déclencheur. Si le Collider appartient au joueur (vérifié par un tag), elle met à jour le chunk actuel du `MapController` pour qu'il pointe vers le `targetMap`.

```csharp
private void OnTriggerStay2D(Collider2D col)
{
    if (col.CompareTag("Player"))
    {
        mc.currentChunk = targetMap;
    }
}
```

### OnTriggerExit2D

Cette méthode est appelée lorsque n'importe quel Collider2D quitte le déclencheur. Si le Collider appartient au joueur et si le chunk actuel est celui représenté par ce déclencheur, elle réinitialise la référence du chunk actuel dans le `MapController` à `null`.

```csharp
private void OnTriggerExit2D(Collider2D col)
{
    if (col.CompareTag("Player"))
    {
        if (mc.currentChunk == targetMap)
        {
            mc.currentChunk = null;
        }
    }
}
```

## Utilisation

1. **Attachement du script**: Attachez ce script à un GameObject dans Unity qui agit comme un déclencheur de zone pour une carte ou un chunk spécifique. Assurez-vous que ce GameObject a un Collider2D configuré comme un déclencheur (Trigger).
   
2. **Configuration**: Assurez-vous que le GameObject ciblé par `targetMap` est correctement configuré et représente la zone de la carte que ce déclencheur doit gérer. Définissez le tag du joueur sur "Player" pour que le déclencheur puisse l'identifier correctement.

3. **Intégration avec MapController**: Ce script suppose que `MapController` est déjà présent et configuré dans la scène pour gérer les différents chunks ou zones de carte.

