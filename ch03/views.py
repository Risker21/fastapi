from datetime import date

from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator

ch03 = APIRouter(prefix="/ch03", tags=["请求体传参"])


class Addr(BaseModel):
    province: str = Field(description="省份")
    city: str = Field(description="城市")
    district: str = Field(description="区县")


class Emp(BaseModel):
    name: str = Field(description="员工的姓名")
    age: int = Field(description="员工的年龄", ge=18, lt=60)
    birth: date = Field(description="员工的出生日期", default=None)
    addr: Addr = Field(description="员工的地址", default=None)

    @field_validator('name')  # 自定义一个复杂的校验器，校验员工姓名是否满足特定的规则
    def validate_name(cls, value):
        import re
        result = re.match(r'^[a-zA-Z_]\w{4,9}$', value)
        assert not result is None
        return value


@ch03.post("/emp", summary="添加员工", description="传入员工信息")
def find_all_emp(emp: Emp):
    print(f'所有员工信息：{emp}')
    return {"message": "OK"}

