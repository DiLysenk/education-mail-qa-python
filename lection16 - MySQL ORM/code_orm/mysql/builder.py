from faker import Faker

from mysql.models import Prepod, Student

fake = Faker()


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_prepod(self, name=None, surname=None, start_teaching=None):
        if name is None:
            name = fake.first_name()

        if surname is None:
            surname = fake.last_name()

        if start_teaching is None:
            start_teaching = fake.date()

        prepod = Prepod(
            name=name,
            surname=surname,
            start_teaching=start_teaching
        )
        self.client.session.add(prepod)
        self.client.session.commit()

        return prepod

    def create_student(self, name=None, prepod_id=None):
        if prepod_id is None:
            prepod_id = self.create_prepod().id

        if name is None:
            name = fake.first_name()

        student = Student(
            name=name,
            prepod_id=prepod_id
        )
        self.client.session.add(student)
        self.client.session.commit()
        return student
