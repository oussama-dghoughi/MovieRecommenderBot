from PyQt5 import QtWidgets  # Importer QtWidgets pour QApplication
from controllers.chatbot_controller import ChatbotController
from views.chatbot_view import MovieView

def main():
    # Créer une instance de QApplication
    app = QtWidgets.QApplication([])  # Notez que nous passons une liste vide ici

    # Initialisation du contrôleur et de la vue
    controller = ChatbotController()
    view = MovieView(controller)  # Passez le contrôleur à la vue

    # Affichage du message de bienvenue
    view.display_welcome_message()

    # Afficher la fenêtre
    view.show()

    # Exécuter l'application
    app.exec_()  # Commencer la boucle d'événements

if __name__ == "__main__":
    main()
