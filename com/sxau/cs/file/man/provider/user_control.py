from com.sxau.cs.file.man.biz import user_biz
from com.sxau.cs.file.man.common.model.requset.user_req import UserRequest


def login():
    user_req = UserRequest()
    user_req.set_user_name('Bob')
    user_req.set_password('123')
    return user_biz.login(user_req)


def logout():
    return user_biz.logout()
