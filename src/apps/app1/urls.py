from fastapi import APIRouter, Response
from conf.settings import settings
from apps.app1.models import User
from conf.database import SessionLocal

router = APIRouter(
    prefix=f"/api/{settings.API_V1_STR}/app1",
    tags=["app1"],
    responses={404: {"description": "Not found"}},
)

@router.get("/test/")
def test(response: Response):
    response.status_code = 200

    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    for user in users:
        print(user.first_name)
    return {"health": 1/2}