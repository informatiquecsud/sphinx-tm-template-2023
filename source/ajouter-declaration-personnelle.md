(ajouter_declaration_personnelle)=

# Ajouter la déclaration personnelle {bdg-warning}`Mis à jour 30 mars 13:33`

```{warning} 
Cette section comportait une erreur et a été mis à jour.
```

Dans cette section, nous allons voir comment ajouter la déclaration personnelle
directement dans le fichier Sphinx sans devoir faire des scans compliqués.

`````{only} html
````{figure} figures/capture-declaration.png
:align: center
:width: 80%

Résultat final dans le PDF de la déclaration personnelle
````
`````

Pour ajouter la déclaration personnelle, vous pouvez simplement prendre le code
du fichier `source/declaration-honneur.md` ci-dessous qui va automatiquement
remplir les champs demandés dans la déclaration personnelle avec les
informations que vous avez fournies dans le fichier `source/tmconfig.py`:

````{literalinclude} declaration-honneur.md
---
caption: source/declaration-honneur.md
language: md
emphasize-lines: 1-3
---
````

```{note}
Vous constatez que le fichier `declaration-honneur.md` est un mélange de MyST/Markdown et de LaTeX. N'allez pas essayer de modifier ce fichier si vous ne savez pas ce que vous faites. Vous pouvez le prendre tel quel.
```


```{attention}
Les lignes 1-3 mises en évidence doivent être présentes si la déclaration personnelle est la première annexe. Dans le cas contraire, il faut supprimer ces lignes et les placer au tout début de la première annexe.
```

