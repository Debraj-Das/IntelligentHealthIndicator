from fastapi import APIRouter

router = APIRouter()


@router.get("/medicine")
def medicine():
    return {"message": "Welcome to the Medicine Prescribed!"}


@router.get("/medicine/{id}")
def medicine_id(id: int):
    return {"item_id": id}


@router.post("/medicine")
def create_medicine():
    return {"message": "Medicine Prescribed has been created!"}


@router.put("/medicine/{id}")
def update_medicine(id: int):
    return {"message": "Medicine Prescribed has been updated!"}


@router.delete("/medicine/{id}")
def delete_medicine(id: int):
    return {"message": "Medicine Prescribed has been deleted!"}
