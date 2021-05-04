import pymysql


class MysqlClient:

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = '127.0.0.1'
        self.port = 3306

        self.connection = None

    def connect(self, db_created=True):
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db_name if db_created else None,
            charset='utf8',
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
        )

    def execute_query(self, query, fetch=True):
        cursor = self.connection.cursor()
        cursor.execute(query)
        if fetch:
            return cursor.fetchall()

    def recreate_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)
        self.connection.close()

    def create_prepods(self):
        prepods_query = """
        CREATE TABLE `prepods` (
          `id` smallint(6) NOT NULL AUTO_INCREMENT,
          `name` char(20) NOT NULL,
          `surname` char(50) NOT NULL,
          `start_teaching` date NOT NULL DEFAULT '2020-01-01',
          PRIMARY KEY (`id`)
        )
        """
        self.execute_query(prepods_query, fetch=False)

    def create_students(self):
        students_query = """
        CREATE TABLE `students` (
          `id` smallint(6) NOT NULL AUTO_INCREMENT,
          `name` char(20) DEFAULT NULL,
          `prepod_id` smallint(6) NOT NULL,
          PRIMARY KEY (`id`),
          KEY `prepod_id` (`prepod_id`),
          CONSTRAINT `students_ibfk_1` FOREIGN KEY (`prepod_id`) REFERENCES `prepods` (`id`)
        )
        """
        self.execute_query(students_query, fetch=False)




