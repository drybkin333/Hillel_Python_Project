from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=12)
    email: str
    phone: str = Field(..., min_length=9, max_length=13)

class UserPatch(BaseModel):
    password: str | None = Field(default=None, min_length=6, max_length=12)
    email: str | None = Field(default=None, min_length=6, max_length=13)
    phone: str | None = Field(default=None, min_length=9, max_length=13)

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    phone: str