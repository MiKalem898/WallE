# Wall-E Desktop Pet
Wall-E est un compagnon de bureau interactif développé en Python. Il utilise la vision par ordinateur et l'intelligence artificielle pour observer son environnement via la webcam et réagir en temps réel aux objets et aux personnes qu'il détecte.

## Fonctionnalités
* **Animation fluide :** Utilisation de Pygame pour gérer les animations de sprites (respiration, clignements d'yeux, mouvements).
* **Vision par ordinateur :** Intégration du modèle YOLOv8 (You Only Look Once) pour la détection d'objets et de squelettes humains.
* **Interactions intelligentes :**
    * **Présence humaine :** Wall-E se réveille et suit l'utilisateur du regard lorsqu'une personne est détectée.
    * **Sommeil :** En l'absence de mouvement ou de présence humaine, le robot passe en mode économie d'énergie et s'endort.
    * **Objets :** Réagit à la présentation de nourriture (pommes, sandwichs) ou de boissons (bouteilles, tasses).
* **Performance :** Architecture multithreadée séparant le rendu graphique (Pygame) du calcul IA (YOLO) pour maintenir une fluidité d'affichage optimale.

## Prérequis
* Python 3.8 ou supérieur
* Une webcam fonctionnelle

# Contrôles
* **Quitter** : Appuyez sur la croix de la fenêtre ou sur la touche A si la fenêtre OpenCV est active (selon configuration).
* **Interaction** : Placez-vous devant la caméra ou montrez des objets (bouteille, fruit) pour voir Wall-E réagir.