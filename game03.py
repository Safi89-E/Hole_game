import pygame
width = 800
height = 600
x = 50
y = 50
x_change = 0
y_change = 0
black = (0,0,0)
white = (255,255,255)
red = (255 , 0 ,0)
gameDisplay = pygame.display.set_mode((width , height))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()
crashed = False
while not crashed:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_change = 5
                y_change = 0
            if event.key == pygame.K_LEFT:
                x_change = -5
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -5
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 5
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, red, [x, y, 50, 50])
        pygame.display.update()