import pygame

pygame.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("al0i's game")

x,y = 640,360
vel = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    move = pygame.key.get_pressed()
    if move[pygame.K_w] or move[pygame.K_UP]:
        y -= vel
    if move[pygame.K_s] or move[pygame.K_DOWN]:
        y += vel
    if move[pygame.K_d] or move[pygame.K_RIGHT]:
        x += vel
    if move[pygame.K_a] or move[pygame.K_LEFT]:
        x -= vel

    window.fill('white')
    pygame.draw.circle(window, (255,0,0), [x,y], 90, 0)
    pygame.display.flip()
    clock.tick(60)