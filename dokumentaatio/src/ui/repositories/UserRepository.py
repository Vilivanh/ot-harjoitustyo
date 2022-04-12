from entities.user import User
from db_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return [User(row["username"], row["password"]) for row in rows]

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO Users (username, password) VALUES (?,?)', (user.username, user.password))
        self._connection.commit()
        return user


user_repository = UserRepository(get_database_connection())
users = user_repository.find_all()