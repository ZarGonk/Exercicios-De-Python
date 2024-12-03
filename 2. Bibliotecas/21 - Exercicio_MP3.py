#Desafio 21 - faça um programa em python que abra e reproduza o audio de um arquivo mp3
import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Inicializa o pygame
pygame.init()

# Carrega o arquivo de áudio
file_path = "mcpikachu-la-no-meu-barraco.mp3"  # Substitua pelo caminho do seu arquivo MP3
pygame.mixer.music.load(file_path)

# Reproduz o áudio
pygame.mixer.music.play()

print("Reproduzindo áudio... Pressione 'Enter' para parar.")
input()  # Aguarda o usuário pressionar Enter para parar a execução

# Para a música e finaliza o pygame
pygame.mixer.music.stop()
pygame.quit()
