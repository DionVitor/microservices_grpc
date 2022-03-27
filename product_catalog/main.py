from typing import Dict

from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from dotenv import load_dotenv


from controllers.product_catolog_service import product_catalog_router


app = FastAPI()
app.include_router(product_catalog_router)


@app.middleware("http")
async def before_request(request: Request, call_next):
    load_dotenv()

    response = await call_next(request)
    return response


def customize_openapi(openapi_schema: Dict):
    pass


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Trampolim B2B - User Recruiter",
        version="1.0.0",
        description="Endpoint documentation to user recruiter microservice.",
        routes=app.routes,
    )

    customize_openapi(openapi_schema)
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
