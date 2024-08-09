from fastapi import APIRouter

router = APIRouter()


@router.get("/shop")
def all_shop():
    return {"message": "Welcome to the shop!"}


@router.get("/shop/{id}")
def read_shop(id: int):
    return {"item_id": id}


@router.post("/shop")
def create_shop():
    return {"message": "Shop has been created!"}


@router.put("/shop/{id}")
def update_shop(id: int):
    return {"message": "Shop has been updated!"}


@router.delete("/shop/{id}")
def delete_shop(id: int):
    return {"message": "Shop has been deleted!"}
