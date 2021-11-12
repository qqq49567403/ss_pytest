"""
======================
Author: songs
Time: 2021-11-07
Project: test_login
Company: 软件自动化测试
======================
"""
import pytest
import allure
import os
from time import sleep

from common.handle_excel import HandleExcel
from common.handle_logger import logger
from common.handle_replace import data_replacement
from common.handle_path import testdatas_dir
from common.handle_data import Data, data_extraction

excel_path = os.path.join(testdatas_dir, "api_cases.xlsx")
cases = HandleExcel(excel_path, "投资").get_all_data()


@pytest.mark.usefixtures("req_assert")
class TestRecharge:

    @allure.title("{case[title]}")
    @pytest.mark.parametrize("case", cases)
    def test_recharge(self, case, req_assert):
        logger.info("===== 发起一次http请求 =====")
        logger.info("从excel中读取的测试数据为：{}".format(case))
        hr, hassert = req_assert
        # 替换数据
        case = data_replacement(case)

        # 发起请求
        if hasattr(Data, "token"):
            resp = hr.send_requests(case["method"], case["url"], case["request_data"],
                                         token=getattr(Data, "token"))
        else:
            resp = hr.send_requests(case["method"], case["url"], case["request_data"])
        resp = resp.json()

        # 数据提取
        if case["extract"]:
            data_extraction(resp, case["extract"])

        if case["expected"]:
            hassert.get_json_comp_res(case["expected"], resp)

        sleep(0.2)
        if case["check_sql"]:
            hassert.init_sql_conn()
            hassert.get_multi_sql_comp_resp(case["check_sql"])
            hassert.close_sql_conn()
