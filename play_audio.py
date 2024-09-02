import base64
import io
import pygame
import ctypes
import sys
import tkinter as tk
from tkinter import filedialog

def hide_console():
    # Fonction pour masquer la console
    if sys.platform == "win32":
        ctypes.windll.kernel32.SetConsoleTitleW("Hidden Console")
        ctypes.windll.kernel32.FreeConsole()

def show_error(message):
    # Fonction pour afficher un message d'erreur sans console
    ctypes.windll.user32.MessageBoxW(0, message, "Erreur", 0x10)

def open_file_dialog():
    # Fonction pour ouvrir une boîte de dialogue de sélection de fichier
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale
    file_path = filedialog.askopenfilename(
        title="Sélectionner le fichier texte contenant la chaîne Base64",
        filetypes=[("Fichiers texte", "*.txt")]
    )
    return file_path

# Masquer la console
hide_console()

try:
    # Ouvrir la boîte de dialogue de sélection de fichier
    base64_file_path = open_file_dialog()
    if not base64_file_path:
        raise FileNotFoundError("Aucun fichier sélectionné")

    # Charger la chaîne Base64 depuis le fichier texte sélectionné
    with open(base64_file_path, 'r') as file:
        encoded_audio_string = file.read().strip()
    
    # Décoder la chaîne base64 en données binaires
    audio_data = base64.b64decode(encoded_audio_string)

    # Charger les données audio en mémoire
    audio_stream = io.BytesIO(audio_data)

    # Initialiser pygame mixer
    pygame.mixer.init()

    # Charger et jouer le fichier MP3 depuis le flux en mémoire
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()

    # Attendre que la musique se termine
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

except Exception as e:
    # Afficher une boîte de message d'erreur
    show_error(f"Une erreur est survenue : {e}")
