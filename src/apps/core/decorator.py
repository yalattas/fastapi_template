from functools import wraps
from apps.core.authentication import KeyCloakIAM
from apps.core.utilities import Utility
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def is_authenticated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_type, token = Utility.get_token(kwargs['request'])
        authenticated, id = KeyCloakIAM(auth_type, token).authenticate()
        kwargs['request'].user_id = id
        return func(*args, **kwargs)
    return wrapper