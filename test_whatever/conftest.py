import pytest

from utils.log_util import logger


@pytest.fixture(scope="function", autouse=True)
def FrontAfterPrint():
    logger.info("测试用例开始运行")
    yield
    logger.info("测试用例执行结束")
