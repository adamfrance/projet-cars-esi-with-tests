#!/bin/sh

# Attendre que MongoDB soit prêt
echo "Attente de MongoDB..."
sleep 10

# Exécuter le script d'import
python importScript.py

# Lancer l'application
python app.py