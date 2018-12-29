import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':
    create_connection("user.db")




#
# def create_table():
# 	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(name TEXT, major TEXT)')
#
# def data_entry():
# 	c.execute("INSERT INTO stuffToPlot VALUES('2016-01-01', 'rish')")
# 	conn.commit()
# 	c.close()
# 	conn.close()
#
#
# def dynamic_data_entry(name, classes):
# 	#unix = time.time()
# 	#date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
# 	keyword = name
# 	#value = random.randrange(0,10)
# 	major = classes
# 	c.execute("INSERT INTO stuffToPlot (name, major) VALUES (?, ?)",
# 		(keyword))
# 	conn.commit()
#
# #create_table()
# #data_entry()
# #events = ["cs","math","chem", "physics","english","apush","apug"]
# #sch = new schedule(courses)
# #pat = new User("pranay", sch)
# dynamic_data_entry("rohan",)
#
#
# # for i in range(10):
# # 	dynamic_data_entry("rohan", "chem")
# # 	time.sleep(1)
# c.close()
# conn.close()
