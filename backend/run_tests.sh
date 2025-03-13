#!/bin/bash

# Activer l'environnement virtuel
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Installer les dépendances spécifiques aux tests si elles ne sont pas dans requirements.txt
pip install pytest pytest-asyncio pytest-mock httpx pytest-cov

# Exécuter les tests avec couverture
pytest -v --cov=. --cov-report=term --cov-report=html:cov_html