from config import *
from player import *

pygame.init()

#window settings
windowWidth, windowHeight = 1280, 720
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("MONKEY GAME")
clock = pygame.time.Clock()

#background image
background = pygame.image.load(f'{path}/img/background.jpg')
backgroundWidth = background.get_width()
backgroundHeight = background.get_height()
count = 1
while backgroundWidth < windowWidth and backgroundHeight < windowHeight:
        backgroundWidth = background.get_width()*count
        backgroundHeight = background.get_height()*count
        count+=0.1
while backgroundWidth > windowWidth and backgroundHeight > windowHeight:
        backgroundWidth = background.get_width()/count
        backgroundHeight = background.get_height()/count
        count+=0.1
background = pygame.transform.scale(background, (backgroundWidth, backgroundHeight))

#player image (limited at 180x180)
monkeySprite = 'monkey.png'
monkeySpriteLocale = pygame.image.load(f'{path}/img/{monkeySprite}')
monkeySpriteWidth = monkeySpriteLocale.get_width()
monkeySpriteHeight = monkeySpriteLocale.get_height()
count = 1
while monkeySpriteWidth > 130 or monkeySpriteHeight > 130:
        monkeySpriteWidth = monkeySpriteLocale.get_width()/count
        monkeySpriteHeight = monkeySpriteLocale.get_height()/count
        count+=0.1
if monkeySpriteWidth < 90 and monkeySpriteHeight < 90:
    while monkeySpriteWidth < 90 or monkeySpriteHeight < 90:
            monkeySpriteWidth = monkeySpriteLocale.get_width()*count
            monkeySpriteHeight = monkeySpriteLocale.get_height()*count
            count+=0.1
monkeySpriteLocale = pygame.transform.scale(monkeySpriteLocale, (monkeySpriteWidth, monkeySpriteHeight))


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, username):
        super().__init__()
        self.username = username
        self.score = 0
        self.lives = 3
        self.speed = 15

        self.image, self.imageWidth, self.imageHeight = monkeySpriteLocale, monkeySpriteWidth, monkeySpriteHeight
        self.image = pygame.transform.scale(self.image, (self.imageWidth,self.imageHeight))
        self.rect = self.image.get_rect(topleft=(x, y))        

    def move(self):
        move = pygame.key.get_pressed()

        #moving left
        if move[pygame.K_LEFT] or move[pygame.K_a]:
            if self.rect.x < 0:
                pass
            else:
                self.rect.x -= self.speed

        #moving right
        if move[pygame.K_RIGHT] or move[pygame.K_d]:
            if self.rect.x > windowWidth-self.imageWidth:
                pass
            else:
                self.rect.x += self.speed

    def update(self):
        self.move()

#obstacles images (limited at 50x50)
bananaSprite = pygame.image.load(f'{path}/img/banana.png')
trashSprite = pygame.image.load(f'{path}/img/trash.png')
obstacleSpriteWidth = (bananaSprite.get_width()+trashSprite.get_width())/2
obstacleSpriteHeight = (bananaSprite.get_height()+trashSprite.get_height())/2
count = 1
while obstacleSpriteWidth > 50 or obstacleSpriteHeight > 50:
    obstacleSpriteWidth = ((bananaSprite.get_width()+trashSprite.get_width())/2)/count
    obstacleSpriteHeight = ((bananaSprite.get_height()+trashSprite.get_height())/2)/count
    count+=0.1

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.velocity = 1

        self.image, self.imageWidth, self.imageHeight = bananaSprite, obstacleSpriteWidth, obstacleSpriteHeight
        self.image = pygame.transform.scale(self.image, (self.imageWidth,self.imageHeight))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        if (self.rect.y >= windowHeight):
            self.rect.y = 1
        self.rect.y = self.rect.y + self.velocity

