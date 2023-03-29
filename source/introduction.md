
# Introduction

Ce document a pour vocation de vous présenter les principaux outils disponibles
dans le système de documentation Sphinx pour la rédaction d'un travail de
maturité en informatique à l'aide de la syntaxe MyST/Markdown.

Le système de documentation Sphinx est le système utilisé par la communauté
Python pour documenter l'écosystème Python, en particulier le langage Python
ainsi que les principales bibliothèques qui y sont liées.

## Le système de documentation Sphinx

Le système Sphinx est lui-même développé en Python et a, depuis sa création, été
adopté bien plus largement que dans la communauté Python, en particulier dans la
communauté du logiciel libre, afin de documenter les bibliothèques, frameworks.
Le système Sphinx a même été utilisé pour rédiger des thèses de doctorat.

Il fonctionne un peu sur le même principe que LaTeX, à savoir que le contenu est
rédigé dans des documents textes suivant une syntaxe particulière. Le système
Sphinx fonctionne avec plusieurs syntaxes différentes, dont le format
RestructuredText qui est le format original et le format Markdown/MyST qui a été
ajouté par la suite. Le format Markdown est de loin le plus populaire des deux
sur le Web, raison pour laquelle nous allons présenter la rédaction d'un travail
avec la syntaxe Markdown.

## Forces de Sphinx

Sphinx ayant été créé pour rédiger des documentations, il est particulièrement
mieux adapté que Microsoft Word pour rédiger des textes liés à des projets
logiciels. Il permet notamment les avantages suivants:

- Versionnage du contenu avec git pour éviter toute perte d'information
- Intégration très puissante de code source depuis des fichiers de programme
  externes
- Génération d'une version HTML pour publier le travail en ligne
- Génération d'un à partir du même contenu grâce au système LaTeX
- Possibilité de déclarer ses propres directives (en Python) pour insérer des
  types de contenus personnalisés.

## Faiblesses de Sphinx

Le système Sphinx présente aussi quelques désavantages par rapport à Microsoft
Word.

- On ne voit pas immédiatement le résultat du travail. Il faut en effet une
  étape de compilation pour générer le site au format HTML ou le document PDF.

- Les outils de correction linguistiques ne sont de loin pas aussi points que
  dans Microsoft Word. On peut toutefois contourner cette limitation en
  important le contenu dans Word et en utilisant son correcteur linguistique.

- La prise en main de Sphinx demande un certain effort et il n'est pas possible
  de rédiger le travail en dernière minute.