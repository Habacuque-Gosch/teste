import uvicorn
from typing import Union
from fastapi import FastAPI, HTTPException
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


# @app.get("/itens/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/")
def index():
    return {"items": items}

@app.get('/details-item/{item_id}')
def query_item_by_id(item_id: int) -> Item:

    if item_id not in items: 
        raise HTTPException(status_code=404, detail=f'Item with item_id={item_id} does not exist.')
    
    return items[item_id]

select = dict[
    str, str | int | float | Category | None
]

@app.get('/items/')
def query_item_by_params(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,

) -> dict[str, select]:
    def check_item(item: Item) -> bool:
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category,

            )
        )
    
    select = [item for item in items.values() if check_item(item)]

    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "select": select,
    }


# @app.put("/itens/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}



# app.include_router(modules.routers.route1_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)