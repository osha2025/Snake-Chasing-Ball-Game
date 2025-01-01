import pygame
import sys

WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (50, 50, 50)
BALL_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ثعبان يطارد الكرة")
clock = pygame.time.Clock()

ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_radius = 15

snake_pos = [100, 100]
snake_speed = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            ball_pos[0], ball_pos[1] = event.pos

    if snake_pos[0] < ball_pos[0]:
        snake_pos[0] += snake_speed
    if snake_pos[0] > ball_pos[0]:
        snake_pos[0] -= snake_speed
    if snake_pos[1] < ball_pos[1]:
        snake_pos[1] += snake_speed
    if snake_pos[1] > ball_pos[1]:
        snake_pos[1] -= snake_speed




    screen.fill(BACKGROUND_COLOR)
    
    

    pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    pygame.draw.rect(screen, SNAKE_COLOR, (snake_pos[0], snake_pos[1], 20, 20))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()