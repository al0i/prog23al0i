from config import *
from table.player import *

if os.path.exists(fileDB):
    os.remove(fileDB)
db.create_all()
print("Table created")
