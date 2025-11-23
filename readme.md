# 🧠 SENTIMENT_MICROSERVICE - API d'Analyse de Sentiment (Back-end)

Ce dossier contient le service d'API REST responsable de l'authentification et de l'exécution de l'analyse de sentiment.

## 🐍 Technologies Utilisées

- **Framework API :** FastAPI
- **Authentification :** JWT Bearer Token
- **Librairies clés (assumées) :** python-multipart, uvicorn, passlibnaturel (NLP).

## ⚙️ Points Clés de l'API

L'API devrait exposer au moins les endpoints suivants :

| Méthode | Endpoint                | Description                                        | Protection      |
|---------|------------------------|----------------------------------------------------|------------------|
| POST    | /token                 | Authentification de l'utilisateur et génération du token JWT. | Aucune           |
| POST    | /predict    | Endpoint pour soumettre du texte et recevoir l'analyse de sentiment. | JWT Requis       |
| GET     | /login              | Récupération des informations de l'utilisateur courant. | JWT Requis       |

## 🚀 Démarrage Rapide

### Prérequis

Assurez-vous d'avoir Python et pip installés.

### Installation

Accédez au dossier du back-end :

```bash
cd backend/
```
Installez les dépendances (en supposant un fichier requirements.txt) :
````
pip install -r requirements.txt
````
### Lancement
Lancez l'API en utilisant Uvicorn :

````
uvicorn main:app --reload 
````

L'API sera disponible à l'adresse [http://localhost:8000].

Documentation
FastAPI génère automatiquement la documentation interactive (Swagger UI) à l'adresse :

http://localhost:8000/docs