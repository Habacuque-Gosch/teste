import uvicorn
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import modules.routers.route1_router
from enum import Enum




app = FastAPI()


class Category(Enum):
    tools = 'tools'
    consumables = 'consumables'
    pass

class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category

    def __str__(self):
        return self.name

items = {
    0: Item(name='Hammer', price=9.99, count=20, id=0, category=Category.tools),
    1: Item(name='Nails', price=1.99, count=4, id=1, category=Category.consumables)
}


@app.get("/")
def index():
    return {"items": items}


# @app.put("/itens/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# app.include_router(modules.routers.route1_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


