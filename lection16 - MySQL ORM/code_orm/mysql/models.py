from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Prepod(Base):
    __tablename__ = 'prepods'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Prepod(" \
               f"id='{self.id}'," \
               f"name='{self.name}', " \
               f"surname='{self.surname}', " \
               f"start_teaching='{self.start_teaching}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(50), nullable=False)
    start_teaching = Column(Date, nullable=False, default='2020-01-01')


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Student(" \
               f"id='{self.id}'," \
               f"name='{self.name}', " \
               f"prepod_id='{self.prepod_id}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    prepod_id = Column(Integer, ForeignKey(f'{Prepod.__tablename__}.{Prepod.id.name}'), nullable=False)
