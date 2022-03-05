"""Generic Pydantic models that are used in different contexts."""

from pydantic import BaseModel


class LimitOffset(BaseModel):
    limit: int
    offset: int
