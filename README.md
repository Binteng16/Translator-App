# Text Translator

Text Translator adalah aplikasi berbasis desktop yang memungkinkan pengguna untuk menerjemahkan teks dari bahasa Inggris ke berbagai bahasa lain serta mengubah teks yang diterjemahkan menjadi suara (TTS - Text-to-Speech).

## Fitur

- Menerjemahkan teks dari bahasa Inggris ke:
  - Bahasa Indonesia (en-id)
  - Bahasa Spanyol (en-es)
  - Bahasa Prancis (en-fr)
  - Bahasa Jerman (en-de)
  - Bahasa Cina (en-zh)
- Menghasilkan suara dari teks yang diterjemahkan menggunakan Google Text-to-Speech (gTTS)
- Memutar, menjeda, dan menghentikan audio yang dihasilkan

## Persyaratan

- Python 3.7 atau lebih baru
- Dependensi Python yang diperlukan/requirements.txt:
  - torch
  - transformers
  - gtts
  - pygame
  - PyQt5
  - sacremoses

## Instalasi

1. **Instalasi Python**:
    - Pastikan Anda memiliki Python 3.7 atau versi yang lebih baru terinstal di komputer Anda. Anda dapat mengunduh dan menginstal Python dari [python.org](https://www.python.org/).

2. **Buat Virtual Environment (Opsional tetapi Disarankan)**:
    python -m venv myenv
    source myenv/bin/activate  # Untuk pengguna Unix/macOS
    myenv\Scripts\activate  # Untuk pengguna Windows

3. **Instalasi Dependensi**:
    pip install -r requirements.txt

## Struktur Direktori Proyek

Pastikan struktur direktori proyek Anda terlihat seperti ini:
project-directory/
│
├── main.py
├── translator_app.py
├── translator_logic.py
├── translator_ui.py
├── requirements.txt
└── tts/ # Folder untuk menyimpan file audio TTS

## Penggunaan

1. **Pastikan Semua File Terorganisir**:
    - Pastikan semua file (`main.py`, `translator_app.py`, `translator_logic.py`, `translator_ui.py`, `requirements.txt`) dan direktori `tts/` sudah berada di lokasi yang tepat dalam struktur direktori proyek Anda.

2. **Menjalankan Aplikasi**:
    - Buka terminal atau command prompt di direktori proyek Anda.
    - Jalankan aplikasi dengan perintah:

      python main.py

## Penggunaan Aplikasi

- Masukkan teks yang ingin diterjemahkan di kotak teks.
- Pilih bahasa tujuan dari dropdown menu.
- Klik tombol "Translate" untuk menerjemahkan teks.
- Hasil terjemahan akan ditampilkan di kotak teks hasil.
- Gunakan tombol "Play/Pause" untuk memutar atau menjeda audio hasil terjemahan.
- Gunakan tombol "Stop" untuk menghentikan audio.
