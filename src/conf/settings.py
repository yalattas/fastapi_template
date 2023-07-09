# import motor.motor_asyncio
import os
import distutils.util
import boto3
import logging
from pydantic_settings import  BaseSettings
from keycloak import KeycloakOpenID

class Settings(BaseSettings):
    PROJECT_NAME: str = os.environ.get('PROJECT_NAME')
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    API_V1_STR: str = os.environ.get('API_V1_STR')
    APP_PORT: int = os.environ.get('APP_PORT')
    ENVIRONMENT: str =  os.environ.get('ENVIRONMENT', default='local')

    # database connection
    DATABASE_URL: str = os.environ.get('DATABASE_URL')

    # application performance config
    IS_SENTRY_ENABLED: bool = distutils.util.strtobool(os.environ.get('IS_SENTRY_ENABLED'))
    SENTRY_DSN: str = os.environ.get('SENTRY_DSN')

    LOGGER: object = logging.getLogger("uvicorn.access")
    LOGGER_FORMAT: str = "{asctime} - {levelname} - {module}: {message}"
    LOGGER_STYLE: str = "{" # Style must be one of: %,{,$

    KEYCLOAK_HOST: str = os.environ.get('KEYCLOAK_HOST')
    KEYCLOAK_CLIENT_ID: str = os.environ.get('KEYCLOAK_CLIENT_ID')
    KEYCLOAK_REALM_NAME: str = os.environ.get('KEYCLOAK_REALM_NAME')
    KEYCLOAK_SECRET_KEY: str = os.environ.get('KEYCLOAK_SECRET_KEY')

    KEYCLOAK_CLIENT: KeycloakOpenID = KeycloakOpenID(server_url=KEYCLOAK_HOST,
                                    client_id=KEYCLOAK_CLIENT_ID,
                                    realm_name=KEYCLOAK_REALM_NAME,
                                    client_secret_key=KEYCLOAK_SECRET_KEY)

    # Get WellKnow
    config_well_known: object = KEYCLOAK_CLIENT.well_known()
    class Config:
        case_sensitive = True


settings = Settings()