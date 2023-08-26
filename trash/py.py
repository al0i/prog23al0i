import pygame
import random

pygame.init()

# definir a tela
MAX_X = 800
MAX_Y = 600
screen = pygame.display.set_mode((MAX_X, MAX_Y))

clock = pygame.time.Clock()

# classe JOGADOR!!
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 255)) # preencher com uma cor
        self.rect = self.image.get_rect(topleft=(x, y)) # obter retângulo em torno da imagem
        self.pontos = 0
        self.velocity = 5

# classe obstáculo
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_y = 1
    def update(self):
        if (self.rect.y >= MAX_Y):
            self.rect.y = 1
        self.rect.y = self.rect.y + self.velocity_y
        
# posições iniciais do player
x = 50
y = 320

# criação do jogador
player = Player(x, y)
player_group = pygame.sprite.Group()
player_group.add(player)

# criação de 3 obstáculos
o1 = Obstacle(50, 400, 10, 20)
o2 = Obstacle(50, 430, 10, 20)
o3 = Obstacle(70, 460, 10, 20)
# criação do grupo de obstáculos
platform_group = pygame.sprite.Group()
# inserir os obstáculos no grupo
platform_group.add(o1, o2, o3)

# criar mais um monte de obstáculos :-p
for i in range(0,20): # criar 20 objetos
    mx = random.randint(1, MAX_X-30)
    my = 10 + random.randint(1, MAX_Y-30)
    platform_group.add(Obstacle(mx, my, 30, 30))

# inicializa a janela
pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))

# continua executando? Sim!
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # captura de eventos do teclado
    pk = pygame.key.get_pressed()

    # verifica se tem que fazer algo
    if pk[pygame.K_LEFT]:
        player.rect.x -= player.velocity
    if pk[pygame.K_RIGHT]:
        player.rect.x += player.velocity
    if pk[pygame.K_UP]:
        player.rect.y -= player.velocity
    if pk[pygame.K_DOWN]:
        player.rect.y += player.velocity

    # colidiu? O último parâmetro igual a TRUE diz que
    # o obstáculo deve SUMIR da tela quando houver colisão
    quem_colidiu = pygame.sprite.spritecollide(player, platform_group, False)

    # se colidiu...
    if quem_colidiu:
        # contabiliza pontos para o jogador :-) depende de quantos coletou
        player.pontos += len(quem_colidiu)
        # remove o obstáculo do grupo
        platform_group.remove(quem_colidiu)
        # mostra quantos objetos foram coletados
        print("objetos coletados:", player.pontos)
    
    screen.fill("yellow") # pinta o fundo de amarelo
    player_group.draw(screen) # mostra o jogador
    platform_group.draw(screen) # mostra os obstáculos
    platform_group.update() # movimenta todos os obstáculos
    pygame.display.flip() # atualiza a tela
    clock.tick(60)
pygame.quit()
