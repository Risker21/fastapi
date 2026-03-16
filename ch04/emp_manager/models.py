import enum
from datetime import date
from decimal import Decimal
from sqlalchemy import String, DECIMAL, Boolean, func, insert, select, text
from sqlalchemy.orm import Mapped, mapped_column, Session, sessionmaker
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
    entry_date: Mapped[date] = mapped_column(insert_default=func.now(), nullable=False, comment="员工的入职时间")

    def __str__(self):
        return f"员工id={self.id},姓名={self.name},年龄={self.age},性别={self.gender.value},工资={self.sal},奖金={self.bonus},是否离职={self.is_leave},入职时间={self.entry_date}"

# if __name__ == '__main__':
# 所有的表都重新创建（删除）表
# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

# 单独把某个表创建（删除）表
# Employee.__table__.create(engine)
# Employee.__table__.drop(engine)


    #      新增数据
if __name__ == '__main__':
    with sessionmaker(bind=engine).begin() as session:
        # 新增数据方式一:面向对象的方式
    #     emp1 = Employee(name="Momo", age=25, gender=SexValue.MALE, sal=Decimal("5000.00"), bonus=1000)
    #     emp2 = Employee(name="Nana", age=21, gender=SexValue.FEMALE, sal=Decimal("3800.00"), bonus=1200)
    #     emp3 = Employee(name="Lily", age=20, gender=SexValue.FEMALE, sal=Decimal("4500.00"), bonus=400)
    #     # session.add(emp1)
    #     session.add_all([emp1, emp2, emp3]) # 批量新增数据

        # 新增数据方式二:类SQL的方式
        # insert_stmt = insert(Employee).values(
        #     name="CC", age=21, gender=SexValue.FEMALE, sal=Decimal("9921.00"), bonus=521)
        # # 执行SQL语句
        # session.execute(insert_stmt)


        # get 返回一条数据
        # 查询id为2的员工
        # emp = session.get(Employee,2)
        # print(emp)


        # 返回全部数据,scalars 返回的是模型对象，all()返回一个列表
        # stmt = select(Employee)
        # list_emp = session.scalars(stmt).all()
        # for emp in list_emp:
        #     print(type(emp))
        #     print(emp)

        # 返回指定的字段数据，execute返回的是一个row对象,key就是属性名，value就是属性值
        # stmt = select(Employee.name, Employee.sal,Employee.age)
        # result = session.execute(stmt).all()
        # for obj in result:
        #     print(type(obj))
        #     print(obj.name,obj.age)


        #  采用原生SQL来查询
        # 返回指定的字段数据，execute返回的是一个row对象，key就是属性名，value就是属性值
        # sql = text('select name, sal from t_emp')
        # result = session.execute(sql).all()
        # for obj in result:
        #     print(type(obj))
        #     print(obj.name,obj.sal)

        sql = text('select id ,name, sal ,age from t_emp')
        orm_sql = sql.columns(Employee.id, Employee.name, Employee.sal,Employee.age)
        stmt = select(Employee).from_statement(orm_sql)
        result = session.execute(stmt).scalars()
        for obj in result:
            print(type(obj))
            print(obj)
