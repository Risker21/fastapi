from enum import Enum

from fastapi import APIRouter, Path

ch01 = APIRouter(prefix="/ch01",tags=["路由传参"])

@ch01.get("/emp",summary="查询所有员工",response_description="返回员工的详细信息")
def find_emp():
    print("查询所有员工")
    return {"message": "OK"}

@ch01.get("/emp/{emp_id}",summary="查询单个员工",response_description="返回员工的详细信息")
def find_emp(emp_id: int):
    print(f'查询的员工ID:{emp_id}')
    return {"message": "OK"}

@ch01.delete("/emp{emp_id}",summary="删除员工",
         response_description="返回员工的详细信息")
def delete_emp(emp_id: int):
    print(f'删除的员工ID:{emp_id}')
    return {"message": "OK"}


class EmpName(Enum):
    JACK = "杰克"
    Momo = "莫莫"
    CC = "CC"


@ch01.put("/emp{emp_name}",summary="修改员工",response_description="返回员工的详细信息")
def update_emp(emp_name: EmpName = Path(description="员工姓名只能是杰克、莫莫、CC")):  # example参数是给接口文档中提供的示例值
    print(f'传入的参数:{emp_name.name}')
    print(f'传入的参数:{emp_name.value}')
    return {"message": "OK"}