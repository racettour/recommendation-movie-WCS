# :clapper: recommendation-movie-WCS
projet 2 de la WCS : 
 - nettoyage de la base de données IMdb
 - création de KPis pour analyser la production cinématographique
 - création d’un moteur de recommandation de film 

#   :handshake: L'Equipe du projet
- [Raphaël Cettour](https://github.com/racettour)
- [Anthony Etienne](https://github.com/Anthowheels)
- [François Albert](https://github.com/francoisalb)
- [Florian Allory](https://github.com/FlorianAllory)


[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)  [![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  
[![forthebadge](https://github.com/racettour/One-Piece-Web-scraping/blob/main/readme_Image/clean-up-in-process-95%25.svg)](http://forthebadge.com)

# :ledger: Index
 - [L'Equipe du projet](#handshake-L'Equipe-du-projet)
 - [Les différentes étapes du projet](#beginner-Les-différentes-étapes-du-projet)
 - [schéma de principe](#twisted_rightwards_arrows-schéma-de-principe)
 - [Développements futurs](#wrench-Développements-futurs)
 - [Galerie](#camera-Galerie)
 
 
 

# :beginner: Les différentes étapes du projet
1. Analyse des besoins et des attentes du client

2. Chargement des différentes bases de données

- name.basics.tsv.gz
- title.akas.tsv.gz
- title.basics.tsv.gz
- title.crew.tsv.gz
- title.principals.tsv.gz
- title.ratings.tsv.gz

3. Analyse et nettoyage des données pertinentes en vue de leur exploitation


4. Création de KPIs sur streamlit


5. Création du moteur de recommandation de film 
- **Choix de l'IA** : K-Nearest Neighbours de Scikit Learn
- Création d'une interface graphique sur streamlit
- **Web scraping :** récupération de l’affiche et du résumé des films sur le site IMdb


# :twisted_rightwards_arrows: schéma de principe
![picture1](image_readme/SchemaPrincipe.png)


# :wrench: Développements futurs
  - Intégrer les séries dans la base de données
  - Etudier une/des solution(s) pour compléter les infos manquantes (NaN) et enrichir la base de données
  - Test utilisateur
  - Gestion d’erreur
  - Remplacer l’identifiant du réalisateur par son nom



#  :camera: Galerie
## 1. KPI exemples

### Graphique linéaire nous décrivant l'évolution du nombre de films produit par année
![picture2](image_readme/KPI1.png)

### Boîte à moustache représentant les notes de films en fonction de trois genres (Action, Documentaire, Western)
![picture3](image_readme/KPI2.png)

### Matrice de corrélation
![picture4](image_readme/KPI3.png)


## 2. Moteur de recommandation

Choix d'un film pour le moteur de recommendation
![picture5](image_readme/IA_1.png)

Exemple de recommandations suite à la sélection "Harry Potter"
![picture6](image_readme/IA_2.png)



#  :lock: License
Add a license here, or a link to it.
