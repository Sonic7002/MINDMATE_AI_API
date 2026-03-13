from fastapi import APIRouter
from scalar_fastapi import get_scalar_api_reference
from main import app

router = APIRouter(prefix="/scalar_docs", tags=["scalar"])

@router.get("/")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )