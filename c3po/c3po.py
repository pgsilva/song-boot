import pygame
import time
import random


def play_c3po():
    track = str(random.randint(1, 5))
    try:

        print('C3PO chose new song for the event')
        pygame.mixer.init()
        pygame.mixer.music.load('song-' + track + '.mp3')
        pygame.mixer.music.play()

        time.sleep(5)
        user = input('dont liked ? [S/s] \n')
        if(str(user) == 's' or str(user) == 'S'):
            pygame.mixer.stop()
            play_c3po()

    except Exception as err:
        print(err)


play_c3po()
