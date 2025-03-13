# Utiliser une image Node officielle
FROM node:16-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de configuration # package.json yarn.lock ./
COPY . .

# Installer les dépendances
RUN yarn install --frozen-lockfile

# Copier le reste du code de l'application
COPY . .

# Construire l'application pour la production
RUN yarn build

# Spécifier le port
EXPOSE 3005

# Lancement (ou alors un serveur statique selon votre config)
CMD ["yarn", "start"]
