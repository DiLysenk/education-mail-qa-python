import pymysql
from faker import Faker

# create initial connection to MySQL server
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='pass',
                             db=None,
                             charset='utf8'
                             )

connection.query('DROP database IF EXISTS TEST_PYTHON')
connection.query('CREATE database TEST_PYTHON')
connection.close()

# create connection to created DataBase
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='pass',
                             db='TEST_PYTHON',
                             charset='utf8',
                             autocommit=True,  # automatically commit data on INSERT|UPDATE|DELETE
                             cursorclass=pymysql.cursors.DictCursor
                             )
prepods_query = """
    CREATE TABLE `prepods` (
      `id` smallint(6) NOT NULL AUTO_INCREMENT,
      `name` char(20) NOT NULL,
      `surname` char(50) NOT NULL,
      `start_teaching` date NOT NULL DEFAULT '2020-01-01',
      PRIMARY KEY (`id`)
    )
"""
connection.query(prepods_query)

fake = Faker()

for _ in range(5):
    insert_query = f"""
        INSERT into prepods (name, surname, start_teaching) 
        VALUES ("{fake.first_name()}", "{fake.last_name()}", "{fake.date()}")
    """
    connection.query(insert_query)

# get cursor interface to fetch data from query results
cursor = connection.cursor()
cursor.execute("SELECT * FROM prepods")
res = cursor.fetchall()  # get all data. for one row use cursor.fetchone()
print(res)

# always close connection at the end
connection.close()
