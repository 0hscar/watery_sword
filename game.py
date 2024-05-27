import pygame

pygame.init()

# Screen stuff
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

rect_color = (255, 0, 0)
rect_pos = (50, 50)
rect_size = (100, 50)
pygame.draw.rect(screen, rect_color, pygame.Rect(rect_pos, rect_size))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()