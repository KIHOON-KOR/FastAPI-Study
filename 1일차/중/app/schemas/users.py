# app/schemas/users.py

from enum import Enum

from pydantic import BaseModel, Field


class GenderEnum(str, Enum):
    male = "male"
    female = "female"


class UserCreateRequest(BaseModel):
    username: str
    age: int
    gender: GenderEnum


class UserUpdateRequest(BaseModel):
    username: str | None = None
    age: int | None = None
    # username 는 str이거나 None 일 수 있다. =None : 기본깂은 None


class UserSearchParams(BaseModel):
    # Path() : 경로 매개변수, BaseModel안에서 사용 불가
    # @app.get() 같은 라우터 함수 매개변수에서만 사용해야 함
    # BaseModel 안에서는 Pydantic의 Field()를 써야 함
    model_config = {"extra": "forbid"}
    # 정의되지 않은 내용 추가시 오류를 발생
    username: str | None = None
    age: int | None = Field(default=None, gt=0)
    gender: GenderEnum | None = None
