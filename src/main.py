import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

# Screen stuff
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

rect_color = (255, 0, 0)
rect_pos = [50, 50]
rect_size = (100, 50)

font = pygame.font.Font(None, 25)
text = font.render('Hello There', True, green, blue)
textRect = text.get_rect()
textRect.center = (screen_width / 2, screen_height / 2)
moveSpeed = 1.5

clock = pygame.time.Clock()
targetFps = 60

ballSize = 10


while True:

    dt = clock.tick(targetFps)
    keys = pygame.key.get_pressed()

    # Move left / right
    if keys[pygame.K_LEFT] and rect_pos[0] > 0:
        rect_pos[0] -= moveSpeed * dt
    if keys[pygame.K_RIGHT] and rect_pos[0] < screen_width-rect_size[0]: # Stop it from exiting the screen
        rect_pos[0] += moveSpeed * dt
    
    # Move up / down
    if keys[pygame.K_UP] and rect_pos[1] > 0:
        rect_pos[1] -= moveSpeed * dt
    if keys[pygame.K_DOWN] and rect_pos[1] < screen_height-rect_size[1]:
        rect_pos[1] += moveSpeed * dt


    screen.fill(black)
    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_pos, rect_size))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    
    pygame.display.flip()