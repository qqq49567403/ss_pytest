"""
======================
Author: songs
Time: 2021-11-07
Project: main
Company: 软件自动化测试
======================
"""

import pytest

# 相当于在命令行当中执行了pytest命令。
pytest.main([
    "--html=output/report/py33-pytest-api.html",
    "--junitxml=output/report/py33-api-test.xml",
    "--alluredir=output/allure/", "--clean-alluredir"
])
