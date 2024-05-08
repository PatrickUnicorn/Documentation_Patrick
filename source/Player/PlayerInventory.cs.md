# Documentation de la Classe `PlayerInventory`

## Description

La classe `PlayerInventory` gère l'inventaire du joueur, en incluant la gestion des objets d'équipement comme les armes et les objets passifs. Elle permet l'ajout, la suppression, et la mise à niveau de ces objets, tout en interagissant avec les interfaces utilisateur correspondantes pour refléter les changements.

## Composants Requis

- **PlayerStats**: Référence aux statistiques du joueur, nécessaire pour les interactions et les recalculages suite aux changements dans l'inventaire.
- **UIInventoryIconsDisplay**: Composants d'interface utilisateur pour afficher les armes et les passifs dans l'inventaire.
- **UIUpgradeWindow**: Fenêtre d'interface utilisateur pour gérer les mises à niveau disponibles lors des sélections d'upgrades.

## Propriétés

- **weaponSlots, passiveSlots (List<Slot>)**: Listes contenant les emplacements pour les armes et les passifs. Chaque emplacement peut contenir un objet de type `Item`.
- **availableWeapons, availablePassives (List<ItemData>)**: Listes des données d'objets disponibles qui peuvent être ajoutées à l'inventaire.
- **upgradeWindow (UIUpgradeWindow)**: Référence à l'interface utilisateur qui gère les fenêtres de mise à niveau.

## Méthodes Internes

### Start

Initialise les composants nécessaires au démarrage (Dans ce cas-ci, c'est PlayerStats).

### Get, Add, Remove

- **Get(ItemData type)**: Récupère un objet dans l'inventaire basé sur ses données.
- **Add(ItemData data)**: Ajoute un objet à l'inventaire en créant une instance de l'objet et en l'assignant à un emplacement disponible.
- **Remove(ItemData data, bool removeUpgradeAvailability)**: Supprime un objet de l'inventaire et, optionnellement, de la liste des améliorations disponibles.

### LevelUp

- **LevelUp(ItemData data)**: Tente de monter de niveau un objet spécifique dans l'inventaire.
- **LevelUp(Item item)**: Effectue la montée de niveau d'un objet, en appliquant les changements nécessaires et en recalculant les statistiques du joueur si nécessaire.

### ApplyUpgradeOptions

Gère la logique pour déterminer quelles options de mise à niveau présenter à l'utilisateur lors de la sélection des améliorations.

### RemoveAndApplyUpgrades

Appelée pour appliquer les options de mise à niveau et potentiellement supprimer les objets existants lors de la mise à niveau.

## Utilisation

### Gestion de l'Inventaire

La classe `PlayerInventory` est utilisée pour gérer dynamiquement les objets que le joueur peut collecter et utiliser tout au long du jeu. Elle est essentielle pour les systèmes de jeu où les joueurs peuvent changer d'équipement ou nécessitent des mises à niveau pour progresser.

### Interaction avec l'UI

L'inventaire interagit directement avec l'interface utilisateur pour mettre à jour les affichages des objets et gérer les fenêtres d'upgrade, assurant ainsi que l'interface utilisateur reste synchronisée avec l'état actuel de l'inventaire du joueur. (Bug où les objets passifs ne s'affiche pas n'est pas encore corriger mais c'est en cours)
