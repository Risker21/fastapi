from datetime import date
from fastapi import APIRouter, Body
from pydantic import BaseModel, Field, field_validator
from pygments.lexer import default

ch03 = APIRouter(prefix="/ch03", tags=["请求体传参"])

# 定义一个地址类
class Addr(BaseModel):
    province: str = Field(description="省份")
    city: str = Field(description="城市")
    district: str = Field(description="区县")

# 定义一个员工类（BaseModel: 定义一个数据模型类，用于表示请求体中的数据）
class Emp(BaseModel):
    name: str = Field(description="员工的姓名")
    age: int = Field(description="员工的年龄", ge=18, lt=60)
    birth: date = Field(description="员工的出生日期", default=None)
    addr: Addr = Field(description="员工的地址", default=None)

    # 自定义一个复杂的校验器，校验员工姓名是否满足特定的规则
    @field_validator('name')
    def validate_name(cls, value):
        import re
        result = re.match(r'^[a-zA-Z_]\w{4,9}$', value)
        # 断言：如果result为None，说明校验失败，抛出异常；如果result不为None，说明校验成功，继续执行后续代码
        assert not result is None
        return value

@ch03.post("/emp", summary="添加员工", description="传入员工信息")
def find_all_emp(emp: Emp):
    print(f'所有员工信息：{emp}')
    return {"message": "OK"}



'''
请求体传参（json格式数据）
{
"name": "zhangsan",}
  "age": 20,
'''
@ch03.post("/test",summary="测试员工信息", description="测试接口")
def test(name:str  = Body(default=None,description="测试的名字"),
         age:int = Body(default=18,description="测试的年龄")):
    print(f'测试人信息 = {name}：{age}')
    return {"message": "OK"}
