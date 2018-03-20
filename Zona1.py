__author__ = '@MkDVice'

# REPRODUTOR MP3

from pygame import mixer

mixer.init() # comando para inicar o pygame
mixer.music.load('capital.mp3') # escolhendo a música
mixer.music.play() # tocando a música
input('Tudo que vai - Capital Inicial') # nome da música