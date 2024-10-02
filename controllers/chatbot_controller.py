# controllers/chatbot_controller.py

from models.movie_model import MovieModel

class ChatbotController:
    def __init__(self):
        self.movie_model = MovieModel()

    def get_movie_recommendations(self, genre):
        """Récupère et affiche les recommandations de films pour un genre donné."""
        recommendations = self.movie_model.get_movie_recommendation(genre)
        if recommendations:
            return recommendations
        else:
            return "Désolé, aucune recommandation n'a été trouvée."

    def interact_with_mistral(self, user_input):
        """Gère l'interaction avec Mistral AI."""
        messages = [
            {
                "role": "user",
                "content": user_input
            }
        ]
        response = self.movie_model.use_mistral_for_chat(messages)

        # Vérifier si la réponse est valide et non "NaN"
        if response is None or response.strip().lower() == "nan":
            return "Désolé, je n'ai pas compris la réponse. Pouvez-vous reformuler ?"
        
        return response
