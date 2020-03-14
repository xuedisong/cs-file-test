# coding=utf-8
from com.sxau.cs.file.man.common.constants import constant
from com.sxau.cs.file.man.common.model.response.user_response import UserResponse

_USER_NAME_NOT_NULL = '用户名不能为空'
_USER_PASSWORD_NOT_NULL = '用户密码不能为空'
_LOGGER = None


def login(user_request):
    print _LOGGER
    if user_request.get_user_name() != '' and user_request.get_user_name() is not None:
        return True
    else:
        print _USER_NAME_NOT_NULL
        print constant.NET_BUSY
        return False


def logout():
    return UserResponse()
