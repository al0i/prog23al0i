import pygame, os, random

pygame.init()
path = os.path.dirname(os.path.abspath(__file__))

#window settings
windowWidth, windowHeight = 1280, 720
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("MONKEY GAME")
clock = pygame.time.Clock()

#background image
background = pygame.image.load(f'{path}/img/morroAzul.jpg')
background = pygame.transform.scale(background, (500*3, 281*3))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, username):
        super().__init__()
        self.imageFile = os.path.join(f'{path}\img\manke.png')
        self.image = pygame.image.load(self.imageFile)        
        self.imageWidth, self.imageHeight = self.image.get_width(), self.image.get_height()
        self.imageWidth, self.imageHeight = self.imageWidth/3, self.imageHeight/3
        self.image = pygame.transform.scale(self.image, (self.imageWidth,self.imageHeight)) #pygame.Surface((self.imageWidth, self.imageHeight)) #

        self.rect = self.image.get_rect(topleft=(x, y))
        self.username = username


        #self.sprites = []
        #self.sprites.append(pygame.image.load('manke.png'))
        #self.numb = 0
        #self.image = self.sprites[self.numb]
        self.speed = 15
        #self.radius = 10
        #self.x = x
        #self.y = y
        #self.rect = self.image.get_rect()

    def move(self):
        move = pygame.key.get_pressed()
        
        #moving left
        if move[pygame.K_LEFT] or move[pygame.K_a]:
            if self.rect.x < 0:
                pass
            else:
                self.rect.x -= player.speed

        #moving right
        if move[pygame.K_RIGHT] or move[pygame.K_d]:
            if self.rect.x > windowWidth-player.imageWidth:
                pass
            else:
                self.rect.x += player.speed

        '''#moving up
        if move[pygame.K_UP] or move[pygame.K_w]:
            if self.rect.y < 0:
                pass
            else:
                self.rect.y -= player.speed

        #moving down
        if move[pygame.K_DOWN] or move[pygame.K_s]:
            if self.rect.y > windowHeight-player.imageHeight:
                pass
            else:
                self.rect.y += player.speed'''

    def salvar_xy(self):
        self.antes_x = self.rect.x
        self.antes_y = self.rect.y

    def restaurar_xy(self):
        self.rect.x = self.antes_x
        self.rect.y = self.antes_y
    
    def update(self):
        self.salvar_xy()
        self.move()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, nome_imagem):
        super().__init__()
        arquivo_banana = os.path.join(path, nome_imagem)
        self.image = pygame.image.load(arquivo_banana)
        self.imageWidth = 800/19#1086/15
        self.imageHeight = 980/19#1085/15
        self.image = pygame.transform.scale(self.image, (self.imageWidth,self.imageHeight))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = 1

    def update(self):
        if (self.rect.y >= windowWidth):
            self.rect.y = 1
        self.rect.y = self.rect.y + self.velocity

obstacleGroup = pygame.sprite.Group()
for i in range(20):
    mx = random.randint(1, windowWidth-30)
    my = random.randint(1, windowHeight-30)+10
    obstacleGroup.add(Obstacle(mx, my, 30, 30, 'img/panana.png'))
    
#o1 = Obstacle(50, 400, 10, 20)
#obsGroup.add(o1)

x = 640
y = windowHeight-376/2.7





def drawText(text, color, x, y):
    msg = pygame.font.SysFont("Lucida Console", 25).render(text, True, color)
    window.blit(msg,(x, y))


def mainMenu():
    global username
    username = ''
    inputRect = pygame.Rect(windowWidth/2-64, windowHeight/2-16, 100, 32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE or event.key==pygame.K_DELETE:
                    username = username[:-1]
                    break
                else:
                    username += event.unicode
            
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            break

        window.blit(background, (0,0))

        pygame.draw.rect(window, 'black', inputRect, width=3)
        textSurface = pygame.font.SysFont("Lucida Console", 25).render(username, True, 'black')
        window.blit(textSurface, (inputRect.x+5, inputRect.y+5))
        inputRect.w = max(100, textSurface.get_width()+10)
        drawText("Insert username:", 'black', windowWidth/2-64, windowHeight/2-40)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        
        quem_colidiu = pygame.sprite.spritecollide(player, obstacleGroup, False)
        if quem_colidiu:
            obstacleGroup.remove(quem_colidiu)


        #print(player.x, player.y)

        window.fill('white')

        window.blit(background, (0,0))

        drawText("EU TENHO A FORÇA", 'black', 100,10)


        sprites.update()
        sprites.draw(window)

        #pygame.draw.rect(window, (0, 0, 255), [0, windowHeight-player.imageHeight, windowWidth, player.imageHeight/2])


        obstacleGroup.draw(window)
        obstacleGroup.update()

        #escreve_texto(screen, 130, 10, "Cavernas dos awdada", (0,0,255))
        pygame.display.update()

        #pygame.draw.circle(window, (255,0,0), [player.x,player.y], player.radius, 0)
        print(player.imageWidth)
        pygame.display.flip()
        clock.tick(60)
        #print(player.rect.x, player.rect.y)



mainMenu()

sprites = pygame.sprite.Group()
player = Player(x, y, username)
sprites.add(player)

game()