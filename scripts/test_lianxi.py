# import os,sys
# sys.path.append(os.getcwd())
# from time import sleep
# import pytest
#
# from base.base_dirver import init_driver
# from page.login_page import LoginPage
# from base.base_yml import yml_data_with_file
# from base.base_yml import data_with_key
# class TestLogin:
#     @pytest.mark.parametrize("args",data_with_key("test_login2"))
#     def test_login2(self,args):
#         #ele=data_with_key("test_login2")[0]['username']
#         print(args['username'])
#         print(args['password'])
#         print(args["toast"])
# username="zhngsan"
# password="123"
# toast="登陆成功"
# print(username,password,toast)
def readimage():
    with open("../screen/test_login_001.png", "rb") as f:
        context = f.read()
    print(context)
readimage()


