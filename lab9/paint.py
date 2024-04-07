import pygame
import sys
import random
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    size = 50
    x = 0
    y = 0
    mode = 'blue'  # Default mode is blue
    points = []
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'  # Change the mode to red
                elif event.key == pygame.K_g:
                    mode = 'green'  # Change the mode to green
                elif event.key == pygame.K_b:
                    mode = 'blue'  # Change the mode to blue
                elif event.key == pygame.K_d:
                    mode = 'rect'  # Change mode to draw rectangle
                elif event.key == pygame.K_c:
                    mode = 'circle'  # Change mode to draw circle
                elif event.key == pygame.K_e:
                    mode = 'erase'  # Change mode to erase
                elif event.key == pygame.K_s:
                    mode = 'square'  # Change mode to square
                elif event.key == pygame.K_t:
                    mode = 'rtriangle'  # Change mode to right triangle
                elif event.key == pygame.K_q:
                    mode = 'equitriangle'  # Change mode to equilateral triangle
                elif event.key == pygame.K_o:
                    mode = 'rhombus'  # Change mode to rhombus

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows size
                    size = min(200, size + 10)
                elif event.button == 3:  # right click shrinks size
                    size = max(10, size - 10)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # Set color based on their selected mode
        if mode == 'red':
            color = (255, 0, 0)
        elif mode == 'green':
            color = (0, 255, 0)
        elif mode == 'blue':
            color = (0, 0, 255)
        
        # draw all figures/line
        i = 0
        while i < len(points) - 1:
            if mode == 'rect':
                pygame.draw.rect(screen, color, (points[i], (size, size+20)))  # Draw rectangle
            elif mode == 'circle':
                pygame.draw.circle(screen, color, points[i], size-30)  # Draw circle
            elif mode == 'square':
                pygame.draw.rect(screen, color, (points[i], (size, size)))  # Draw square
            elif mode == 'rtriangle':
                pygame.draw.polygon(screen, color, [(points[i][0], points[i][1] + size // 2),  # Draw right triangle
                                                    (points[i][0] + size, points[i][1] + size // 2),
                                                    (points[i][0], points[i][1] + size)])
            elif mode == "equitriangle":
                pygame.draw.polygon(screen, color, [(points[i][0], points[i][1] + size // 2),  # Draw equilateral triangle
                                                    (points[i][0] + size // 2, points[i][1] - size // 2),
                                                    (points[i][0] + size, points[i][1] + size // 2)])
            elif mode == "rhombus":
                pygame.draw.polygon(screen, color, [(points[i][0], points[i][1] + size // 2),  # Draw rhombus
                                                    (points[i][0] + size // 2, points[i][1]),
                                                    (points[i][0] + size, points[i][1] + size // 2),
                                                    (points[i][0] + size // 2, points[i][1] + size)])
            elif mode == 'erase':
                pygame.draw.circle(screen, (0, 0, 0), points[i], size // 2)  # Erase
            else:
                drawLineBetween(screen, i, points[i], points[i + 1], size-10, color)
            i += 1
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()





""" 
BUTTON         FIGURES
o              rhombus
d              rectangle
t              right triangle
q              equilateral triangle
c              circle
s              squar
"""

