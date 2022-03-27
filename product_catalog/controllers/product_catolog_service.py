from fastapi.routing import APIRouter


product_catalog_router = APIRouter(prefix="/product_catalog", tags=["Product Catalog"])


@product_catalog_router.get("")
def get_product_catalog():
    return [
        {
            "name": "Product one",
            "price": 9.99,
            "stock": 10
        },
        {
            "name": "Product two",
            "price": 99.99,
            "stock": 2
        }
    ]
