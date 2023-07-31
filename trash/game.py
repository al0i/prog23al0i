import pygame

pygame.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("al0i's game")

class Player:
    def __init__(self):
        self.x = 
    pygame.draw.circle(window, (255,0,0), [640,360], 90, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    window.fill('white')

    player(window)
    pygame.display.flip()
    clock.tick(60)