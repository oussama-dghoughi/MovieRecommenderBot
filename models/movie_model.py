import os
import base64
import requests
from dotenv import load_dotenv
from mistralai import Mistral 


class MovieModel:
    OMDB_API_URL = "http://www.omdbapi.com/"
    OMDB_API_KEY = os.getenv("OMDB_API_KEY")  # Récupérer la clé API OMDB depuis les variables d'environnement
    # Chargement des variables d'environnement
    load_dotenv()

    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")  # Clé API pour Mistral

    @staticmethod
    def send_request_to_omdb(params):
        """Envoie une requête à l'API OMDB avec les paramètres fournis."""
        response = requests.get(MovieModel.OMDB_API_URL, params=params)

        # Affichez le code de statut et le contenu de la réponse pour le débogage
        print(f"Code de statut de l'API : {response.status_code}")
        print(f"Contenu de la réponse : {response.text}")

        return response.json()

    @staticmethod
    def get_movie_recommendation(genre):
        """Récupère les recommandations de films en fonction du genre."""
        params = {
            'apikey': MovieModel.OMDB_API_KEY,
            's': genre,  # Recherche par genre (ou titre) de film
            'type': 'movie'
        }
        result = MovieModel.send_request_to_omdb(params)

        # Vérifiez si la réponse contient des résultats
        if result.get('Response') == 'True':
            return result.get('Search', [])  # Retourne les résultats de recherche de films
        else:
            print("Erreur:", result.get('Error', 'Aucune erreur spécifiée.'))
            return []

