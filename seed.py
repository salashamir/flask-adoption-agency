"""Seed file to prepopulate db"""

from models import Pet, db
from app import app

# CREATE TABLES
db.drop_all()
db.create_all()

# empty tables
Pet.query.delete()

# add pets
bubbles = Pet(name="Bubbles", species="turtle", age=3, notes="Likes lettuce")
dino = Pet(name="Dino", species="salamander", age=2, notes="Loves sleeping")
Colt = Pet(name="Colt", species="cat", age=8, notes="Needs to be brushed daily")
Hammer = Pet(name="Hammer", species="dog", age=11, notes="Gets easily excited")
cockatoo = Pet(name="Cockatoo", species="bird", age=1, notes="Keep in cage")

# add to db
db.session.add(bubbles)
db.session.add(dino)
db.session.add(Colt)
db.session.add(Hammer)
db.session.add(cockatoo)

db.session.commit()