from sqlite3 import Error

from connect import create_connection, database

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

if __name__ == '__main__':
    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     fullname VARCHAR(100) NOT NULL,
     email VARCHAR(100) NOT NULL,
     CONSTRAINT users_email_un UNIQUE (email)
    );
    """

    sql_create_status_table = """
    CREATE TABLE IF NOT EXISTS status (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name VARCHAR(50) NOT NULL,
     CONSTRAINT status_name_un UNIQUE (name)
    );
    """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     title VARCHAR(100),
     description TEXT,
     status_id INTEGER,
     user_id INTEGER,
     FOREIGN KEY (status_id) REFERENCES status (id)
         ON DELETE SET NULL
         ON UPDATE CASCADE,
     FOREIGN KEY (user_id) REFERENCES users (id)
         ON DELETE CASCADE
         ON UPDATE CASCADE
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
                        # create projects table
            create_table(conn, sql_create_users_table)
                        # create status table
            create_table(conn, sql_create_status_table)
                        # create tasks table
            create_table(conn, sql_create_tasks_table)
        else:
            print("Error! Cannot create the database connection.")
