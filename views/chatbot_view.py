from PyQt5 import QtWidgets, uic
import os

class MovieView(QtWidgets.QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller  # Stocker le contrôleur pour l'utiliser plus tard
        # Charger l'interface utilisateur depuis le fichier .ui
        ui_file_path = os.path.join(os.path.dirname(__file__), '../resources/interface.ui')
        uic.loadUi(ui_file_path, self)

        # Connecter le bouton "envoyer"
        self.send_button = self.findChild(QtWidgets.QPushButton, 'ENVOYER')  # Assurez-vous que ce nom est correct
        self.user_input = self.findChild(QtWidgets.QLineEdit, 'lineEdit')  # Nom de la zone de saisie
        self.text_area = self.findChild(QtWidgets.QTextEdit, 'texteEdit')  # Nom de la zone d'affichage

        # Vérifiez si les widgets sont correctement chargés
        if self.send_button is None:
            print("Erreur : le bouton 'ENVOYER' n'a pas été trouvé dans le fichier .ui.")
        else:
            self.send_button.clicked.connect(self.handle_send)  # Connecter le clic du bouton à la méthode

        if self.text_area is None:
            print("Erreur : la zone de texte n'a pas été trouvée dans le fichier .ui.")
        else:
            self.display_welcome_message()

    def handle_send(self):
        """Gérer l'envoi du message de l'utilisateur."""
        user_input = self.user_input.text()
        self.text_area.append(f"Vous : {user_input}")  
        self.user_input.clear()  # Effacer l'entrée après l'envoi

        # Appeler le contrôleur pour obtenir une réponse de Mistral
        mistral_response = self.controller.get_mistral_response(user_input)
        self.display_mistral_response(mistral_response)

        # Appeler le contrôleur pour obtenir des recommandations de films
        movie_recommendations = self.controller.get_movie_recommendations(user_input)
        self.display_movie_recommendations(movie_recommendations)

    def display_welcome_message(self):
        if self.text_area is not None:
            self.text_area.append("Bienvenue dans le Chatbot de recommandation de films !")

    def display_movie_recommendations(self, recommendations):
        if isinstance(recommendations, str):  # En cas de message d'erreur
            if self.text_area is not None:
                self.text_area.append(recommendations)
        else:
            if self.text_area is not None:
                self.text_area.append("Voici des films que vous pourriez aimer :")
                for movie in recommendations:
                    self.text_area.append(f"- {movie['Title']} ({movie['Year']})")

    def display_mistral_response(self, response):
        if self.text_area is not None:
            self.text_area.append(f"Réponse du chatbot : {response}")
