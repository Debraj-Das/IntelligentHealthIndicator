from fastapi import APIRouter

router = APIRouter()


@router.get("/pathology")
def pathology():
    return {"message": "Welcome to the Pathology Test Results!"}


@router.get("/pathology/{id}")
def pathology_id(id: int):
    return {"item_id": id}


@router.post("/pathology")
def create_pathology():
    return {"message": "Pathology Test Results has been created!"}


@router.put("/pathology/{id}")
def update_pathology(id: int):
    return {"message": "Pathology Test Results has been updated!"}


@router.delete("/pathology/{id}")
def delete_pathology(id: int):
    return {"message": "Pathology Test Results has been deleted!"}
