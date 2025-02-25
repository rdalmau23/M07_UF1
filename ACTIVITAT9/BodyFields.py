from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float = Field(gt=0, description="The price must be greater than zero")
    description: str | None = Field(default=None, max_length=300, title="The description of the item")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    return {"item_id": item_id, "item": item}
