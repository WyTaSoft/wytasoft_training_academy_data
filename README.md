# Formation Apache Spark Avancée - WyTaSoft

Bienvenue dans la formation Apache Spark Avancée proposée par WyTaSoft. Cette formation est destinée aux ingénieurs de données et aux data scientists souhaitant approfondir leurs connaissances de Spark à travers des cas d'utilisation concrets.

## Use Case 1: Prise en main de Docker avec Spark

Dans ce premier use case, nous allons apprendre à utiliser Docker pour exécuter des jobs Apache Spark. Le but est de démontrer comment containeriser un environnement Spark et lancer des traitements sur des données CSV.

### Objectifs :
- Découvrir l'environnement Docker et Spark.
- Configurer un container Spark avec Docker.
- Exécuter des transformations et actions Spark sur des fichiers CSV.

### Données :
- **orders.csv** : Contient les informations sur les commandes.
- **clients.csv** : Contient les informations sur les clients.

### Étapes :
1. Configuration de l'environnement Docker pour Spark.
2. Utilisation de Spark pour charger les données clients et commandes.
3. Réalisation d'actions simples (jointures, filtrage) sur les datasets.

### Technologies utilisées :
- Docker
- Apache Spark
- Fichiers CSV

---

## Use Case 2: Cluster Spark avec Docker Compose

Ce deuxième use case se concentre sur la configuration d'un cluster Apache Spark à l'aide de Docker Compose. L'objectif est de simuler un environnement de cluster distribué pour exécuter des tâches Spark à travers plusieurs nœuds, via une orchestration de containers.

### Objectifs :
- Configurer un cluster Spark avec Docker Compose.
- Lancer un nœud maître (Spark Master) et des nœuds travailleurs (Spark Worker).
- Exécuter une application PySpark dans ce cluster distribué.

### Fichier `docker-compose.yml` :
- **Spark Master** : Service responsable de la coordination des tâches.
- **Spark Worker** : Services qui exécutent les calculs distribués.
- **Application PySpark** : Service qui envoie les tâches de traitement de données au Spark Master.

### Étapes :
1. Créer un fichier `docker-compose.yml` pour orchestrer les services Spark Master, Spark Workers, et l’application PySpark.
2. Lancer le cluster Spark à l’aide de Docker Compose.
3. Envoyer et exécuter des jobs PySpark dans le cluster Spark.

### Technologies utilisées :
- Docker Compose
- Apache Spark
- PySpark

---

## Use Case 3: La notion de Closure avec Apache Spark

Dans ce troisième use case, nous explorons la notion de **Closure** dans Apache Spark. Ce concept est crucial lorsque vous utilisez des fonctions anonymes ou des variables externes dans vos jobs Spark distribués.

### Objectifs :
- Comprendre la notion de Closure dans Spark.
- Identifier comment les variables externes sont capturées dans les transformations distribuées.
- Éviter les pièges courants liés aux Closures dans Spark.

### Étapes :
1. Explication théorique de la **Closure** dans Apache Spark.
2. Création d'un exemple PySpark qui met en évidence l'importance des Closures.
3. Analyse des erreurs fréquentes liées aux Closures dans les transformations RDD et DataFrame.

### Technologies utilisées :
- Apache Spark
- PySpark

---

## Use Case 4: Opérations RDD avec Apache Spark

Ce quatrième use case se concentre sur les **opérations RDD** dans Apache Spark, en utilisant des données réelles sur les comptes et les transactions financières. Le but est de manipuler et transformer les données à l'aide des RDD pour effectuer des analyses simples et complexes.

### Objectifs :
- Comprendre et manipuler les RDD dans Spark.
- Appliquer des transformations et actions RDD (map, filter, reduce, etc.).
- Effectuer des analyses sur des datasets de comptes et transactions.

### Données :
- **comptes.csv** : Contient des informations sur les comptes bancaires.
- **transactions.csv** : Contient des informations sur les transactions effectuées sur les comptes.

### Étapes :
1. Charger les fichiers CSV en tant que RDD.
2. Appliquer des transformations comme `map`, `filter` et `join` pour analyser les transactions par compte.
3. Calculer des statistiques agrégées (par exemple, le total des transactions par compte).

