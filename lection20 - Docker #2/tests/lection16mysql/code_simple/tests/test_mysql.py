import pytest

from mysql.builder import MySQLBuilder


class MySQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)

        self.prepare()


class TestMysql(MySQLBase):
    """
    dmdmas;da
    """
    def prepare(self):
        self.mysql_builder.create_prepod()
        self.prepod_id = self.mysql.connection.insert_id()

        for i in range(10):
            self.mysql_builder.create_student(prepod_id=self.prepod_id)

    def get_students(self):
        students = self.mysql.execute_query('SELECT * FROM students')
        print(students)
        return students

    def test(self):
        students = self.get_students()
        assert len(students) == 10


class TestMysqlDelete(TestMysql):

    def test(self):
        self.mysql.execute_query('DELETE FROM students')

        students = self.get_students()
        assert len(students) == 0










