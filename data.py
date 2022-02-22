# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2,
#             }
#         }


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()


# class Item(BaseModel):
#     name: str = Field(..., example="Foo")
#     description: Optional[str] = Field(None, example="A very nice Item")
#     price: float = Field(..., example=35.4)
#     tax: Optional[float] = Field(None, example=3.2)


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# from typing import Optional

# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Item = Body(
#         ...,
#         examples={
#             "normal": {
# "summary": "A normal example",
# "description": "A **normal** item works correctly.",
#                 "value": {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 },
#             },
#             "converted": {
#                 "summary": "An example with converted data",
#                 "description": "FastAPI can convert price strings to actual 'numbers' automatically",
#                 "value": {"name": "Bar", "price": "35.4"},
#             },
#             "invalid": {
#                 "summary": "Invalid data is rejected with an error",
#                 "value": {"name": "Baz", "price": "thirty five point four"},
#             },
#         },
#     ),
# ):
#     results = {"item_id": item_id, "item": item}
#     return results

# from datetime import datetime, time, timedelta
# from typing import Optional

# from uuid import UUID

# from fastapi import Body, FastAPI

# app = FastAPI()


# @app.put("/items/{item_id}")
# async def read_items(
#     item_id: UUID,
#     start_datetime: Optional[datetime] = Body(None),
#     end_datetime: Optional[datetime] = Body(None),
#     repeat_at: Optional[time] = Body(None),
#     process_after: Optional[timedelta] = Body(None),
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#     }

# from typing import Optional

# from fastapi import Cookie, FastAPI

# app = FastAPI()


# @app.get("/items/")
# async def read_items(ads_id: Optional[str] = Cookie(None)):
#     return {"ads_id": ads_id}

# from typing import Optional

# from fastapi import FastAPI, Header

# app = FastAPI()


# @app.get("/items/")
# async def read_items(user_agent: Optional[str] = Header(None)):
#     return {"User-Agent": user_agent}

from typing import List, Optional
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Optional[List[str]] = Header(None)):
    return {"X_token values": x_token}
