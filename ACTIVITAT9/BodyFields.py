from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float = Field(gt=0, description="El preu ha de ser més de 0")
    description: str | None = Field(default=None, max_length=300, title="Descripció del item")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    return {"item_id": item_id, "item": item}
