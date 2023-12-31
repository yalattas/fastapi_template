import uvicorn
import sentry_sdk
from fastapi import FastAPI
# from telegram import urls as telegram_app_url
from openapi import OpenAPI
import urls as main_url
from apps.app1 import urls as app1_router
from apps.app2 import urls as app2_router
from conf.settings import settings

if settings.IS_SENTRY_ENABLED:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production,
        traces_sample_rate=1.0,
        environment=settings.ENVIRONMENT
    )

app = FastAPI(
    title=OpenAPI.title,
    summary=OpenAPI.summary,
    description=OpenAPI.description,
    version=OpenAPI.version,
    openapi_url=OpenAPI.openapi_url,
    docs_url=OpenAPI.docs_url, # or None to disable
    redoc_url=OpenAPI.redoc_url, # or None to disable
    openapi_tags=OpenAPI.openapi_tags,
    terms_of_service=OpenAPI.terms_of_service,
    contact=OpenAPI.contact,
    license_info=OpenAPI.license_info,
)

app.include_router(main_url.router)
app.include_router(app1_router.router)
app.include_router(app2_router.router)
# app.mount('/app1', app1_router.app)
# app.include_router(telegram_app_url.router)

# https://docs.python.org/3/library/logging.html
# logging.getLogger("uvicorn.access").disabled = False
# logging.getLogger("uvicorn.error").disabled = False

@app.on_event("startup")
async def startup_event():
    logger = settings.LOGGER
    console_formatter = uvicorn.logging.ColourizedFormatter(settings.LOGGER_FORMAT,style=settings.LOGGER_STYLE, use_colors=True)
    logger.handlers[0].setFormatter(console_formatter)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=settings.APP_PORT)
