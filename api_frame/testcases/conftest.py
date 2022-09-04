import pytest


# @pytest.fixture(scope="class",autouse=True,params=[1,222],ids=["aa","bbb"],name="sql")
# @pytest.fixture(scope="class",autouse=True)
# def exe_sql():
#     print("连接sql")
#     yield
#     print("关闭sql")

# @pytest.fixture(scope="module",autouse=True)
# def exe_login():
#     print("固件2的")
#     yield
#     print("固件2的关闭")