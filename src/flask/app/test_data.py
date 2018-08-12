import pytest

from app.data.firebase import Firebase
from app.data.mysql import MySQL


# Fixtures are good !
@pytest.fixture
def mysql():
    return MySQL()


@pytest.fixture
def firebase():
    return Firebase()


class TestMysql():

    def test_connection(self, mysql):
        assert mysql  # mysql variable is non null, which means connection is successful

    def test_user_table_exists(self, mysql):
        cursor = mysql.execute(mysql.QUERY_SELECT_USERS_10)
        assert cursor.rowcount > 0  # at least one user exists in the user table

    def test_firebase_users_exist_in_mysql(self, mysql, benchmark):
        @benchmark
        def imports():
            return mysql.import_all_firebase_users()
        assert imports == 0  # all firebase users already in mysql database

    def test_firebase_users_reimport_in_mysql(self, mysql, benchmark):
        imports = benchmark(mysql.import_all_firebase_users, reimport=True)
        # mysql.commit()
        assert imports > 0


class TestFirebase():
    def test_users_list_retrieved(self, firebase):
        users = firebase.getUsers()
        assert len(users) > 0  # at least one user retrieved from firebase
