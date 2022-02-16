from typing import Optional

from pydantic import BaseModel


class PostsModel(BaseModel):
    integration_id: Optional[int]
    title: Optional[str]
    body: Optional[str]
    user_id: Optional[int]
