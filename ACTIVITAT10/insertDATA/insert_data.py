import pandas as pd
from sqlalchemy.orm import Session
from database import engine, Base
from models import Word

Base.metadata.create_all(bind=engine)

def insert_data():
    df = pd.read_csv("data.csv")  
    with Session(engine) as session:
        for _, row in df.iterrows():
            word = Word(word=row["word"], theme=row["theme"])
            session.add(word)
        session.commit()
        print(f"Se han insertado {len(df)} palabras en la base de datos.")

if __name__ == "__main__":
    insert_data()
