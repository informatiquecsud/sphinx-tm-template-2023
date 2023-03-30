(inserer-pdf.md)=

# Insérer un PDF dans le document

Pour insérer un PDF dans le document écrit imprimé, le plus simple est de
convertir le PDF en image PNG, puis d'inclure chaque page sous forme d'image
avec la balise `figure` ou `image`.

```{note}
Il existe un moyen d'inclure directement du PDF dans le document LaTeX généré par Sphinx, mais cela ne va pas tout seul. La solution proposée est la plus simple à mettre en oeuvre.
```