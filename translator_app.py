from PyQt5.QtWidgets import QMainWindow
from translator_ui import TranslatorUI
from translator_logic import TranslatorLogic

class TranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Text Translator')
        self.setGeometry(100, 100, 800, 600)

        # Initialize logic and UI
        self.logic = TranslatorLogic()
        self.ui = TranslatorUI(self, self.logic)

        # Set up the UI
        self.setCentralWidget(self.ui)
