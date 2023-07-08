from fastapi import Request
from conf.settings import settings
from .services import AccountService
from .serializers import KeycloakCustomSerializer

class UserView:
    def UserAuth(request: Request) -> str:
        try:
            user_id = request.user_id
        except AttributeError as e:
            user_id = None
        client = "https://oauth.pstmn.io/v1/callback"
        auth_url = settings.KEYCLOAK_CLIENT.auth_url(
            # must whitelist front-end uri
            redirect_uri=client,
            scope="openid",
            state=AccountService.generate_session_state(client, user_id)
        )
        return auth_url
    def Authenticate(request: Request, body: KeycloakCustomSerializer) -> str:
        client = "https://oauth.pstmn.io/v1/callback"
        access_response = settings.KEYCLOAK_CLIENT.token(
            grant_type='authorization_code',
            code=body.code,
            redirect_uri=client
        )
        # token_type = access_response['token_type'] # should be Bearer
        access_token = access_response['access_token']
        return access_token