from fastapi import APIRouter

router = APIRouter(
    prefix = "/items"
)

@router.get("/")
def products_main():
    return (
        {"hello": "world"}
    )