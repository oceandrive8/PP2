import pygame as pg
import sys

pg.init()

sc = pg.display.set_mode((500, 500))
pg.display.set_caption("Music Player")

bcg=pg.image.load("images/pic.jpg")
background = pg.transform.scale(bcg, (500,500))

playlist = ['music/Creep.mp3', 'music/SZAGD.mp3', 'music/Sade.mp3','music/frocean.mp3']
index = 0



while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            sys.exit()

        elif i.type == pg.KEYUP:
            if i.key == pg.K_SPACE:
                pg.mixer.music.load(playlist[index])
                pg.mixer.music.play()
            elif i.key == pg.K_s:
                pg.mixer.music.stop()
            elif i.key == pg.K_n:
                index = (index + 1) % len(playlist)
                pg.mixer.music.load(playlist[index])
                pg.mixer.music.play()
            elif i.key == pg.K_p:
                index = (index - 1) % len(playlist)
                pg.mixer.music.load(playlist[index])
                pg.mixer.music.play()
    
    sc.blit(background, (0, 0))

    pg.display.flip()
    pg.time.delay(20)



"""
KEYBOARD AND ACTION
Space---->playing song(пробел/whitespace)
n-------->next song
p-------->previous song
s-------->stop the music

"""

