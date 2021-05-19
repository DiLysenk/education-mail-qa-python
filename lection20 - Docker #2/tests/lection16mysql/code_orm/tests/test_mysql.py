import pytest

from mysql.builder import MySQLBuilder
from mysql.models import Student


class MySQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)

        self.prepare()


class TestMysql(MySQLBase):

    def prepare(self):
        self.prepod = self.mysql_builder.create_prepod()

        for i in range(10):
            self.mysql_builder.create_student(prepod_id=self.prepod.id)

    def get_students(self, prepod_id):
        students = self.mysql.session.query(Student).filter_by(prepod_id=prepod_id).all()
        print(students)
        return students

    def test(self):
        students = self.get_students(prepod_id=self.prepod.id)
        assert len(students) == 10

        for s in students:
            assert s.prepod_id == self.prepod.id

        print(self.mysql.session.query(Student).filter_by(id=5).first())  # first model
        print(self.mysql.session.query(Student).filter_by(id=5).all())    # all models
        print(self.mysql.session.query(Student).filter_by(id=5))          # show SQL query


class TestMysqlDelete(TestMysql):

    def test(self):
        # delete by id
        self.mysql.session.query(Student).filter_by(id=5).delete()
        assert len(self.get_students(prepod_id=self.prepod.id)) == 9

        # delete concrete model
        student_to_delete = self.mysql.session.query(Student).filter_by(id=8).first()
        self.mysql.session.delete(student_to_delete)

        assert len(self.get_students(prepod_id=self.prepod.id)) == 8

        # delete all
        self.mysql.session.query(Student).delete()
        assert len(self.get_students(prepod_id=self.prepod.id)) == 0










