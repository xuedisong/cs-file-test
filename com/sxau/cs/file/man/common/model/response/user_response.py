class UserResponse:
    def __init__(self):
        self._token = ''

    def get_token(self):
        return self._token

    def set_token(self, token):
        self._token = token
