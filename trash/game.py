import pygame
import os

pygame.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("al0i's game")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, height):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('mamaco.jpg'))
        self.numb = 0
        self.image = self.sprites[self.numb]
        self.image = pygame.transform.scale(self.image, (550/3,641/3))
        self.speed = 15
        self.radius = 10
        self.x = x
        self.y = height#-self.radius
        self.rect = self.image.get_rect()

    def move(self):
        move = pygame.key.get_pressed()
        if move[pygame.K_LEFT] or move[pygame.K_a]:
            if player.x < 0+player.radius:
                pass
            else:
                player.x -= player.speed

        if move[pygame.K_RIGHT] or move[pygame.K_d]:
            if player.x > width+player.radius:
                pass
            else:
                player.x += player.speed

        if move[pygame.K_UP] or move[pygame.K_w]:
            if player.y > width+player.radius:
                pass
            else:
                player.y -= player.speed

        if move[pygame.K_DOWN] or move[pygame.K_s]:
            if player.y > width+player.radius:
                pass
            else:
                player.y += player.speed

        if move[pygame.K_SPACE]:
            player.radius += 1

    def update(self):
        self.move()

x = 640
sprites = pygame.sprite.Group()
player = Player(x, height)
sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    
    

    print(player.x, player.y)

    window.fill('white')
    sprites.update()
    sprites.draw(window)

    pygame.draw.circle(window, (255,0,0), [player.x,player.y], player.radius, 0)
    sprites.draw(window)
    sprites.update()
    pygame.display.flip()
    clock.tick(60)