import sys
from PyQt5 import QtWidgets
from views.chatbot_view import MovieApp

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MovieApp()
    window.show()
    sys.exit(app.exec_())
