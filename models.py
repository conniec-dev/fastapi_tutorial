# from typing import List, Optional

# from fastapi import FastAPI

# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: List[str] = []


# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     return item

# from typing import Optional

# from fastapi import FastAPI

# from pydantic import BaseModel, EmailStr

# app = FastAPI()


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None


# # Don't do this in production
# @app.post("/users/", response_model=UserIn)
# async def create_user(user: UserIn):
#     return user

# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()


# class UserIn(BaseModel):

#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None


# class UserOut(BaseModel):

#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None


# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user

# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None


# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


# from typing import List, Optional

# from fastapi import FastAPI

# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: float = 10.5
#     tags: List[str] = []


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }


# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# async def read_item(item_id: str):
#     return items[item_id]


# from typing import Optional

# from fastapi import FastAPI

# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: float = 10.5


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
#     "baz": {
#         "name": "Baz",
#         "description": "There goes my baz",
#         "price": 50.2,
#         "tax": 10.5,
#     },
# }


# @app.get(
#     "/items/{item_id}",
#     response_model=Item,
#     response_model_include={"name", "description"},
# )
# async def read_item_name(item_id: str):
#     return items[item_id]


# @app.get("/items/{item_id}/public", repsonse_model=Item, response_model_exclude={"tax"})
# async def read_item_public_data(item_id: str):
#     return items[item_id]

# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: float = 10.5


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
#     "baz": {
#         "name": "Baz",
#         "description": "There goes my baz",
#         "price": 50.2,
#         "tax": 10.5,
#     },
# }


# @app.get(
#     "/items/{item_id}/name",
#     response_model=Item,
#     response_model_include=["name", "description"],
# )
# async def read_item_name(item_id: str):
#     return items[item_id]


# @app.get("/items/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
# async def read_item_public_data(item_id: str):
#     return items[item_id]


# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None


# class UserOut(BaseModel):
#     username: str
#     enail: EmailStr
#     full_name: Optional[str] = None


# class UserInDB(BaseModel):
#     username: str
#     hashed_password: str
#     email: EmailStr
#     full_name: Optional[str] = None


# def fake_password_hasher(raw_password: str):
#     return "supersecret" + raw_password


# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#     print("User saved! ..not really")
#     return user_in_db


# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved

# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()


# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str]


# class UserIn(UserBase):
#     password: str


# class UserOut(UserBase):
#     pass


# class UserInDB(UserBase):
#     hashed_password: str


# def fake_password_hasher(raw_password: str):
#     return "supersecret" + raw_password


# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(*+user_in.dict(), hashed_password=hashed_password)
#     print("User saved! ..not really")
#     return user_in_db


# @app.post("/user/, response_model=UserOut")
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved

# from typing import Union
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class BaseItem(BaseModel):
#     description: str
#     type: str


# class CarItem(BaseItem):
#     type = "car"


# class PlaneItem(BaseItem):
#     type = "plane"
#     size: int


# items = {
#     "item1": {"description": "All my friends drive a low rider", "type": "car"},
#     "item2": {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }


# @app.get("/items/{item_id", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: str):
#     return items[item_id]

# from typing import List


# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str


# items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"},
# ]


# @app.get("/items/", response_model=List[Item])
# async def read_items():
#     return items


from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}