### Technologies utilisées :
- Apache Spark
- RDD
- Fichiers CSV

---

## Use Case 5: Opérations DataFrame avec Apache Spark

Ce cinquième use case se concentre sur les **opérations DataFrame** dans Apache Spark, en explorant l'utilisation des DataFrames pour manipuler et analyser les données de manière efficace.

### Objectifs :
- Manipuler des DataFrames dans Spark.
- Effectuer des transformations comme `select`, `filter`, `groupBy`, et `agg` pour analyser des données.
- Comparer les performances entre les RDD et les DataFrames.

### Étapes :
1. Charger un fichier CSV en tant que DataFrame.
2. Appliquer des transformations complexes (agrégations, jointures, filtres).
3. Comparer les performances des opérations avec celles des RDD.

### Technologies utilisées :
- Apache Spark
- DataFrames
- PySpark

---

## Use Case 6: ETL Scala Spark

Dans ce sixième use case, nous utilisons **Scala avec Apache Spark** pour lire, transformer, joindre et écrire des données issues d'un fichier CSV, tout en optimisant les performances.

### Objectifs :
- Lire des données CSV avec Scala Spark.
- Appliquer des transformations et des jointures sur les DataFrames.
- Écrire les résultats dans un format de sortie performant (Parquet, etc.).
- Explorer les options de performance (partitionnement, cache, etc.).

### Données :
- **transactions.csv** : Contient des informations sur les transactions financières.

### Étapes :
1. Lecture du fichier `transactions.csv` en tant que DataFrame avec Spark Scala.
2. Application de transformations sur les transactions (filtres, agrégations).
3. Jointure avec d'autres DataFrames pour enrichir les données.
4. Écriture des résultats dans un fichier Parquet optimisé.
5. Analyse et application d'options de performance (repartition, cache, etc.).

### Technologies utilisées :
- Apache Spark
- Scala
- Fichiers CSV
- Parquet

---

## Use Case 7: Recommender System avec Apache Spark

Dans ce septième use case, nous développons un **moteur de recommandations** pour une banque, basé sur les transactions et profils clients, afin de proposer des produits financiers personnalisés.

### Contexte :
Une banque souhaite améliorer la satisfaction et la fidélisation de ses clients en leur proposant des produits financiers personnalisés (prêts, cartes de crédit, épargne, etc.). Elle dispose de données sur les transactions bancaires, les interactions avec les services bancaires en ligne, et les profils des clients.

### Objectifs :
- Utiliser Apache Spark pour développer un moteur de recommandations qui suggère des produits financiers adaptés aux clients en fonction de leur historique d'utilisation, comportements transactionnels et profils similaires.
- Appliquer des méthodes de filtrage collaboratif (Collaborative Filtering) ou de filtrage basé sur le contenu.

### Données :
- **Transactions bancaires** : Montants, types de transaction (dépôt, retrait, achat), dates.
- **Profils clients** : Âge, revenu, type de compte, historique de crédit, préférences de services bancaires.
- **Historique des interactions avec la banque** : Utilisation des applications bancaires, visites en agence, contacts avec le service client.

### Tâches :
1. Créer un modèle de recommandation basé sur le filtrage collaboratif ou basé sur le contenu.
2. Prévoir les produits financiers que les clients pourraient être intéressés à utiliser.
3. Exemples d'applications :
    - Recommander des cartes de crédit en fonction des habitudes d'achat.
    - Proposer des offres de prêt aux clients similaires à ceux ayant souscrit des prêts.
    - Suggérer des produits d'investissement ou d'épargne adaptés au profil financier d'un client.

### Technologies utilisées :
- Apache Spark
- Filtrage collaboratif
- Filtrage basé sur le contenu

---

## Use Case 8: Forecast Sales avec Apache Spark

Dans ce huitième use case, nous développons un modèle de **prévision des ventes** pour une entreprise de retail en ligne, afin d'optimiser la gestion des stocks et des campagnes marketing.

