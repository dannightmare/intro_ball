import pygame
import sys
import time
pygame.init()

size = width, height = 320, 240
speed = [0,0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

# the ball from the pygame site
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_q:
                sys.exit()
            if key == pygame.K_DOWN:
                speed[1] += 1
            elif key == pygame.K_UP:
                speed[1] += -1
            elif key == pygame.K_LEFT:
                speed[0] += -1
            elif key == pygame.K_RIGHT:
                speed[0] += 1
        if event.type == pygame.KEYUP:
            key = event.key
            if key == pygame.K_DOWN:
                speed[1] -= 1
            elif key == pygame.K_UP:
                speed[1] -= -1
            elif key == pygame.K_LEFT:
                speed[0] -= -1
            elif key == pygame.K_RIGHT:
                speed[0] -= 1

    print(speed)
    ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    time.sleep(0.0167)
