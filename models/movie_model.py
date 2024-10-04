# models/movie_model.py

import os
import requests
from dotenv import load_dotenv
from mistralai import Mistral  




class MovieModel:
    load_dotenv()
    OMDB_API_URL = "http://www.omdbapi.com/"
    OMDB_API_KEY = os.getenv("OMDB_API_KEY")  

    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY") 

    
    @staticmethod
    def get_movie_recommendation(genre):
        """Récupère les recommandations de films en fonction du genre via OMDB API."""
        params = {
            'apikey': MovieModel.OMDB_API_KEY,
            's': genre,  
            'type': 'movie'
        }
        response = requests.get(MovieModel.OMDB_API_URL, params=params)

        if response.status_code == 200:
            result = response.json()
            if result.get('Response') == 'True':
                movies = [(movie['Title'], movie['Year'], movie['Poster']) for movie in result.get('Search', [])]
               
                if movies:
                    return movies
                else:
                    return [("Désolé, aucun film trouvé pour ce genre.", "", "")]
            else:
                print(f"Error: {result.get('Error')}")
                return [("Désolé, aucun film trouvé pour ce genre.", "", "")]
        else:
            print(f"HTTP Error: {response.status_code}")
            return [("Erreur de connexion avec le service OMDB.", "", "")]



    @staticmethod
    def use_mistral_for_chat(messages):
        """Utilise Mistral AI pour gérer les conversations."""
       

        client = Mistral(api_key=MovieModel.MISTRAL_API_KEY)

        chat_response = client.chat.complete(
            model="pixtral-12b-2409",
            messages=messages,
            response_format={"type": "json_object"}
        )

        return chat_response.choices[0].message.content
