from config import *

#player image (limited at 180x180)
#monkeySprite = pygame.image.load(f'{path}/img/monkey.png')

class PlayerDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    score = db.Column(db.Integer)
    image = db.Column(db.Text) 

    def __str__(self):
        return f'{self.id} - {self.username} - {self.score} - {self.image}'

    def json(self):
        return{
            "id":self.id,
            "username":self.username,
            "score":self.score,
            "image":self.image
        }