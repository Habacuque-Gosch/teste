from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/router1-router-teste")


# class ContaPagarResponse(BaseModel)
#     pass




@router.get("/")
def router1_test():
        
    return [
        {"contas1": "contas123"},
        {"contas1": "contas123"},
    ]