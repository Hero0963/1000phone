# ref= https://www.maxlist.xyz/2018/09/23/python_mysql/
# ref= https://www.796t.com/content/1526900177.html

# Connect MySQL
import mysql.connector


class MySQLTed(object):
    def __init__(self, host, user, passwd, dbname):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=passwd,
            database=dbname,
            # charset='utf8',
            buffered=True,
        )

    def exec(self, sql: str):
        self.db.cursor().execute(sql)
        self.db.commit()

    def query(self, sql: str):
        self.db.cursor().execute(sql)
        result = self.db.cursor().fetchall()
        return result


def main2():
    mysql_test = MySQLTed(
        "127.0.0.1",
        "root",
        "qwer987",
        "ted001",
    )

    # mysql_test.exec('create table t1 (id int auto_increment primary key,timestamp TIMESTAMP)')
    # mysql_test.exec('insert into t1 (id,timestamp) value (NULL,CURRENT_TIMESTAMP)')
    # mysql_test.exec('insert into t1 (id,timestamp) value (NULL,CURRENT_TIMESTAMP)')
    # result = mysql_test.query('select * from t1')
    result = mysql_test.query("SELECT * FROM users Where name Like 'M%'")
    for row in result:
        print(row)
    mysql_test.exec('delete from t1 where id = 1')


def main():
    teddb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="qwer987",
        database="ted001",
        buffered=True,
    )
    cursor = teddb.cursor()

    # Read
    cursor.execute("SELECT * FROM users Where name Like 'M%'")
    result = cursor.fetchall()
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
