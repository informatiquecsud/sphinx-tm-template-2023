(mise-en-route.md)=

# Mise en route {bdg-warning}`Mis à jour 30 mars 14:23`

## Indiquer les informations personnelles 

Les informations concernant le travail de maturité doivent être indiquées dans le fichier `source/tmconfig.py`.

Voici un exemple de fichier rempli. Veillez en particulier à ce que les champs
suivants soient remplis correctement

- `title` qui indique le titre du travail de maturité sur le PDF
- `first_name` et `last_name` qui indiquent votre prénom et votre nom
- `address` qui indique votre adresse (pour la déclaration personnelle en
  annexe)
- Le champ `the_date` qui indique la date à inscrire sur la page de garde de
  votre travail


```{literalinclude} tmconfig.py

```

## Mettre à jour les fichiers de configuration



```{attention}
Des modifications ont été apportées dans les fichiers suivants pour améliorer la page de garde et permettre de générer la déclaration personnelle:

- `source/conf.py`
- `latex-templates/sphinxmanual.cls`
- `Makefile`
- `requirements.txt`

Ces fichiers doivent être mis à jour pour que tout se passe bien. Il vous suffit de copier les fichiers ci-dessous et de remplacer le code se trouvant dans vos propres fichiers. 

Attention à bien sauvegarder votre travail avant de procéder aux manipulations indiquées ci-après. Si vous faites une erreur, vous avez le pouvoir de tout faire foirer. Il vaut donc mieux pouvoir "revenir en arrière".
```

### Fichier `conf.py` {bdg-warning}`Mis à jour 30 mars 14:23`

```{warning}
Le fichier `conf.py` donné n'était pas compatible avec votre fichier `tmconfig.py` et est maintenant correct.
```

```{literalinclude} conf.py
---
caption: source/conf.py
language: python
---

```

### Fichier `sphinxmanual.cls`

```{literalinclude} ../latex-templates/sphinxmanual.cls
---
caption: latex-templates/sphinxmanual.cls
language: latex
---

```

### Fichier `Makefile`


```{literalinclude} ../Makefile
---
caption: Makefile
language: Makefile
---

```

### Fichier `requirements.txt`


```{literalinclude} ../requirements.txt
---
caption: requirements.txt
---

```

## Appliquer les changements

Une fois les fichiers mis à jour, il faut simplement pousser les modifications
sur vote dépôt GitHub, fermer gitpod et rouvrir le dépôt dans gitpod.