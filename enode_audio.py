import base64
import tkinter as tk
from tkinter import filedialog

# Créer une fenêtre Tkinter cachée (elle ne sera pas affichée)
root = tk.Tk()
root.withdraw()

# Ouvrir la fenêtre de dialogue pour choisir un fichier
file_path = filedialog.askopenfilename(
    title="Sélectionnez un fichier audio",
    filetypes=[("Fichiers MP3", "*.mp3")]
)

# Vérifier si un fichier a été sélectionné
if file_path:
    try:
        # Lire le fichier MP3 et l'encoder en base64
        with open(file_path, "rb") as audio_file:
            encoded_string = base64.b64encode(audio_file.read())

        # Décoder la chaîne base64 en une chaîne UTF-8 pour affichage
        encoded_string_utf8 = encoded_string.decode('utf-8')

        # Afficher la chaîne base64 complète
        print("Le fichier audio a été encodé avec succès en base64.")
        print("Voici la chaîne base64 complète :")
        print(encoded_string_utf8)  # Affiche la chaîne base64 complète

        # Optionnel : Enregistrer la chaîne encodée dans un fichier texte
        with open("encoded_audio.txt", "w") as encoded_file:
            encoded_file.write(encoded_string_utf8)
        print("La chaîne base64 a été enregistrée dans 'encoded_audio.txt'.")

    except Exception as e:
        print(f"Une erreur est survenue lors de l'encodage du fichier: {e}")
else:
    print("Aucun fichier n'a été sélectionné.")
