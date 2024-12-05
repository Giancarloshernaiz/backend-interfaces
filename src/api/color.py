from fastapi import APIRouter, HTTPException
from src.lib.managedb import ManageDB
from pydantic import BaseModel
from uuid import uuid4

router_colores = APIRouter()
manage = ManageDB()

class Color(BaseModel):
    id : str = str(uuid4()) 
    text: str 
    background: str
    button_text: str
    button_background: str
    font_size: str
    font_title: str
    font_par: str

@router_colores.get("/")
def root():
    return {"Colors"} 

@router_colores.get("/colors")
def get_colors():
    return manage.read_colors()

@router_colores.get("/colors/{color_id}")
def get_single_colors(color_id: str):
    colors: list = manage.read_colors()
    for color in colors:
        if str(color["id"]) == color_id:
            return color
    raise HTTPException(status_code=404, detail="Color not found")

@router_colores.post("/colors")
def create_color(color: Color):
    colors: list = manage.read_colors()
    colors.append(color.dict())
    manage.write_colors(colors)
    return {"Success":True,
            "Message":"Color added successfully",
            "Value":color.dict()
            }

@router_colores.put("/colors/{color_id}")
def update_color(color_id: str, color: Color):
    colors: list = manage.read_colors()
    for index, col in enumerate(colors):
        if col["id"] == color_id:
            colors[index] = color.dict()
            manage.write_colors(colors)
            return {"Success":True,
                    "Message":"Color updated successfully",
                    "Value":color.dict()
                    }
    raise HTTPException(status_code=404, detail="Color not found")

@router_colores.delete("/colors/{color_id}")
def delete_color(color_id: str):
    colors: list = manage.read_colors()
    for index, col in enumerate(colors):
        if col["id"] == color_id:
            colors.pop(index)
            manage.write_colors(colors)
            return {"Success":True,
                    "Message":"Color deleted successfully",
                    "Value":color_id
                    }
    raise HTTPException(status_code=404, detail="Color not found")