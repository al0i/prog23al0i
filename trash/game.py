import pygame
import os

pygame.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("al0i's game")

caminho = os.path.dirname(os.path.abspath(__file__))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, nome_imagem, nome):
        super().__init__()
        arquivo_imagem = os.path.join(caminho, nome_imagem)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.nome = nome

        self.sprites = []
        self.sprites.append(pygame.image.load('mamaco.jpg'))
        self.numb = 0
        self.image = self.sprites[self.numb]
        #self.image = pygame.transform.scale(self.image, (550/3,641/3))
        self.speed = 15
        self.radius = 10
        self.x = x
        self.y = y
        #self.rect = self.image.get_rect()

    def move(self):
        move = pygame.key.get_pressed()
        if move[pygame.K_LEFT] or move[pygame.K_a]:
            if self.rect.x < 0+player.radius:
                pass
            else:
                self.rect.x -= player.speed

        if move[pygame.K_RIGHT] or move[pygame.K_d]:
            if self.rect.x > width+player.radius:
                pass
            else:
                self.rect.x += player.speed

        '''if move[pygame.K_UP] or move[pygame.K_w]:
            if self.rect.y > width+player.radius:
                pass
            else:
                self.rect.y -= player.speed

        if move[pygame.K_DOWN] or move[pygame.K_s]:
            if self.rect.y > width+player.radius:
                pass
            else:
                self.rect.y += player.speed

        if move[pygame.K_SPACE]:
            player.radius += 1'''

    def salvar_xy(self):
        self.antes_x = self.rect.x
        self.antes_y = self.rect.y

    def restaurar_xy(self):
        self.rect.x = self.antes_x
        self.rect.y = self.antes_y
    
    def update(self):
        self.salvar_xy()
        self.move()


x = 640
y = 360

sprites = pygame.sprite.Group()
player = Player(x, y, 'mamaco.jpg', 'macacao007')
sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    
    

    #print(player.x, player.y)

    window.fill('white')

    sprites.update()
    sprites.draw(window)

    #escreve_texto(screen, 130, 10, "Cavernas dos awdada", (0,0,255))
    pygame.display.update()

    #pygame.draw.circle(window, (255,0,0), [player.x,player.y], player.radius, 0)

    pygame.display.flip()
    clock.tick(60)