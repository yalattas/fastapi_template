from fastapi import APIRouter, Request
from conf.settings import settings
from apps.app1.models import User
from conf.database import SessionLocal
from apps.core.decorator import is_authenticated

router = APIRouter(
    prefix=f"/api/{settings.API_V1_STR}/app1",
    tags=["app1"],
    responses={404: {"description": "Not found"}},
)
class FirstClass:
    @router.get("/test/")
    @is_authenticated
    def test(request: Request):         # parameter must be named request for middleware to work
        request.status_code = 200

        print(request.user_id)
        session = SessionLocal()
        users = session.query(User).all()
        session.close()
        for user in users:
            print(user.first_name)
        return {"health": request.user_id}
