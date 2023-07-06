from conf.settings import settings
from apps.core.errors import Error, APIError
from keycloak.exceptions import KeycloakAuthenticationError, KeycloakGetError

class KeyCloakIAM():
    token: str
    auth_type: str

    def __init__(self, auth_type, token) -> None:
        self.auth_type = auth_type
        self.token = token
    def __str__(self) -> str:
        return self.auth_type + ' ' + self.token

    def authenticate(self) -> tuple:
        authenticated = False
        id = None
        try:
            user_details = settings.KEYCLOAK_CLIENT.userinfo(self.token)
            id = user_details.get('sub')
            authenticated = True
        except KeycloakAuthenticationError as e:
            raise APIError(Error.INVALID_TOKEN)
        except KeycloakGetError as e:
            raise APIError(Error.MISSING_TOKEN)
        return authenticated, id
