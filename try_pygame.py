import pygame

WINDOW_SIZE = (600, 400)

screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill((50, 100, 220))
ball = pygame.image.load("ball.png")
ballpos = [250, 150]
ball.set_colorkey((255, 255, 255))
screen.blit(ball, ballpos)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
