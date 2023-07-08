from fastapi import Request
from conf.settings import settings
from apps.core.authentication import KeyCloakIAM
from .services import AccountService
from .serializers import KeycloakCustomSerializer

class UserView:
    def UserAuth(request: Request) -> str:
        client = "https://oauth.pstmn.io/v1/callback"
        auth_url = settings.KEYCLOAK_CLIENT.auth_url(
            # must whitelist front-end uri
            redirect_uri=client,
            scope="openid",
            state=AccountService.generate_session_state(client)
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
        token_type = access_response['token_type']
        access_token = access_response['access_token']
        refresh_token = access_response['refresh_token']
        session_state = access_response['session_state']
        authenticated, user_id = KeyCloakIAM(token_type, access_token).authenticate()
        user = AccountService.get_or_create_user(id=user_id)
        print('session state ---------------------------------- ', session_state)
        session_state = AccountService.generate_session_state(client=client,  session_id=session_state, user_id=user_id)
        return access_token, refresh_token