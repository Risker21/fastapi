from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from ch03.views import ch03
from shopping_app.views.cart_views import shop
from ch01.views.views import ch01
from ch02.views.views import ch02


# 变量名
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
# 加载所有的分路由
app.include_router(shop)
app.include_router(ch01)
app.include_router(ch02)
app.include_router(ch03)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/test",
          tags=["给接口分组的标签"],summary="测试接口",
          description="接口描述信息",response_description="响应数据的详细信息")
def test():
    print("执行了test函数")
    return {"message": "OK"}


# 运行服务器
# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app)
