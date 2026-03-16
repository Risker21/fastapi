from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# 创建数据库引擎，echo=True表示输出SQL语句，future=True表示使用SQLAlchemy 2.0的API
engine = create_engine("mysql+pymysql://root:Wordl9543@localhost:3306/fastapi_db", echo=True, future=True, pool_size=10)


# 定义一个模型类的基类
class Base(DeclarativeBase):
    pass
# 所有的模型类，都有的属性和字段映射
    create_time: Mapped[datetime] = mapped_column(DateTime,insert_default=func.now(),comment="记录创建时间")
    update_time: Mapped[datetime] = mapped_column(DateTime,insert_default=func.now(),onupdate=func.now(),comment="记录最后一次修改时间")



