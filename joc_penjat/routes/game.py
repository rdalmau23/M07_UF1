from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import obtenir_db
from models import Usuari, Joc

ruta = APIRouter()

@ruta.post("/usuaris/")
def afegir_usuari(nom: str, db: Session = Depends(obtenir_db)):
    nou_usuari = Usuari(nom=nom)
    db.add(nou_usuari)
    db.commit()
    return {"missatge": "Usuari registrat"}

@ruta.post("/jocs/")
def iniciar_joc(nom: str, mot: str, db: Session = Depends(obtenir_db)):
    jugador = db.query(Usuari).filter(Usuari.nom == nom).first()
    if not jugador:
        return {"error": "Usuari inexistent"}
    
    nou_joc = Joc(usuari_id=jugador.id, mot=mot, intents=0, estat="actiu")
    db.add(nou_joc)
    db.commit()
    return {"missatge": "Joc començat"}

@ruta.get("/estadistiques/")
def obtenir_estadistiques(nom: str, db: Session = Depends(obtenir_db)):
    jugador = db.query(Usuari).filter(Usuari.nom == nom).first()
    if not jugador:
        return {"error": "Usuari inexistent"}
    
    total_jocs = len(jugador.jocs)
    jocs_guanyats = sum(1 for j in jugador.jocs if j.estat == "guanyat")
    return {"total_jocs": total_jocs, "jocs_guanyats": jocs_guanyats}
