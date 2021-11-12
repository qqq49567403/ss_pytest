"""
======================
Author: songs
Time: 2021-11-07
Project: test_login
Company: 软件自动化测试
======================
"""
import pytest

from common.handle_requests import HandleRequests
from common.handle_assert import HandleAssert
from common.handle_logger import logger


@pytest.fixture(scope="class")
def login():
    hr = HandleRequests()
    yield hr


@pytest.fixture
def req_assert():
    hr = HandleRequests()
    hassert = HandleAssert()
    yield hr, hassert
    hassert.init_sql_comp_res()
