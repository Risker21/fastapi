import enum
from decimal import Decimal
from sqlalchemy import String, DECIMAL, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from ch04.db_main import Base, engine
class SexValue(enum.Enum):
    """通过枚举，给一些属性（字段）设置一些固定的值"""
    MALE = "男"
    FEMALE = "女"

class Employee(Base):
    """员工的模型类"""
    __tablename__ = 't_emp'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    gender: Mapped[SexValue]
    # DECIMAL(10,2)表示总共10位数字，其中小数部分有2位，整数部分有8位
    sal: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=False, comment="员工的工资")
    bonus: Mapped[int] = mapped_column(default=0, nullable=False, comment="员工的奖金")
    is_leave: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment="员工是否离职")
    
    
if __name__ == '__main__':
    # 所有的表都重新创建（删除）表
    Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)

    # 单独把某个表创建（删除）表
    # Employee.__table__.create(engine)
    # Employee.__table__.drop(engine)

