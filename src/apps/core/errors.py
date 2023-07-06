from enum import Enum
from conf.settings import settings
from fastapi import HTTPException



class Error(Enum):
    INVALID_TOKEN = {'status_code': 403, 'detail': ('Invalid token')}
    MISSING_TOKEN = {'status_code': 400, 'detail': ('Missing token')}

class APIError:
    def __init__(self, error: Error, extra=None):
        self.error = error
        self.extra = extra or None
        error_detail = error.value
        if self.extra:
            # Extra values can be used in foramtting a string that contains {}
            if isinstance(self.extra, list):
                error_detail['detail'] = error_detail['detail'].format(*extra)
        try:
            logger = settings.LOGGER
            logger.warning(error.value)
        except BaseException:
            pass
        raise HTTPException(**error_detail)
