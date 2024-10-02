# views/movie_view.py

class MovieView:
    @staticmethod
    def display_welcome_message():
        print("Bienvenue dans le Chatbot de recommandation de films !")

    @staticmethod
    def ask_for_genre():
        return input("Quel genre de film souhaitez-vous regarder aujourd'hui ? ")

    @staticmethod
    def display_movie_recommendations(recommendations):
        if isinstance(recommendations, str):  
            print(recommendations)
        else:
            print("Voici des films que vous pourriez aimer :")
            for movie in recommendations:
                print(f"- {movie['Title']} ({movie['Year']})")

    @staticmethod
    def ask_for_mistral_input():
        return input("Que voulez-vous demander au chatbot Mistral ?")

    @staticmethod
    def display_mistral_response(response):
        print(f"Réponse du chatbot : {response}")
