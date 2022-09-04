import re

import allure
import pytest
from commons.yaml_util import read_yaml
import requests

# @pytest.mark.usefixtures("exe_sql")



@allure.epic("项目名称：商城接口自动化")
@allure.feature("模块：商品管理自动化")

class Test:
    # @allure.story("接口名称：登录接口")
    # @allure.title("用力名称：登录成功")
    # @allure.description("描述：登录列表")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.link("接口连接")
    # @allure.issue("bug连接")
    # @allure.testcase("用例的连接")
    # def test_class1_login(self,base_url):
    #     print("这是class1里的test_class2")
    #     api_url = "order/index"
    #     all_url = base_url + api_url
    #     print(all_url)
    #     #增加用例执行步骤
    #     for i in range(1,11):
    #         with allure.step("这是第"+ str(i) + "步：步骤如下："):
    #             print("执行第"+ str(i) +" 步")
    #     #增加用例用例附件
    #     with open("D:\\666.jpg",mode="rb") as f:
    #         content = f.read()
    #         allure.attach(body=content,name="错误截图",attachment_type=allure.attachment_type.JPG)
    #
    # @allure.story("接口名称：注册接口")
    # def test_class1_register(self,base_url):
    #     print("这是class1里的test_class2")
    #     api_url = "order/index"
    #     allurl = base_url + api_url
    #     print(allurl)
    #     allure.dynamic.title("用力名：注册成功")
    #     allure.dynamic.description("用力描述：注册成功")
    #对用例传入yaml参数
    @pytest.mark.parametrize("caseinfo",read_yaml("./test.yaml"))
    def test_get_metris(self,base_url,caseinfo):
        # print("测试parametrize函数，传入两个值就会执行两次" + str(caseinfo))
        # print("---------------------------------------------------------")
        # print("---------------------------------------------------------")
        # print(caseinfo["story"])
        # print(caseinfo["title"])
        # print(caseinfo["request"]["method"])
        # print(base_url+caseinfo["request"]["url"])
        # 获取到yaml里的参数
        print(caseinfo)
        url = base_url + caseinfo["request"]["url"]
        data = caseinfo["request"]["data"]
        params = caseinfo["request"]["params"]
        #发起请求
        res = requests.post(url,json=data,params=params)
        print(res.text)

        re.search