import uvicorn
from fastapi import FastAPI
from openapi import OpenAPI
from conf.settings import settings


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


@app.get("/te")
def read_main():
    return {"message": "Hello World from main app"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=settings.APP_PORT)
