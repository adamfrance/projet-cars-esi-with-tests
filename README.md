# Projet FullStack Cars Analytics

Ce projet est une application fullstack permettant d'analyser des données de voitures. Il utilise une architecture FARM (FastAPI, React, MongoDB) et inclut des tests unitaires pour assurer la qualité du code.

## Structure du projet

```
project/
├── backend/           # API FastAPI 
│   ├── routers/       # Routes de l'API
│   ├── tests/         # Tests unitaires backend
│   └── utils/         # Utilitaires et fonctions auxiliaires
├── frontend/          # Application React
│   ├── src/           # Code source React
│   │   ├── components/# Composants React
│   │   └── unit-tests/# Tests unitaires frontend
│   └── public/        # Fichiers statiques
└── docker-compose.yml # Configuration Docker
```

## Backend (FastAPI)

### Fichiers de tests et leurs rôles

Le backend comprend plusieurs types de tests unitaires:

1. **tests/test_models.py** - Teste la validation des modèles de données
   - `test_car_base_valid_data`: Vérifie qu'un modèle de voiture valide est accepté
   - `test_car_base_invalid_year`: Vérifie que la validation rejette les années incorrectes

2. **tests/test_cars_router_mock.py** - Teste les routes API avec des mocks
   - `test_list_all_cars_mock`: Vérifie l'endpoint qui liste toutes les voitures
   - `test_list_cars_filtered_by_brand_mock`: Vérifie le filtrage des voitures par marque
   - `test_brand_count_mock`: Vérifie le comptage de voitures par marque

3. **tests/test_utils.py** - Teste les fonctions utilitaires
   - `test_report_pipeline_simple`: Vérifie la génération de rapports

### Comment lancer les tests backend

Pour lancer tous les tests du backend:

```bash
cd backend
pytest
```

Pour exécuter un fichier de tests spécifique:

```bash
pytest tests/test_models.py -v
```

Pour exécuter un test spécifique:

```bash
pytest tests/test_models.py::test_car_base_valid_data -v
```

Pour afficher la couverture de tests:

```bash
pytest --cov=. --cov-report=term
```

## Frontend (React)

### Tests unitaires frontend

Les tests frontend sont organisés dans le dossier `frontend/src/unit-tests/` et testent les différents composants React:

- `App.test.js` - Teste le composant principal App
- `Card.test.js` - Teste l'affichage des cartes de voitures
- `BrandCount.test.js` - Teste le compteur de marques
- `ModelCount.test.js` - Teste le compteur de modèles
- `CarsDropDown.test.js` - Teste le menu déroulant de sélection
- Etc.

### Comment lancer les tests frontend

```bash
cd frontend
npm test
```

Pour lancer un test spécifique:

```bash
npm test -- -t "Card Component"
```

## Lancer l'application complète

Pour démarrer l'application complète avec Docker:

```bash
docker compose up -d
```

Cela va:
1. Démarrer une base de données MongoDB
2. Importer les données de voitures
3. Lancer l'API backend sur http://localhost:5005
4. Lancer l'interface frontend sur http://localhost:3005

## Notes pour le développement

### Tests sans Docker

Les tests backend sont conçus pour fonctionner sans avoir besoin de lancer les conteneurs Docker. Ils utilisent:
- `mongomock` pour simuler MongoDB
- Des mocks pour isoler les composants
- Des versions modifiées des routes API pour les tests

Cela permet un développement plus rapide et des tests plus fiables qui ne dépendent pas de l'infrastructure.

### Fonctionnalités de l'application

- Exploration des données de voitures avec filtrage par marque
- Visualisation des statistiques par marques et modèles
- Génération de rapports par email
- Tableaux de bord avec graphiques interactifs