# from fastapi import BackgroundTasks, FastAPI

# app = FastAPI()


# def write_notifications(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         content = f"notification for {email}: message"
#         email_file.write(content)


# @app.post("/send-notification/{email}")
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notifications, email, message="some notification")
#     return {"message": "Notification sent in the background"}

from os import write
from typing import Optional

from fastapi import BackgroundTasks, FastAPI
from fastapi.param_functions import Depends

app = FastAPI()


def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notification/{email}")
async def send_notification(
    email: str, background_tasks: BackgroundTasks, q: str = Depends(get_query)
):
    message = f"message to {email}"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}
