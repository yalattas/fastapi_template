import uuid
from . import models

class AccountService:
    @staticmethod
    def generate_session_state(client: str, session_id: str = None, user_id: str = None) -> str:
        if session_id is None:
            session_id = str(uuid.uuid4())
        print('------------ session id:  ', session_id)
        models.SessionLog(session_id=session_id, client_id=client, user_id=user_id).save()
        return session_id
    @staticmethod
    def get_or_create_user(id: str) -> models.User:
        user = models.User(id=id)
        user = user.get_or_create_user(id=id)
        if not user:
            user = models.User(id=id)
            user.save()
        return user