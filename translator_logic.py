from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS
import os
import pygame
import time
from knowledge_base import KnowledgeBase  # Import KnowledgeBase

class TranslatorLogic:
    def __init__(self):
        self.models = {
            'en-id': MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-id'),
            'en-es': MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-es'),
            'en-fr': MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-fr'),
            'en-de': MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-de'),
            'en-zh': MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-zh')
        }
        self.tokenizers = {
            'en-id': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-id'),
            'en-es': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-es'),
            'en-fr': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-fr'),
            'en-de': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-de'),
            'en-zh': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-zh')
        }
        self.current_language = 'en-id'  # Default language
        self.audio_file = ''  # Inisialisasi dengan string kosong
        self.pause_position = 0  # Position where the audio was paused

        self.knowledge_base = KnowledgeBase()  # Initialize knowledge base

        pygame.mixer.init()

    def set_current_language(self, index):
        language_map = {
            0: 'en-id',
            1: 'en-es',
            2: 'en-fr',
            3: 'en-de',
            4: 'en-zh'
        }
        self.current_language = language_map.get(index, 'en-id')
        print(f"Language set to: {self.current_language}")  # Debugging line

    def recommend_language(self, text):
        return self.knowledge_base.get_language_recommendation(text)

    def translate(self, text):
        try:
            tokenizer = self.tokenizers[self.current_language]
            model = self.models[self.current_language]
            inputs = tokenizer(text, return_tensors="pt", padding=True)
            translated = model.generate(**inputs, max_new_tokens=512)
            translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
            return translated_text
        except Exception as e:
            print(f"Error in translation: {e}")
            return "Translation error"

    def text_to_speech(self, text):
        try:
            lang_code = {
                'en-id': 'id',  # Indonesian
                'en-es': 'es',  # Spanish
                'en-fr': 'fr',  # French
                'en-de': 'de',  # German
                'en-zh': 'zh'   # Chinese
            }
            language = lang_code.get(self.current_language, 'en')
            print(f"Language code for TTS: {language}")  # Debugging line

            tts = gTTS(text, lang=language)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            self.audio_file = f'tts/translated_text_{timestamp}.mp3'
            tts.save(self.audio_file)
        except Exception as e:
            print(f"Error in text_to_speech: {e}")  # Debugging line

    def play_audio(self):
        try:
            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play(start=self.pause_position)
        except Exception as e:
            print(f"Error in play_audio: {e}")

    def pause_audio(self):
        try:
            self.pause_position = pygame.mixer.music.get_pos() / 1000.0
            pygame.mixer.music.pause()
        except Exception as e:
            print(f"Error in pause_audio: {e}")

    def stop_audio(self):
        try:
            pygame.mixer.music.stop()
            self.pause_position = 0
        except Exception as e:
            print(f"Error in stop_audio: {e}")