### Contexte :
Une entreprise de retail en ligne souhaite améliorer ses prévisions de vente pour optimiser ses stocks et mieux gérer ses campagnes marketing. L'objectif est de prédire les ventes mensuelles pour les différents produits sur plusieurs mois, en se basant sur des données historiques.

### Objectifs :
- Utiliser Apache Spark pour prédire les ventes mensuelles des produits en fonction de données historiques, saisonnières et externes.
- Utiliser des méthodes de machine learning ou de séries temporelles pour générer les prévisions.

### Données :
- **Historique des ventes** : Données sur les ventes quotidiennes ou hebdomadaires sur 2 ans, incluant les caractéristiques des produits (catégorie, prix, promotions, etc.).
- **Données externes** : Informations sur les tendances économiques (inflation, taux d'intérêt), la saisonnalité (fêtes, événements spéciaux), et des données météorologiques.
- **Données internes** : Informations sur les stocks, les retours de produits, et les avis clients.

### Tâches :
1. Ingestion et exploration des données : Charger les données historiques dans Spark, les nettoyer et explorer les tendances de vente passées.
2. Préparation des données : Créer des variables additionnelles basées sur la saisonnalité, les promotions ou les événements spéciaux (Black Friday, Noël, etc.).
3. Modélisation prédictive : Utiliser un modèle de machine learning (régression linéaire, forêt aléatoire, XGBoost) ou une approche de séries temporelles pour prédire les ventes mensuelles des produits.
4. Évaluation du modèle : Comparer les performances des différents modèles à l'aide de métriques comme la MAE (erreur absolue moyenne) ou la RMSE (erreur quadratique moyenne).
5. Industrialisation : Déployer un pipeline de prévision des ventes à l'aide de Spark MLlib pour automatiser les prévisions de vente chaque mois.

### Technologies utilisées :
- Apache Spark
- Machine Learning (régression linéaire, forêt aléatoire, séries temporelles)
- Spark MLlib

---

## Use Case 9: Sentiment Analysis avec Apache Spark Streaming

Dans ce neuvième use case, nous mettons en place une solution d'**analyse de sentiment en temps réel** pour des flux de commentaires clients, en utilisant Spark Streaming et un modèle pré-entraîné DistilBERT.

### Contexte :
L'analyse de sentiment est cruciale pour les entreprises qui souhaitent comprendre ce que leurs clients pensent de leurs produits ou services. Avec l'explosion des réseaux sociaux et des plateformes de commentaires en ligne, les entreprises doivent analyser ces données en temps réel.

### Objectifs :
- Utiliser Spark Streaming pour ingérer des flux de commentaires en temps réel.
- Appliquer un modèle de machine learning pré-entraîné (DistilBERT) pour détecter le sentiment (positif ou négatif).
- Afficher en temps réel les résultats dans la console (commentaire + sentiment).

### Étapes :
1. Mise en place de Spark Streaming pour lire des flux de données provenant de Kafka.
2. Simulation des commentaires clients en temps réel à l'aide d'un producteur Kafka.
3. Utilisation du modèle pré-entraîné DistilBERT pour analyser les sentiments des commentaires.
4. Affichage en temps réel des résultats dans la console avec le sentiment associé.

### Technologies utilisées :
- Apache Spark Streaming
- Kafka
- Modèle DistilBERT
- PySpark

---

## Liste des autres Use Cases :
1. **Prise en main de Docker avec Spark** - [Details](#use-case-1)
2. **Cluster Spark avec Docker Compose** - [Details](#use-case-2)
3. **La notion de Closure avec Apache Spark** - [Details](#use-case-3)
4. **Opérations RDD avec Apache Spark** - [Details](#use-case-4)
5. **Opérations DataFrame avec Apache Spark** - [Details](#use-case-5)
6. **ETL Scala Spark** - [Details](#use-case-6)
7. **Recommender System avec Apache Spark** - [Details](#use-case-7)
8. **Forecast Sales avec Apache Spark** - [Details](#use-case-8)
9. **Sentiment Analysis avec Apache Spark Streaming** - [Details](#use-case-9)
