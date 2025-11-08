from peewee import *

# Connection to a MySQL database on network.
def connect_db():

    mysql_db = MySQLDatabase(
        'StaN1234_game_bd',
        user='StaN1234_clients',
        password='111111',
        host='10.11.13.118',
        port=3306
)
    return mysql_db
if __name__ == "__main__":
    print(connect_db().connect())