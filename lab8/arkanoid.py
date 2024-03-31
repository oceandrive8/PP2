import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0,0,0 )

# Paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('materials/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Block settings
block_list = []
color_list = []

# Adding breakable blocks
breakable_blocks = 35  # Total number of breakable blocks
for i in range(breakable_blocks):
    x = random.randrange(0, W - 100, 150)  # Random x position with a gap of 150 pixels between each block
    y = random.randrange(50, H // 2, 75)    # Random y position within the top half of the screen with a gap of 75 pixels between each block
    block = pygame.Rect(x, y, 100, 50)
    block_list.append(block)
    color_list.append((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))

# Adding unbreakable blocks among breakable blocks
unbreakable_blocks = 5  # Number of unbreakable blocks
for i in range(unbreakable_blocks):
    x = random.randrange(0, W - 100, 150)  # Random x position with a gap of 150 pixels between each block
    y = random.randrange(50, H // 2, 75)    # Random y position within the top half of the screen with a gap of 75 pixels between each block
    block = pygame.Rect(x, y, 100, 50)
    block_list.append(block)
    color_list.append((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))  # Random color for unbreakable blocks

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (135, 206, 235))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

def increase_ball_speed():
    global ballSpeed
    ballSpeed += 0.1

def shrink_paddle():
    global paddleW
    if paddleW > 50:  # Minimum paddle width
        paddleW -= 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)] # Drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    # Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()
        
    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
        
    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    # Increase ball speed and shrink paddle over time
    if game_score % 5== 0:  # Increase ball speed every 5 point
        increase_ball_speed()
    if game_score % 5== 0:  # Shrink paddle every 5 points
        shrink_paddle()

    pygame.display.flip()
    clock.tick(FPS)
 




