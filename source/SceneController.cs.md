# Documentation de la Classe `SceneController`

## Description

La classe `SceneController` est conçue pour gérer les transitions entre les scènes et les actions relatives à l'application, comme la fermeture du jeu. Elle fournit des méthodes simples pour charger une nouvelle scène et quitter l'application.

## Fonctionnalités

- **Changement de scène** : Permet de charger n'importe quelle scène par son nom.
- **Quitter l'application** : Gère l'arrêt de l'application.

## Méthodes

### SceneChange

Charge une nouvelle scène en utilisant le nom fourni. Cette méthode rétablit également la vitesse du temps à 1, assurant que le jeu revienne à la normale après des pauses ou des ralentissements.

```csharp
public void SceneChange(string name)
{
    SceneManager.LoadScene(name);
    Time.timeScale = 1;
}
```

### ApplicationQuit

Ferme l'application.
```csharp
public void ApplicationQuit()
{
    Debug.Log("Fermeture");
    Application.Quit();
}
```


### Configuration

1. **Attachement du script** : Attachez ce script à un GameObject dans votre scène Unity.
2. **Configuration des boutons** : Liez les méthodes `SceneChange` et `ApplicationQuit` aux événements de clic de boutons dans l'interface utilisateur pour permettre aux utilisateurs de naviguer entre les scènes ou de quitter le jeu.

### Exemple d'implémentation dans l'UI

Vous pouvez configurer un bouton dans l'interface utilisateur pour quitter le jeu :

```csharp
public Button quitButton;

void Start()
{
    quitButton.onClick.AddListener(SceneController.Instance.ApplicationQuit);
}
```

Et un autre pour changer de scène :

```csharp
public Button startButton;

void Start()
{
    startButton.onClick.AddListener(() => SceneController.Instance.SceneChange("GameScene"));
}
```
