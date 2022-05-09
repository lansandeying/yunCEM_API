#encoding:utf-8
from common.logger import logger
from common.http_requests import HTTPRequests
from config.url_config import URLConfig
import os
import pytest

datadir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test_data")

def pytest_addoption(parser):
    parser.addoption(
        "--env",action="store",default="test",chioces=["dev","test"],help("set env")
    )

@pytest.fixture(scope="session")
def get_env(request):
    return request.config.getoption('--env')

if __name__=="__main__":
    print(get_env)

