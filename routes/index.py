from fastapi import APIRouter

router = APIRouter(prefix="", tags=["index"])


@router.get('/')
async def index():
    return {"message": "Website is working"}
