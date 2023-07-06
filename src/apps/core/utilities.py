
class Utility:
    @staticmethod
    def get_token(request) -> tuple:
        auth = request.headers.get('AUTHORIZATION')
        if auth is None:
            return None, ''
        auth_type, token = auth.split()
        if token is None or token == '':
                return None, ''
        return auth_type, token