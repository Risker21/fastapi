from fastapi import APIRouter, Query

ch02 = APIRouter(prefix="/ch02", tags=["URL传参"])


@ch02.get("/emp", summary="搜索员工")
def find_all_emp(id: int = Query(default=None, description="员工ID"),
                 name: str = Query(default=None, description="员工姓名")):
    print(f"搜索员工信息：id={id},name={name}")
    return {"message": "OK"}
