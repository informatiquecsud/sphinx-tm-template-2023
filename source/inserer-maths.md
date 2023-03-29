(inserer-maths.md)=

# Insérer des mathématiques

## Formules directement dans le texte

On peut facilement insérer des mathématiques directement dans le texte en
mettant du code LaTeX entre dollars simples `$`.

````{admonition} Exemple

Pour insérer les formules directement dans le texte comme ceci : 
$\sin^2(x) + \cos^2(x) = 1$

Voici le code:

```md
Pour insérer les formules directement dans le texte comme ceci : 
$\sin^2(x) + \cos^2(x) = 1$
```


````

## Formules mises en évidence hors du texte

Pour mettre des formules au format "display", il faut utiliser les doubles dollars `$$` comme délimiteurs de la formule LaTeX.



````{admonition} Exemple

Pour insérer la formule en évidence comme ceci

$$\sin^2(x) + \cos^2(x) = 1$$

on utilise le code 

```md
Pour insérer les formules directement dans le texte comme ceci : 

$$\sin^2(x) + \cos^2(x) = 1$$
```


````