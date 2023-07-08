from fastapi import Request
import urllib.parse

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

    @staticmethod
    def extract_body_from_request(request: Request) -> tuple:
        body = request.body()
        return request, body

    @staticmethod
    def parse_byte_to_dict(data: b'str') -> dict:
        decoded_data = data.decode('utf-8')
        parsed_data = urllib.parse.parse_qs(decoded_data)
        parsed_data = {k: v[0] for k, v in parsed_data.items()}
        return parsed_data