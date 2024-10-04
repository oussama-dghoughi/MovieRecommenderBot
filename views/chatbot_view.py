from PyQt5 import QtWidgets, uic
from controllers.chatbot_controller import ChatbotController
import os

class MovieApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'interface.ui')        
        uic.loadUi(ui_file_path, self)

        self.controller = ChatbotController()
        self.lineEdit.setPlaceholderText("Entrez un genre de film (ex: action, comédie)...")

        if hasattr(self, 'pushButton'):
            self.pushButton.clicked.connect(self.handle_send)

    def handle_send(self):
        user_input = self.lineEdit.text().strip()
        if self.is_genre(user_input):
            # Si l'utilisateur a saisi un genre de film
            recommendations = self.controller.get_movie_recommendations(user_input)
            self.display_movie_recommendations(recommendations)
        else:
            # Si l'utilisateur pose une question ou une phrase complexe
            response = self.controller.interact_with_mistral(user_input)
            self.display_chatbot_response(user_input, response)

        self.lineEdit.clear()

    def is_genre(self, user_input):
        genres = ["action", "comédie", "drame", "horreur", "thriller", "aventure", "animation", "fantastique"]
        return user_input.lower() in genres

    def display_chatbot_response(self, user_input, response):
        self.textBrowser.append(f"Utilisateur: {user_input}\nChatbot: {response}")

    def display_movie_recommendations(self, recommendations):
        if isinstance(recommendations, str):
            self.textBrowser.append(recommendations)  # Affiche le message d'erreur
        elif isinstance(recommendations, list) and recommendations:
            self.textBrowser.append("Voici des films que vous pourriez aimer :")
            for movie in recommendations:
                # Vérifier si les clés attendues sont présentes dans chaque film
                if 'Title' in movie and 'Year' in movie and 'imdbID' in movie:
                    # Construire l'URL IMDb du film
                    imdb_url = f"https://www.imdb.com/title/{movie['imdbID']}/"
                    # Créer un lien cliquable
                    link = f'<a href="{imdb_url}">{movie["Title"]} ({movie["Year"]})</a>'
                    # Afficher le titre, l'année et l'URL du film dans le QTextBrowser
                    self.textBrowser.append(link)
                else:
                    self.textBrowser.append("Erreur : Informations du film manquantes.")
        else:
            self.textBrowser.append("Aucune recommandation trouvée pour ce genre.")

    def display_chatbot_response(self, user_input, response):
        conversation = f"Utilisateur: {user_input}\nChatbot: {response}"
        self.textBrowser.append(conversation)
