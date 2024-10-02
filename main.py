import sys
from PyQt5 import QtWidgets, uic
import os
from controllers.chatbot_controller import ChatbotController

class MovieApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Charger l'interface utilisateur depuis le fichier .ui
        ui_file_path = os.path.join(os.path.dirname(__file__), 'resources', 'interface.ui')
        print("Chargement de l'interface utilisateur...")
        uic.loadUi(ui_file_path, self)  # Charge le fichier .ui
        print("Interface utilisateur chargée.")

        self.controller = ChatbotController()
        self.lineEdit.setPlaceholderText("Entrez un genre de film (ex: action, comédie)...")

        # Utilisez le nom correct du bouton, ici pushButton
        if hasattr(self, 'pushButton'):
            self.pushButton.clicked.connect(self.handle_send)
        else:
            print("Erreur : le bouton 'pushButton' n'a pas été trouvé.")

    def handle_send(self):
        # Récupérer le texte saisi par l'utilisateur
        user_input = self.lineEdit.text().strip()

        if user_input:
            if self.is_genre(user_input):
                # Si l'utilisateur a saisi un genre de film
                recommendations = self.controller.get_movie_recommendations(user_input)
                self.display_movie_recommendations(recommendations)
            else:
                # Si l'utilisateur pose une question ou une phrase complexe
                response = self.controller.interact_with_mistral(user_input)
                self.display_chatbot_response(user_input, response)

            # Effacer le champ de saisie après avoir cliqué sur "Envoyer"
            self.lineEdit.clear()

    def is_genre(self, user_input):
        """Vérifie si l'entrée utilisateur est un genre de film connu."""
        genres = ["action", "comédie", "drame", "horreur", "thriller", "aventure", "animation", "fantastique"]
        return user_input.lower() in genres

    def display_movie_recommendations(self, recommendations):
        if isinstance(recommendations, str):
            self.plainTextEdit.appendPlainText(recommendations)  # Utilisez appendPlainText
        else:
            self.plainTextEdit.appendPlainText("Voici des films que vous pourriez aimer :")
            for movie in recommendations:
                self.plainTextEdit.appendPlainText(f"- {movie['Title']} ({movie['Year']})")
    
    def chat_with_mistral(self):
        # Demander à l'utilisateur d'interagir avec le chatbot
        user_input = QtWidgets.QInputDialog.getText(self, "Chatbot", "Posez une question au chatbot :")[0]

        if user_input:
            # Utiliser Mistral pour répondre à la question
            response = self.controller.interact_with_mistral(user_input)

            # Afficher la réponse du chatbot
            self.plainTextEdit.append(f"Utilisateur: {user_input}\nChatbot: {response}")
    
    def display_chatbot_response(self, user_input, response):
        conversation = f"Utilisateur: {user_input}\nChatbot: {response}"
        self.plainTextEdit.appendPlainText(conversation)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MovieApp()
    window.show()
    sys.exit(app.exec_())
