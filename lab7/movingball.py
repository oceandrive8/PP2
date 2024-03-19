import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((600,400), pygame.RESIZABLE)
pygame.display.set_caption("Moving Ball")
width = 600
height = 400

WHITE = (255, 255, 255)
RED = (255, 0, 0)


ball_r = 25
ball_x = width // 2
ball_y = height // 2
ball_speed = 20


running=1
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_r)
    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - ball_speed >= ball_r:
                    ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + ball_speed <= height - ball_r:
                    ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - ball_speed >= ball_r:
                    ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + ball_speed <= width - ball_r:
                    ball_x += ball_speed
