db = db.getSiblingDB('cars_db');

// Créer un utilisateur avec les droits nécessaires
db.createUser({
  user: 'root',
  pwd: 'root',
  roles: [
    {
      role: 'readWrite',
      db: 'cars_db'
    }
  ]
});