# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()


# @app.post("/files/")
# async def create_file(file: bytes = File(...)):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile = File(...)):
#     return {"filename": file.filename}

# from typing import List

# from fastapi import FastAPI, File, UploadFile

# from fastapi.responses import HTMLResponse

# app = FastAPI()


# @app.post("/files/")
# async def create_file(files: List[bytes] = File(...)):
#     return {"file_sizes": [len(file) for file in files]}


# @app.post("/uploadfiles/")
# async def create_upload_files(files: List[UploadFile] = File(...)):
#     return {"filenames": [file.filename for file in files]}


# @app.get("/")
# async def main():
#     content = """
# <body>
# <from action="/files/" enctype="multipart/form-data" method="post">
# <input name = "files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
# """
#     return HTMLResponse(content=content)

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(
    file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
