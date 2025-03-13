import csv
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from models import CarBase
from decouple import config
import time

# Attendre que MongoDB soit prêt
time.sleep(2)

# Récupérer les variables d'environnement
DB_URL = config('DB_URL')
DB_NAME = config('DB_NAME')

# Configuration MongoDB
client = MongoClient(DB_URL)
db = client[DB_NAME]  # Utilise la base de données "dashboard"
cars = db["cars"]     # Utilise la collection "cars"

print(f"Connexion à MongoDB réussie! Base de données: {DB_NAME}")

# Lecture du fichier CSV
file_path = "./filteredCars.csv"
with open(file_path, encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)
    name_records = list(csv_reader)

inserted_count = 0
error_count = 0

for rec in name_records:
    try:
        # Conversion des champs
        rec["cm3"] = int(rec["cm3"])
        rec["price"] = int(rec["price"])
        rec["year"] = int(rec["year"])
        rec["km"] = int(rec["km"])
        rec["brand"] = str(rec["brand"])
        rec["make"] = str(rec["make"])
        
        # Création du document
        car = jsonable_encoder(CarBase(**rec))
        print("Inserting:", car)
        
        # Insertion dans MongoDB
        result = cars.insert_one(car)
        inserted_count += 1
        print(f"Document inséré avec succès: {car['brand']} {car['make']}")
        
    except Exception as e:
        print(f"Erreur lors de l'insertion: {e}")
        error_count += 1

print(f"Import terminé! {inserted_count} documents insérés, {error_count} erreurs")