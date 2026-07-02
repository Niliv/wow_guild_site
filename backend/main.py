from fastapi import FastAPI, Depends
import database as db
import models
from sqlalchemy.orm import Session
from models import Members, Character

app = FastAPI()

models.Base.metadata.create_all(bind=db.engine)

ID = 0

# ---------------- Members ---------------
@app.post("/members")
def add_member(name: str, session = Depends(db.get_db)):
    new_member = Members(name = name)

    session.add(new_member)
    session.commit()

    return new_member

@app.get("/members")
def get_members(session: Session = Depends(db.get_db)):
    return session.query(Members).all()


# --------------- Characters -----------
@app.post("/characters")
def add_character(name, realm, owner, session = Depends(db.get_db)):

    new_char = Character(id = 0, name = name, realm = realm, class_ = models.WoWClasses.paladin, whose = owner)

    session.add(new_char)
    session.commit()

    return new_char

@app.get("/characters")
def get_characters(session: Session = Depends(db.get_db)):
    return session.query(Character).all()



app.frontend("/", directory="../frontend")