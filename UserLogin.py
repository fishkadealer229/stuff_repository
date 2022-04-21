from flask_login import UserMixin


class UserLogin(UserMixin):
    def fromDB(self, username, db):
        self.__user = db.getUser(username)
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user['username'])

    def get_name(self):
        return str(self.__user['name'])

    def get_pass(self):
        return str(self.__user['password'])

    def get_age(self):
        return str(self.__user['age'])

    def get_locality(self):
        return str(self.__user['locality'])

    def get_gender(self):
        return str(self.__user['gender'])

    def get_work_place(self):
        return str(self.__user['work_place'])

    def get_surname(self):
        return str(self.__user['surname'])
