(ajouter_annexes)=

# Ajouter des annexes

Pour ajouter un annexe, il suffit d'ajouter un nouveau chapitre à la fin de la
table des matières dans le fichier `index.rst`.

## Exemple de la déclaration sur l'honneur

Nous prendrons l'exemple de la déclaration sur l'honneur. Pour cela, il suffit
de rajouter l'entrée `declaration-honneur.md` à la fin du toctree (après la conclusion et les références).

```{code-block} rst
---
emphasize-lines: 12
caption: source/index.rst
---
..  toctree::
    :maxdepth: 2
    :caption: Table des matières

    introduction.md
    mise-en-route.md
    directives-roles-sphinx.md
    inserer-code.md
    annexes.md
    conclusion.md
    references.rst
    declaration-honneur.md
```

Pour que ce nouveau chapitre ajouté apparaisse comme une annexe dans le document
PDF, il faut encore ajouter un code LaTeX spécial qui fait comprendre à LaTeX
qu'à partir de ce moment, tous les chapitres sont en fait des annexes.


`````{admonition} Code magique pour passer aux annexes
Le code suivant doit être rajouté au **début de la première annexe**:


````md
```{raw} latex
\appendix
```
````

Ce code a pour effet d'ajouter le code `\appendix` directement dans le document LaTeX généré par Sphinx.

`````

## Ajouter la déclaration personnelle

Le chapitre {ref}`ajouter_declaration_personnelle` indique le contenu à insérer
dans le fichier `source/declaration-honneur.md` pour ajouter la déclaration personnelle sur l'honneur directement dans votre document.