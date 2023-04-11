(test-travaux.md)=

# Test des projets

Cette section regroupe les différentes manipulations à faire pour tester les
projets. Pour tester les projets, il faut 

- un compte Github
- un compte sur la plateforme https://gitpod.io


## Capucine

:::{note}

Le travail est essentiellement un site statique. On peut donc sans problème
télécharger les fichiers depuis https://github.com/capucineboh/site-candide et l'ouvrir localement dans un navigateur. 

:::

Il faut suivre les étapes suivantes dans le workspace https://gipod.io#https://github.com/capucineboh/site-candide

1.  Ouvrir un terminal et taper la commande 

    ```bash
    python -m http.server 8000
    ```

2.  Ouvrir dans une nouvelle fenêtre du navigateur (proposé automatiquement par
    Gitpod normalement)

## Louis

Il suffit d'ouvrir le projet sur Stackblitz comme indiqué sur la page d'accueil
du dépôt Github du projet (https://github.com/Oheir/TM-site).

Projet sur Stackblitz : https://stackblitz.com/edit/vue-iuhwfl

Les liens permettant de naviguer dans les différents modules du projet ne
fonctionnent pas. Il faut remplacer le code du fichier ``App.vue`` par le code
ci-dessous pour rendre les liens fonctionnels et afficher les différents
composants:

```html
<template>
  <div id="app">
    <ul>
    <li @click="id = 0"><a href="#Congruence">Congruence Modulaire</li>
    <li @click="id = 1"><a href="#PGDC" target="_self">PGDC</a></li>
    <li @click="id = 2"><a href="#Inverse">Inverse modulaire</a></li>
  </ul>
  </div>
    <Textecongruence v-if="id === 0"/>
    <Textepgdc v-if="id === 1"/>
    <Texteinverse v-if="id === 2"/>
</template>
<script>
import Textecongruence from './components/Partie_1/TexteModulo.vue'
import Textepgdc from './components/Partie_2/Textepgdc.vue'
import Texteinverse from './components/Partie_3/Texteinverse.vue'
export default {
  name: 'App',
  components: {
    Textecongruence,
    Textepgdc,
    Texteinverse,
  },
  data() {
    return {
      id: 1
    };
  },
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
body {
  margin:0;
  background: #282828
}
ul {
  display: flex;
  justify-content: space-evenly;
  list-style-type: none;
  margin: 0;
  padding: 0;
  background-color: #1F2833;
  position: fixed;
  top: 0;
  width: 100%;
}
li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
li a:hover {
  background-color: #C5C6C7;
  color: #3500D3;
}
</style>

```


## Patrick

Ouvrir le dépôt https://github.com/PatrickUnicorn/TM-Informatique dans gitpod avec https://gitpod.io#https://github.com/PatrickUnicorn/TM-Informatique

- faire `cd TM-Informatique`
- Installer les packages du fichier "package.json" avec la commande `npm install`			
- Lancer le projet à l'aide de la commande `npm run dev`.

```{admonition} Connexion au site
:class: note

Pour se connecter au site, il faut utiliser les informations de connexion suivantes:
			
- Nom d'utilisateur: `admin`	
- Mot de passe: `admin123`
```
			
```{admonition} Accès aux composants
De manière générale, le projet est fonctionnel, mais certaines routes sont
inaccessibles en utilisant les éléments de interface de l'application. Il est
cependant possible d'y accéder en écrivant directement la bonne url dans le
navigateur:
				
- `/QCM`
				
- `/QCM2`
				
- `/TextTrou`
				
- `/triage`
				
- `/TextArea`

```
			
## Gabriel

Le fichier README du dépôt est très bien détaillé pour tester le projet en
local. Le plus simple est sans doute d'utiliser Stackblitz pour tester le
projet, avec https://stackblitz.com/edit/quasarframework-oksr1v?file=README.md```

:::{admonition} Connexion au site
:class: note

Pour se connecter au site, on peut entrer n'importe quelle chaîne de caractère
dans chacun des champs. La raison est que le frontend n'a pas été connecté à un
backend.
			
- Champ `name` : n'importe quoi
- Champ `email` : n'importe quoi
- Champ `password` : n'importe quoi
:::
