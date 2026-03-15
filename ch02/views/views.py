from typing import List

from fastapi import APIRouter, Query

ch02 = APIRouter(prefix="/ch02", tags=["URL传参"])


@ch02.get("/emp", summary="搜索员工")
def find_all_emp(id: int = Query(default=None, description="员工ID"),
                 name: str = Query(default=None, description="员工姓名")):
    print(f"搜索员工信息：id={id},name={name}")
    return {"message": "OK"}


@ch02.delete("/emp", summary="批量删除员工", description="传入多个员工ID，批量删除员工")
def delete_emp(emp_ids: List[int] = Query(default=[], description="多个员工id"), ):
    print(f"批量删除员工：emp_ids={emp_ids}")
    return {"message": "OK"}


# 字符串长度的校验
# @ch02.post("/emp", summary="添加员工",description="传入员工名字")
# def create_emp(name: str = Query(description="员工姓名",max_length=10,min_length=5)):
#     print(f"添加员工：name={name}")
#     return {"message": "OK"}


# 正则表达式的校验
'''
1.用户名只能包含数字，字母，下划线
2.不能以数字开头
3.长度在5-10之间
ge 大于等于
gt 大于
le 小于等于
lt 小于
'''


@ch02.post("/emp", summary="添加员工", description="传入员工名字")
def create_emp(name: str = Query(description="员工姓名", regex=r"^[a-zA-Z_]\w{4,9}$"),
               age: int = Query(description="年龄", ge=18, lt=60)):
    print(f"添加员工：name={name},age={age}")
    return {"message": "OK"}
