from fastapi import APIRouter, HTTPException
from src.lib.managedb import ManageDB
from pydantic import BaseModel
from uuid import uuid4

router_multimedia = APIRouter()
manage = ManageDB()

class Media(BaseModel):
    id : str = str(uuid4()) 
    video: str 
    subtitle: str
    image_1: str
    image_2: str
    image_3: str
    audio_1: str
    audio_2: str
    audio_3: str
    pdf: str

@router_multimedia.get("/")
def root():
    return {"Multimedia"} 

@router_multimedia.get("/multimedia")
def get_multimedia():
    return manage.read_multimedia()

@router_multimedia.get("/multimedia/{media_id}")
def get_single_multimedia(media_id: str):
    multimedia: list = manage.read_multimedia()
    for media in multimedia:
        if str(media["id"]) == media_id:
            return media
    raise HTTPException(status_code=404, detail="Media not found")

@router_multimedia.post("/multimedia")
def create_color(media: Media):
    multimedia: list = manage.read_multimedia()
    multimedia.append(media.dict())
    manage.write_multimedia(multimedia)
    return {"Success":True,
            "Message":"Media added successfully",
            "Value":media.dict()
            }

@router_multimedia.put("/multimedia/{media_id}")
def update_color(media_id: str, media: Media):
    multimedia: list = manage.read_multimedia()
    for index, col in enumerate(multimedia):
        if col["id"] == media_id:
            multimedia[index] = media.dict()
            manage.write_multimedia(multimedia)
            return {"Success":True,
                    "Message":"Media updated successfully",
                    "Value":media.dict()
                    }
    raise HTTPException(status_code=404, detail="Media not found")

@router_multimedia.delete("/multimedia/{media_id}")
def delete_color(media_id: str):
    multimedia: list = manage.read_multimedia()
    for index, col in enumerate(multimedia):
        if col["id"] == media_id:
            multimedia.pop(index)
            manage.write_multimedia(multimedia)
            return {"Success":True,
                    "Message":"Media deleted successfully",
                    "Value":media_id
                    }
    raise HTTPException(status_code=404, detail="Media not found")