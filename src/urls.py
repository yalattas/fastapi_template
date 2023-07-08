from fastapi import APIRouter, Response

router = APIRouter(
    tags=["default"],
    responses={404: {"description": "Not found"}},
)

@router.get("/health/")
def test(response: Response):
    response.status_code = 200
    return {"health": "ok"}