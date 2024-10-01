# main.py
from controllers.chatbot_controller import ChatbotController
from views.chatbot_view import ChatbotView

def main():
    # Affiche le message de bienvenue
    ChatbotView.display_welcome_message()

    # Demande les préférences utilisateur
    user_input = ChatbotView.ask_user_preferences()

    # Obtient les recommandations du contrôleur
    recommendations = ChatbotController.recommend_movie(user_input)

    # Affiche les recommandations
    ChatbotView.display_recommendations(recommendations)

if __name__ == "__main__":
    main()
