# Documentation de la Classe `GameManager`

## Description

La classe `GameManager` est un contrôleur central pour la gestion des états du jeu, des interfaces utilisateur, des transitions entre les états et des éléments interactifs spécifiques tels que l'affichage de texte flottant pour les dégâts. Elle utilise le motif Singleton pour s'assurer qu'une seule instance de cette classe gère les opérations à travers toutes les scènes.

## Fonctionnalités

- **Gestion des états du jeu**: Contrôle les différents états du jeu comme le gameplay, pause, fin de jeu, et niveau supérieur.
- **Interface utilisateur**: Gère les écrans de pause, de résultats, et de montée de niveau.
- **Génération de texte flottant**: Affiche des textes flottants pour les dégâts ou autres notifications à l'écran.
- **Gestion du temps de jeu**: Comprend un chronomètre pour le suivi du temps de jeu et potentiellement des limites de temps pour certaines actions.

## Propriétés

- **instance (GameManager)**: Instance unique du GameManager pour un accès global.
- **currentState, previousState (GameState)**: États actuel et précédent du jeu pour gérer les transitions.
- **damageTextCanvas (Canvas)**: Canvas pour le rendu du texte flottant des dégâts.
- **pauseScreen, resultsScreen, levelUpScreen (GameObject)**: Écrans pour les différentes interfaces utilisateur.
- **stopwatchTime, timeLimit (float)**: Gestion du temps pour les limites de session ou d'autres événements basés sur le temps.

## Méthodes

### Méthodes de Contrôle de l'État

- **ChangeState**: Change l'état actuel du jeu.
- **PauseGame, ResumeGame**: Met en pause ou reprend le jeu.
- **GameOver**: Gère la logique de fin de jeu.

### Gestion de l'Interface Utilisateur

- **DisableScreens**: Désactive tous les écrans de l'interface utilisateur.
- **DisplayResults**: Affiche l'écran des résultats.
- **AssignChosenCharacterUI, AssignLevelReachedUI**: Assignent les informations du personnage et du niveau atteint aux éléments de l'interface utilisateur.

### Gestion des Textes Flottants

- **GenerateFloatingText**: Crée et gère l'affichage du texte flottant pour les dégâts.
- **GenerateFloatingTextCoroutine**: Coroutine qui anime le texte flottant.

### Chronomètre

- **UpdateStopwatch**: Met à jour le chronomètre du jeu.
- **UpdateStopwatchDisplay**: Met à jour l'affichage du chronomètre.

### Configuration

1. **Singleton Setup**: Assurez-vous que le script est attaché à un GameObject dans la scène initiale et marqué pour ne pas être détruit lors du chargement des scènes.
2. **UI Setup**: Liez les GameObjects des écrans de pause, de résultats, et de montée de niveau dans l'inspecteur Unity.

### Exemples de transitions d'état

```csharp
// Pour mettre le jeu en pause
GameManager.instance.PauseGame();

// Pour reprendre le jeu
GameManager.instance.ResumeGame();

// Pour terminer le jeu
GameManager.instance.GameOver();
```
