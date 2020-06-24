from pydantic import BaseModel


class ExpressionRequest(BaseModel):
    expression: str