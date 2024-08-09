from fastapi import APIRouter

router = APIRouter()


@router.get("/IPD")
def IPD():
    return {"message": "Welcome to the In-Patient Department!"}


@router.get("/IPD/{id}")
def read_IPD(id: int):
    return {"item_id": id}


@router.post("/IPD")
def create_IPD():
    return {"message": "IPD has been created!"}


@router.put("/IPD/{id}")
def update_IPD(id: int):
    return {"message": "IPD has been updated!"}


@router.delete("/IPD/{id}")
def delete_IPD(id: int):
    return {"message": "IPD has been deleted!"}
