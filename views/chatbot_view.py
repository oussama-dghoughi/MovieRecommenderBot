from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
import json

class MovieView(QMainWindow):
    def __init__(self):
        super(MovieView, self).__init__()
        uic.loadUi("./resources/interface.ui", self)  
        self.lineEdit.setPlaceholderText("Entrez un genre de film aimeriez-vous voir ?")
        self.show()




    def display_movie_recommendations(self, recommendations):
        """Affiche les recommandations de films."""
        if isinstance(recommendations, str):
            self.plainTextEdit.appendPlainText(recommendations)
        else:
            self.plainTextEdit.appendPlainText("Voici des films que vous pourriez aimer :")
            for movie in recommendations:
                self.plainTextEdit.appendPlainText(f"- {movie['Title']} ({movie['Year']})")



    def display_movie_recommendations(self, recommendations):
        """Affiche la liste des films recommandés dans l'interface utilisateur."""
        self.plainTextEdit.appendPlainText("Voici les recommandations de films :")
        for movie in recommendations:
           
            if movie[0]:
                self.plainTextEdit.appendPlainText(f"- {movie[0]} ({movie[1]})")
            else:
                self.plainTextEdit.appendPlainText("Aucune recommandation disponible pour ce genre.")

                


    def display_chatbot_response(self, user_input, response):
        """Affiche la réponse du chatbot après une interaction utilisateur."""
        self.plainTextEdit.appendPlainText(f"Utilisateur : {user_input}")
        self.plainTextEdit.appendPlainText(f"Chatbot : {response}")
