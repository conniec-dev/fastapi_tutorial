# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/users/me")
# async def read_user_me(item_id: int):
#     return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# from enum import Enum

# from fastapi import FastAPI

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lexnet"

# app = FastAPI()

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

# from fastapi import FastAPI

# app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"} , {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# from typing import Optional

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id" : item_id}

# from typing import Optional

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


# from typing import Optional

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/users/{user_id}/items/{item:id"})
# async def read_user_item(
#     user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#     return item

# from typing import Optional
# from fastapi import FastAPI


# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item

# from typing import Optional

# from fastapi import FastAPI

# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


# app = FastAPI()

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item

# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


# app = FastAPI()

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


# app = FastAPI()

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: Optional[str] = None):
#     result = {"item_id": item_id, *+item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

# from typing import Optional

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
#     results = {"items" : [{"item_id": "Foo"}, {"item_id" : "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# from fastapi import FastAPI, Query
# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: str = Query(..., min_length=3)):
#     results = {"items" : [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# from typing import List, Optional
# from fastapi import FastAPI, Query
# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, alias="item-query", title="Query string", description="Query strings fot the items to search in the database that have a good match", min_length=3, max_length=50, regex="^fixedquery$", deprecated=True)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
