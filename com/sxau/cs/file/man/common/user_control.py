from com.sxau.cs.file.man.biz import user_biz


def login(user_req):
    return user_biz.login(user_req)


def logout():
    return user_biz.logout()
