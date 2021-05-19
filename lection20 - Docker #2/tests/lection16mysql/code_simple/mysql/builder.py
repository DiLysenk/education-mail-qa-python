from faker import Faker


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

        insert_prepod = f"""
                    INSERT INTO prepods(name, surname, start_teaching) VALUES('{name}', '{surname}', '{start_teaching}')
                    """
        self.client.execute_query(insert_prepod, fetch=False)

    def create_student(self, name=None, prepod_id=None):
        if prepod_id is None:
            self.create_prepod()
            prepod_id = self.client.connection.insert_id()

        if name is None:
            name = fake.first_name()

        insert_student = f"""
        INSERT INTO students(name, prepod_id) VALUES('{name}', {prepod_id})
        """
        self.client.execute_query(insert_student, fetch=False)

