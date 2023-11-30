from config import *
from player import *

if os.path.exists(fileDB):
    os.remove(fileDB)
db.create_all()
print("Table created")
