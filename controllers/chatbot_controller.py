# app/controllers/chatbot_controller.py
from models.movie_model import MovieModel


class ChatbotController:
    @staticmethod
    def recommend_movie(user_input):
        # Extrait les préférences de l'utilisateur (par exemple, un genre ou une humeur)
        genre, mood = ChatbotController.parse_user_input(user_input)
        # Appelle le modèle pour obtenir des recommandations
        recommendations = MovieModel.get_movie_recommendation(genre, mood)
        return recommendations

    @staticmethod
    def parse_user_input(user_input):
        # Analyse simple des préférences de l'utilisateur
        # Exemple : "Je veux un film d'action pour une soirée détendue"
        if "action" in user_input.lower():
            return "action", "detente"
        elif "comédie" in user_input.lower():
            return "comedy", "fun"
        # Ajoutez plus de genres et d'humeurs ici
        return "drama", "neutral"
