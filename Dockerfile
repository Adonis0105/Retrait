# Utilise l'image officielle de Python
FROM python:3.12

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8000 pour Django
EXPOSE 8000

# Lancer l'application Django avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "qr_transaction_facilitator.wsgi:application"]
