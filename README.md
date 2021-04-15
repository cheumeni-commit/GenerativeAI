# Generative IA
Generative Dungeon Maps with IA
# Description
Ce projet réalise l'implémentation d'un IA générative de carte viable. En effet, l'IA génère une matrice 4x4 (carte d'un donjon viable) avec un point de départ, un point de sortie et une point trésor.
Le but de cette IA générative est de s'assurer de l'existence de chemin entre le point de départ (quelconque) et le point trésor (quelconque), le point de départ et le point de sortie en utilisant le Reinforcement Learning grâce à l'algorithme de Q-Learning.

![resultat de l'IA](https://github.com/cheumeni-commit/GenerativeAI/tree/master/img/generativeIA.png)

# Installation
Pour faire fonctionner cette IA generatrice, vous devez 'uploader' le projet, ensuite le dezipper. Une fois ces étapes sont réalisées:
## Requirements
Vous devez disposer des 'requirements' suivant pour deployer l'IA génératrice :
- Linux or macOS with Python ≥ 3.6
- numpy 1.20.1
- tkinter
## Installs
- Si vous êtes sur Windows, il faut disposer d'un IDE. A défaut, vous pouvez vous positionner en ligne de commande dans le reperoitre 'main' et lancer 'python GenerativeDungeonMaps.py'
- Si vous êtes sur Linux, il faut se positionner en ligne de commande dans le repertoire du projet et lancer './deploy.sh'

# ChangeLog

- V.1.0.0 : Release intiale

# Architecture utilisee:
Pour mener à bien ce projet, nous avons modélisé notre problème de la manière suivante:
- une définition des états, des actions et des récompenses
- nous avons utilisé l'équation de Bellman, le processus décisionnel de Markov pour modéliser la stochastivité et enfin l'algorithme de Q-learning.

# Citing Generative IA

Si vous utilisez ce projet pour faire des travaux de recherche et pour résoudre d'autres problèmes, merci de me citer comme suit.

```BibTeX
@misc{jmc2021GenerativeIA,
  author =       {Jean-Michel Cheumeni},
  title =        {Generative AI},
  howpublished = {\url{https://github.com/cheumeni-commit/GenerativeAI/tree/master}},
  year =         {2021}
}
```
