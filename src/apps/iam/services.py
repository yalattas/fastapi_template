import uuid
from . import models

class AccountService:
    @staticmethod
    def generate_session_state(client: str, user_id: str = None) -> str:
        session_id = str(uuid.uuid4())
        models.SessionLog(session_id=session_id, client_id=client, user_id=user_id).save()
        return session_id