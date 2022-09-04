import allure
import pytest

@allure.epic("项目名称：商城接口自动化")
@allure.feature("模块：用户管理自动化")

class Test:
#     # @pytest.mark.skip(reason="22这是class2跳过的用例")
#     # @pytest.mark.run(order=1)
    def test_class2(self):
        print("这是class2目录的用例1")