class Trash(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image, self.imageWidth, self.imageHeight = trashSprite, obstacleSpriteWidth, obstacleSpriteHeight
        self.image = pygame.transform.scale(self.image, (self.imageWidth,self.imageHeight))  

    def update(self):
        if (self.rect.y >= windowHeight):
            trashGroup.remove(self)
        self.rect.y = self.rect.y + self.velocity

def drawText(text, color, x, y):
    msg = pygame.font.SysFont("Lucida Console", 25).render(text, True, color)
    window.blit(msg,(x, y))

def mainMenu():
    global username
    username = ''
    keyList = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, 
           pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9, 
           pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z,
           pygame.K_UNDERSCORE, pygame.K_KP_MINUS, pygame.K_MINUS]

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
                elif event.key in keyList:
                    username += event.unicode
            
        if pygame.key.get_pressed()[pygame.K_RETURN] or pygame.key.get_pressed()[pygame.K_KP_ENTER]:
            username = username.encode('ascii', 'ignore').decode('utf-8')
            if len(username) > 32:
                username = username[0:32]
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
    minTrash = 3

    while True:
        execTime = time.time() - initTime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        
        collidedBanana = pygame.sprite.spritecollide(player, bananaGroup, False)
        if collidedBanana:
            bananaGroup.remove(collidedBanana)
            player.score += 10
            randomX = random.randint(1, windowWidth)
            randomY = random.randint(1, windowHeight)
            bananaGroup.add(Obstacle(randomX, randomY-windowHeight))
        collidedTrash = pygame.sprite.spritecollide(player, trashGroup, False)
        if collidedTrash:
            trashGroup.remove(collidedTrash)
            player.lives-=1
        if player.lives <= 0:
            break
        if len(trashGroup)<minTrash:
            randomX = random.randint(0, windowWidth-int(obstacleSpriteWidth))
            randomY = random.randint(0, windowHeight)
            trashGroup.add(Trash(randomX, randomY-windowHeight))

        for i in bananaGroup:
            if int(execTime) >= 2 and i.velocity <= 1:
                    i.velocity += 0.2
        for i in trashGroup:
            if int(execTime) >= 2 and i.velocity <= 1:
                    i.velocity += 0.2

        if int(execTime) == 27 and minTrash <= 3:
            minTrash += 1
        for i in bananaGroup:
            if int(execTime) >= 27 and i.velocity <= 1:
                    i.velocity += 0.2
        for i in trashGroup:
            if int(execTime) >= 27 and i.velocity <= 1:
                    i.velocity += 0.2

        if int(execTime) == 40 and minTrash <= 4:
            minTrash += 1
        for i in bananaGroup:
            if int(execTime) >= 40 and i.velocity <= 1.2:
                    i.velocity += 0.3
        for i in trashGroup:
            if int(execTime) >= 40 and i.velocity <= 1.2:
                    i.velocity += 0.3

        if int(execTime) == 55 and minTrash <= 5:
            minTrash += 1
        for i in bananaGroup:
            if int(execTime) >= 55 and i.velocity <= 1.5:
                    i.velocity += 0.4
        for i in trashGroup:
            if int(execTime) >= 55 and i.velocity <= 1.5:
                    i.velocity += 0.4

        if int(execTime) == 75 and minTrash <= 6:
            minTrash += 1
        if int(execTime) == 90 and minTrash <= 7:
            minTrash += 1
        for i in bananaGroup:
            if int(execTime) >= 90 and i.velocity <= 1.9:
                    i.velocity += 0.5
        for i in trashGroup:
            if int(execTime) >= 90 and i.velocity <= 1.9:
                    i.velocity += 0.5

        if int(execTime) == 105 and minTrash <= 8:
            minTrash += 1
        if int(execTime) == 120 and minTrash <= 9:
            minTrash += 1
        for i in bananaGroup:
            if int(execTime) >= 120 and i.velocity <= 2.4:
                    i.velocity += 0.4
        for i in trashGroup:
            if int(execTime) >= 120 and i.velocity <= 2.4:
                    i.velocity += 0.4

        if int(execTime) == 130 and minTrash <= 10:
            minTrash += 1
        for i in bananaGroup:
            if int(execTime) >= 130 and i.velocity <= 2.8:
                    i.velocity += 0.4
        for i in trashGroup:
            if int(execTime) >= 130 and i.velocity <= 2.8:
                    i.velocity += 0.4

        if int(execTime) == 140 and minTrash <= 11:
            minTrash += 1
        for i in bananaGroup:
            if int(execTime) >= 140 and i.velocity <= 3.2:
                    i.velocity += 0.4
        for i in trashGroup:
            if int(execTime) >= 140 and i.velocity <= 3.2:
                    i.velocity += 0.4

        if int(execTime) == 150 and minTrash <= 12:
            minTrash += 1
        for i in bananaGroup:
            if int(execTime) >= 150 and i.velocity <= 3.6:
                    i.velocity += 0.4
        for i in trashGroup:
            if int(execTime) >= 150 and i.velocity <= 3.6:
                    i.velocity += 0.4

        if int(execTime) == 155 and minTrash <= 13:
            minTrash += 1
        for i in bananaGroup:
            if int(execTime) >= 155 and i.velocity <= 4:
                    i.velocity += 0.4
        for i in trashGroup:
            if int(execTime) >= 155 and i.velocity <= 4:
                    i.velocity += 0.4

        if int(execTime) == 160 and minTrash <= 14:
            minTrash += 1
        for i in bananaGroup:
            if int(execTime) >= 160 and i.velocity <= 4.4:
                    i.velocity += 0.4
        for i in trashGroup:
            if int(execTime) >= 160 and i.velocity <= 4.4:
                    i.velocity += 0.4

        if int(execTime) == 165 and minTrash <= 15:
            minTrash += 1
        for i in bananaGroup:
            if int(execTime) >= 165 and i.velocity <= 4.8:
                    i.velocity += 0.4
        for i in trashGroup:
            if int(execTime) >= 165 and i.velocity <= 4.8:
                    i.velocity += 0.4

        if int(execTime) == 170 and minTrash <= 16:
            minTrash += 1
        if int(execTime) == 175 and minTrash <= 17:
            minTrash += 1
        if int(execTime) == 180 and minTrash <= 18:
            minTrash += 1
        if int(execTime) == 185 and minTrash <= 19:
            minTrash += 1
        if int(execTime) == 190 and minTrash <= 20:
            minTrash += 1
        if int(execTime) == 195 and minTrash <= 21:
            minTrash += 1
        if int(execTime) == 200 and minTrash <= 22:
            minTrash += 1
        if int(execTime) == 205 and minTrash <= 23:
            minTrash += 1
        if int(execTime) == 210 and minTrash <= 24:
            minTrash += 1
        if int(execTime) == 215 and minTrash <= 25:
            minTrash += 1    

        window.fill('white')
        window.blit(background, (0,0))
        sprites.update()
        sprites.draw(window)

        bananaGroup.draw(window)
        bananaGroup.update()
        trashGroup.draw(window)
        trashGroup.update()

        drawText(f"SCORE: {player.score}", 'white', 10,10)
        drawText(f"LIVES: {player.lives}", 'white', windowWidth-150,10)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

