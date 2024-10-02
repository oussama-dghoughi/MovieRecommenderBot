# models/movie_model.py

import os
import requests
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

class MovieModel:
    OMDB_API_URL = "http://www.omdbapi.com/"
    OMDB_API_KEY = os.getenv("OMDB_API_KEY")  # Récupérer la clé API OMDB depuis les variables d'environnement

    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")  # Clé API pour Mistral

    @staticmethod
    def get_movie_recommendation(genre):
        """Récupère les recommandations de films en fonction du genre via OMDB API."""
        params = {
            'apikey': MovieModel.OMDB_API_KEY,
            's': genre,  # Recherche par genre ou titre
            'type': 'movie'
        }
        response = requests.get(MovieModel.OMDB_API_URL, params=params)

        if response.status_code == 200:
            result = response.json()
            if result.get('Response') == 'True':
                return result.get('Search', [])  # Retourne les résultats des films trouvés
            else:
                return []
        else:
            return []

    @staticmethod
    def use_mistral_for_chat(messages):
        """Utilise Mistral AI pour gérer les conversations."""
        from mistralai import Mistral  # Import local pour l'utiliser uniquement si nécessaire

        # Initialisation du client Mistral avec la clé API
        client = Mistral(api_key=MovieModel.MISTRAL_API_KEY)

        # Appel à l'API Mistral pour obtenir une réponse
        chat_response = client.chat.complete(
            model="pixtral-12b-2409",
            messages=messages,
            response_format={"type": "json_object"}
        )

        # Retourne la réponse du chatbot
        return chat_response.choices[0].message.content
