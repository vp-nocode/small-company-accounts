
class User:
    _users = []

    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'  # default access level

    @classmethod
    def get_users(cls):
        return cls._users

    @staticmethod
    def find_user_by_id(user_id):
        for cur_user in User._users:
            if user._user_id == user_id:
                return cur_user
        return None

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, new_name):
        if self in User._users:
            self._name = new_name
        else:
            print('User not found')


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, new_user):
        if new_user not in self._users:
            self._users.append(user)

    def remove_user(self, user_id):
        find_user = User.find_user_by_id(user_id)
        if find_user:
            self._users.remove(find_user)


admin = Admin('001', 'Alica')
user1 = User('002', 'Slava')
user2 = User('003', 'Petr')

# Админ добавляет пользователей
admin.add_user(admin)
admin.add_user(user1)
admin.add_user(user2)

# Печать списка пользователей
for user in User.get_users():
    print(f'ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}')

# Админ удаляет пользователя
admin.remove_user('003')

user1.set_name('Viacheslav')

# Печать обновленного списка пользователей
print("\nAfter removing user and rename another user:")
for user in User.get_users():
    print(f'ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}')
