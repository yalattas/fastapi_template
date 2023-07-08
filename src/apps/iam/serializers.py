# from pydantic import BaseModel, HttpUrl


# class KeycloakSerializer(BaseModel):
#     grant_type: str
#     code: str
#     redirect: HttpUrl

class KeycloakCustomSerializer:
    grant_type: str
    code: str
    redirect_uri: str
    def __init__(self, payload):
        self.grant_type = payload['grant_type'] or None
        self.code = payload['code']
        self.redirect_uri = payload['redirect_uri'] or None
    def __str__(self) -> str:
        return self.grant_type+'    '+ self.code+'   '+self.redirect_uri