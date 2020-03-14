class UserRequest:
    def __init__(self):
        self._username = ''
        self._password = ''

    def get_user_name(self):
        return self._username

    def get_password(self):
        return self._password

    def set_user_name(self,user_name):
        self._username=user_name

    def set_password(self,password):
        self._password=password
