# import motor.motor_asyncio
import os
import distutils.util
import boto3
from pydantic import  BaseSettings
import logging

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

    LOGGER = logging.getLogger("uvicorn.access")
    LOGGER_FORMAT: str = "{asctime} - {levelname} - {module}: {message}"
    LOGGER_STYLE: str = "{" # Style must be one of: %,{,$

    class Config:
        case_sensitive = True


settings = Settings()