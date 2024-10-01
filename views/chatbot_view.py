# app/views/chatbot_view.py
class ChatbotView:
    @staticmethod
    def display_welcome_message():
        print("Bienvenue dans le Chatbot de recommandation de films !")

    @staticmethod
    def ask_user_preferences():
        return input("Quel genre de film souhaitez-vous regarder aujourd'hui ? ")

    @staticmethod
    def display_recommendations(recommendations):
        if recommendations:
            print("Voici des films que je vous recommande :")
            for movie in recommendations:
                print(f"- {movie['Title']} ({movie['Year']})")
        else:
            print("Désolé, je n'ai trouvé aucune recommandation.")