def gameOver():
    global username

    playerDB = PlayerDB(username=player.username, score=player.score, image=monkeySprite)
    db.session.add(playerDB)
    db.session.commit()

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
            
        if pygame.key.get_pressed()[pygame.K_RETURN] or pygame.key.get_pressed()[pygame.K_KP_ENTER]:
            break

        window.blit(background, (0,0))

        drawText(f"{player.username}, YOU LOSE.", 'black', windowWidth/2-64, windowHeight/2-40)
        drawText(f"YOUR SCORE: {player.score}", 'black', windowWidth/2-64, windowHeight/2-20)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

mainMenu()

bananaGroup = pygame.sprite.Group()
for i in range(20):
    randomX = random.randint(0, windowWidth-int(obstacleSpriteWidth))
    randomY = random.randint(0, windowHeight)
    bananaGroup.add(Obstacle(randomX, randomY-windowHeight))
trashGroup = pygame.sprite.Group()
for i in range(5):
    randomX = random.randint(0, windowWidth-int(obstacleSpriteWidth))
    randomY = random.randint(0, windowHeight)
    trashGroup.add(Trash(randomX, randomY-windowHeight))

x = windowWidth/2
y = windowHeight-monkeySpriteHeight+1

#playerDB = db.session.query(Player).first
player = Player(x, y, username)
sprites = pygame.sprite.Group()
sprites.add(player)
initTime = time.time()

game()
gameOver()