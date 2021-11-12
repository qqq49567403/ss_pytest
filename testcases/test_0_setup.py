"""
======================
Author: songs
Time: 2021-11-07
Project: test_login
Company: 软件自动化测试
======================
"""
import pytest
import os
import allure

from common.handle_excel import HandleExcel
from common.handle_logger import logger
from common.handle_replace import data_replacement
from common.handle_path import testdatas_dir

excel_path = os.path.join(testdatas_dir, "api_cases.xlsx")
cases = HandleExcel(excel_path, "全局前置操作").get_all_data()


class TestSetup:

    @allure.title("{case[title]}")
    @pytest.mark.parametrize("case", cases)
    def test_login(self, case, login):
        logger.info("===== 发起一次http请求 =====")
        logger.info("从excel中读取的测试数据为：{}".format(case))
        hr = login
        # 替换数据
        case = data_replacement(case)

        # 发起请求
        resp = hr.send_requests(case["method"], case["url"], case["request_data"])
        # print(resp.json())

