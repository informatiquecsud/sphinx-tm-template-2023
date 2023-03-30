# Directives et roles Sphinx

Les directives et les roles sont des constructions permettant d'intégrer dans le
document des éléments tels que des bouts de code, des tableaux, des figures, des vidéos Youtube et quantité d'autres éléments.

```{note}
Les principales directives Sphinx sont présentées (avec la syntaxe RestructuredText) dans le document https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html.
```

## Les directives

Le système Sphinx met à disposition de nombreuses directives permettant
d'intégrer des éléments dans la documentation. Si l'on fait un parallèle avec le
HTML, les directives correspondent à des balises `<div>` et créent un nouveau
bloc pouvant contenir un contenu quelconque très complexe. La correspondance
entre la syntaxe RestructureText utilisée dans la documentation Sphinx et la
syntaxe Mardown/MyST est indiquée sur la page
https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html.

La directive `figure` est l'une des plus largement utilisées en Sphinx et permet
d'insérer des images dans le document. Par l'exemple, la figure
{ref}`figure-moleson` a été produite avec le code suivant:

(figure-moleson)=

```{figure} https://upload.wikimedia.org/wikipedia/commons/d/de/Moleson.jpg
:width: 70%
:align: center

Le Moléson dans toute sa splendeur
```

## Les roles

Les roles correspondent davantage à la balise `<span>` et permettent d'intégrer
des éléments directement dans le texte. Les roles très importants à maîtriser sont

- `ref` pour insérer des références croisées (notamment sur des images ou des titres (chapitres, sections, ...))
- `cite:p` qui permet de citer les références bibliographiques intégrées dans la
  bibliographiques
- `math` pour insérer des formules mathématiques au fil du texte

## Pour aller plus loin

La documentation concernant les roles et les directives se trouve sur la page
https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html