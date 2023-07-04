from conf.settings import settings

class OpenAPI:
    title: str = settings.PROJECT_NAME
    summary: str = "Deadpool's favorite app. Nuff said."
    description: str = """
    ChimichangApp API helps you do awesome stuff. 🚀

    ## Items

    You can **read items**.

    ## Users

    You will be able to:

    * **Create users** (_not implemented_).
    * **Read users** (_not implemented_).
    """
    version: str = "latest"
    openapi_url: str = f"/api/{settings.API_V1_STR}/openapi.json"
    docs_url: str = f"/api/{settings.API_V1_STR}/docs" # or None to disable
    redoc_url: str = f"/api/{settings.API_V1_STR}/redoc" # or None to disable
    openapi_tags: list = [{
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    }]
    terms_of_service: str = "http://example.com/terms/"
    contact: dict = {
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    }
    license_info: dict = {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }