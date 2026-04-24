from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ExampleRequest(BaseModel):
    message: str


class ExampleResponse(BaseModel):
    reply: str


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/example", response_model=ExampleResponse)
def example_endpoint(body: ExampleRequest):
    # TODO: add your logic here
    return ExampleResponse(reply=f"You said: {body.message}")
