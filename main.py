import sys
from PyQt5.QtWidgets import QApplication  # Ajoutez cette ligne pour importer QApplication
from controllers.chatbot_controller import ChatbotController
from views.chatbot_view import MovieView

# Initialisation de l'application
# Créer la vue
# Créer le contrôleur et connecter la vue au contrôleur
# Lancer l'application


app = QApplication(sys.argv) 
view = MovieView()
controller = ChatbotController(view)
view.show()  
sys.exit(app.exec_())  
