from fastapi import APIRouter, File, UploadFile
from typing import Optional
import logging

router = APIRouter()


@router.post("/upload")
async def upload_file(file: Optional[UploadFile] = File(None)):
    if file is None:
        logging.info("No file uploaded")
        return {"filename": ""}

    logging.info(f"File uploaded: {file.filename}")
    file_location = f"static/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    return {"filename": file.filename}
