# Insérer du code source

Pour insérer du code dans le document, il faut éviter de faire des captures
d'écran du code, car cela alourdit inutilement le document. À la place, il faut
utiliser les directives spéciales telles que `code-block` ou `literalinclude`
mises à disposition par le système Sphinx.

## Code directement dans le texte

Très souvent, on doit insérer des bouts de code tels que des noms de variables
ou noms due fonctions directement dans le texte. Cela peut se faire en utilisant
les "backticks", à savoir le caractère `` ` ``. Pour produire le texte 

```{admonition} Exemples
1.  Insérer des noms de variables

    Soit `n` le nombre d'éléments dans la liste ...

    ```md
    Soit `n` le nombre d'éléments dans la liste ...
    ```

1.  Indiquer des noms de fichiers `index.html`

```

## Insérer du code très simple

Pour insérer un petit bout de code hors du texte, on peut simplement utiliser la syntaxe

````md
```python
from math import pi

print(pi)
```
````

ou, pour d'autres langages tels que le Javascript, 


````md
```js
function foo(a, b) {
    return a + b
}

console.log(foo(10, 20))
```
````

## Utilisation directives Sphinx

La syntaxe précédente est assez basique et standard en Markdown. Sphinx met à
disposition des directives plus puissantes:

- `code-block` pour insérer du code directement dans le fichier Markdown
- `literalinclude` pour inclure du code présent dans un autre fichier accessible
  par une chemin relatif par rapport au fichier Markdown dans lequel il faut inclure le code. 

### Directive `code-block`

La directive `code-block` permet d'intégrer du code sans avoir à faire une
capture d'écran. Par exemple, pour produire le code

```{code-block} python
---
linenos: true
emphasize-lines: 3
---
from math import pi

print(pi)
```

on peut utiliser la syntaxe

````md
```{code-block} python
---
linenos: true
emphasize-lines: 3
---
from math import pi

print(pi)
```
````

### Directive `literalinclude`

La directive `literalinclude` permet d'inclure du code source depuis un fichier
externe. Cela est très pratique dans les cas suivants

- Pour intégrer tout un fichier source en annexe sans avoir à copier le code
  directement dans le fichier Markdown.
- Maintenir le code inséré dans le texte à jour avec le code réellement utilisé
  dans le projet sans avoir à faire sans arrêt du copier-coller. 
- Lorsque le fichier contient beaucoup de lignes

```{note}
Les options de la directive sont listées sur la page de la documentation https://devopstutodoc.readthedocs.io/en/stable/documentation/doc_generators/sphinx/rest_sphinx/code/literalinclude/literalinclude.html#lines-xxx
```

`````{admonition} Exemple
Pour insérer les lignes 1 à 10 du fichier `conf.py` en insérant les numéros de lignes, en mettant en évidence les lignes 3 à 5 et en rajoutant la légende `requirements.txt`, il suffit d'utiliser la syntaxe suivante:

````md
```{literalinclude} requirements.txt
---
linenos: true
language: txt
lines: 1-10
emphasize-lines: 3-5
caption: requirements.txt
---
```
````

Cela produit le résultat suivant:

```{literalinclude} ../requirements.txt
---
linenos: true
language: txt
lines: 1-10
emphasize-lines: 3-5
caption: requirements.txt
---
```

`````