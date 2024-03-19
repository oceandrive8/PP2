import pygame, sys
import math
from datetime import datetime


pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")


bgr= pygame.image.load("images/main-clock.png")
background= pygame.transform.scale(bgr, (WIDTH, HEIGHT))


mhand = pygame.image.load("images/right-hand.png")
min_hand = pygame.transform.scale(mhand, (210, 70))

shand = pygame.image.load("images/left-hand.png")
sec_hand = pygame.transform.scale(shand, (210, 70))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    screen.blit(background, (0, 0))

    now = datetime.now()
    
    min_angle =-((now.minute+1)*6)+90
    
    
    sec_angle = -(now.second *6)+90

    
    rminhand = pygame.transform.rotate(min_hand, min_angle)
    rsechand = pygame.transform.rotate(sec_hand, sec_angle)

    
    screen.blit(rminhand, (WIDTH // 2 -rminhand.get_width() // 2, HEIGHT // 2 - rminhand.get_height() // 2))
    screen.blit(rsechand, (WIDTH // 2 - rsechand.get_width() // 2, HEIGHT // 2 - rsechand.get_height() // 2))

    
    pygame.display.flip()

    
    pygame.time.Clock().tick(60)





