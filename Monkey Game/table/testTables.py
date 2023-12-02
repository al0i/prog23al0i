from config import *
from table.player import *

p1 = PlayerDB(username='sigmund-freud',
            score=180,
            image='monkey.png')

p2 = PlayerDB(username='al0i',
            score=1080,
            image='manke.jpg')

p3 = PlayerDB(username='barbaraakk',
            score=920,
            image='mamaco.png')

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.commit()

print("Data inserted")