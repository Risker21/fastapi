from fastapi import APIRouter
# 创建一个分路由
shop = APIRouter(prefix="/shop", tags=["购物车相关接口"])

@shop.post("/catall",summary="查询接口", description="购物车相关接口的描述信息",response_description="响应数据的详细信息")
def find_cat():
    print("查询购物车")
    return {"message": "OK"}

@shop.post("/add",summary="添加接口", description="购物车相关接口的描述信息",response_description="响应数据的详细信息")
def find_cat():
    print("添加购物车")
    return {"message": "OK"}