# coding=utf-8
_USER_NAME_NOT_NULL = '用户名不能为空'
_USER_PASSWORD_NOT_NULL = '用户密码不能为空'


def login(user_request):
    if user_request.get_user_name() != '' and user_request.get_user_name() is not None:
        return True
    else:
        print _USER_NAME_NOT_NULL
        return False


def logout():
    return True
