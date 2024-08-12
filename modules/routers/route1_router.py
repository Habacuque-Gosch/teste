from fastapi import APIRouter


router = APIRouter(prefix="/router1-router")


@router.get("/")
def router1_test():
    return [
        {"contas1": "contas123"},
        {"contas1": "contas123"},
    ]