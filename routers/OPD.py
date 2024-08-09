from fastapi import APIRouter

router = APIRouter()


@router.get("/OPD")
def OPD():
    return {"message": "Welcome to the Out-Patient Department!"}


@router.get("/OPD/{id}")
def read_OPD(id: int):
    return {"item_id": id}


@router.post("/OPD")
def create_OPD():
    return {"message": "OPD has been created!"}


@router.put("/OPD/{id}")
def update_OPD(id: int):
    return {"message": "OPD has been updated!"}


@router.delete("/OPD/{id}")
def delete_OPD(id: int):
    return {"message": "OPD has been deleted!"}
