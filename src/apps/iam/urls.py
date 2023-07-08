from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, Response
from conf.settings import settings
from apps.core.utilities import Utility
from .views import UserView
from .serializers import KeycloakCustomSerializer
import json

router = APIRouter(
    prefix=f"/api/{settings.API_V1_STR}/iam",
    tags=["iam"],
    responses={404: {"description": "Not found"}},
)
class iam:
    @router.get("/auth/")
    def auth(request: Request):         # parameter must be named request for middleware to work
        request.status_code = 200
        auth_url = UserView.UserAuth(request)
        return RedirectResponse(auth_url, status_code=303)

    @router.post("/auth/")
    async def login(request: Request):
        """
        grant_type: str
        code: str
        redirect_uri: str
        """
        req, body = Utility.extract_body_from_request(request)
        body = await body
        body = Utility.parse_byte_to_dict(body)
        body = KeycloakCustomSerializer(payload=body)
        access_token, refresh_token = UserView.Authenticate(request, body)
        response = {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }
        return Response(content=json.dumps(response),  status_code=200, media_type="application/json")
