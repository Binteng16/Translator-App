from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout, QLabel, QComboBox
from PyQt5.QtGui import QFont

class TranslatorUI(QWidget):
    def __init__(self, parent, logic):
        super().__init__(parent)
        self.logic = logic
        self.initUI()

    def initUI(self):
        # Set font
        font = QFont('Arial', 12)

        # Create widgets
        self.text_edit = QTextEdit(self)
        self.text_edit.setFont(font)
        self.text_edit.setPlaceholderText('Enter text to translate...')
        self.text_edit.setStyleSheet('background-color: #ffffff; border: 1px solid #cccccc; padding: 10px;')

        self.translate_button = QPushButton('Translate', self)
        self.translate_button.setFont(font)
        self.translate_button.setStyleSheet('background-color: #0078d4; color: #ffffff; padding: 10px; border: none; border-radius: 5px;')

        self.result_label = QLabel('Translated Text:', self)
        self.result_label.setFont(font)

        self.result_edit = QTextEdit(self)
        self.result_edit.setFont(font)
        self.result_edit.setReadOnly(True)
        self.result_edit.setStyleSheet('background-color: #f5f5f5; border: 1px solid #cccccc; padding: 10px;')

        # Create audio control buttons
        self.play_pause_button = QPushButton('Play/Pause', self)
        self.play_pause_button.setFont(font)
        self.play_pause_button.setStyleSheet('background-color: #0078d4; color: #ffffff; padding: 10px; border: none; border-radius: 5px;')

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.setFont(font)
        self.stop_button.setStyleSheet('background-color: #dc3545; color: #ffffff; padding: 10px; border: none; border-radius: 5px;')

        # Language selection
        self.language_selector = QComboBox(self)
        self.language_selector.addItems([
            'Indonesian (en-id)',
            'Spanish (en-es)',
            'French (en-fr)',
            'German (en-de)',
            'Chinese (en-zh)'
        ])
        self.language_selector.setFont(font)
        self.language_selector.setStyleSheet('padding: 10px;')

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Enter text to translate:', self))
        layout.addWidget(self.text_edit)
        layout.addWidget(self.language_selector)
        layout.addWidget(self.translate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_edit)
        layout.addWidget(self.play_pause_button)
        layout.addWidget(self.stop_button)
        layout.setContentsMargins(20, 20, 20, 20)  # Margin around the layout

        self.setLayout(layout)

        # Connect button click events
        self.translate_button.clicked.connect(self.translate_text)
        self.play_pause_button.clicked.connect(self.toggle_play_pause)
        self.stop_button.clicked.connect(self.stop_audio)
        self.language_selector.currentIndexChanged.connect(self.change_language)

        self.is_playing = False

    def change_language(self, index):
        self.logic.set_current_language(index)

    def translate_text(self):
        text = self.text_edit.toPlainText()
        recommended_language = self.logic.recommend_language(text)
        language_index = self.language_selector.findText(f'{recommended_language.capitalize()} ({recommended_language})')
        self.language_selector.setCurrentIndex(language_index)

        translated_text = self.logic.translate(text)
        self.result_edit.setText(translated_text)
        self.logic.text_to_speech(translated_text)

    def toggle_play_pause(self):
        if self.is_playing:
            self.logic.pause_audio()
            self.play_pause_button.setText('Play')
        else:
            self.logic.play_audio()
            self.play_pause_button.setText('Pause')
        self.is_playing = not self.is_playing

    def stop_audio(self):
        self.logic.stop_audio()
        self.play_pause_button.setText('Play')
        self.is_playing = False
