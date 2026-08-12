from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., max_length=500)

class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., max_length=500)
    completed: bool

class TaskPatch(BaseModel):
    title: str | None = Field(default=None,min_length=3, max_length=100)
    description: str | None = Field(default=None,max_length=500)
    completed: bool | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    user_id: int