from models.movie_model import MovieModel

class ChatbotController:
    def __init__(self, view):
        self.movie_model = MovieModel()
        self.view = view

       
        self.view.pushButton.clicked.connect(self.handle_send)



    def handle_send(self):
        user_input = self.view.lineEdit.text().strip()
        

        if user_input:
            if self.is_genre(user_input):
                recommendations = self.get_movie_recommendations(user_input)
                self.view.display_movie_recommendations(recommendations)
            else:
                response = self.interact_with_mistral(user_input)
                self.view.display_chatbot_response(user_input, response)

            self.view.lineEdit.clear()



    def get_movie_recommendations(self, genre):
        recommendations = self.movie_model.get_movie_recommendation(genre)
        if recommendations:
            return recommendations
        else:
            return "Désolé, aucune recommandation n'a été trouvée."
        



    def interact_with_mistral(self, user_input):
        messages = [{"role": "user", "content": user_input}]
        response = self.movie_model.use_mistral_for_chat(messages)
        return response
    


    def is_genre(self, user_input):
        """Vérifie si l'entrée utilisateur est un genre de film connu."""
        genres = ["action", "comédie", "drame", "horreur", "thriller", "aventure", "animation", "fantastique"]
        return user_input.lower() in genres
