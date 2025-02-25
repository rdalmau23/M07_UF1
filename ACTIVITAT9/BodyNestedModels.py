from typing import Annotated
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    description: str | None = Field(default=None, title="Descripció del item", max_length=300)
    name: str
    tax: float | None = None
    price: float = Field(gt=0, description="EL preu ha de ser més de 0")


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    return {"item_id": item_id, "item": item}
