# encoding: utf-8

import logging
import os

import pytest

from common.http_request import HTTPRequests
from config.url_config import URLConf


datadir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test_data")
logger = logging.getLogger('conftest日志')


def pytest_addoption(parser):
    # choices 只允许输入的值的范围
    parser.addoption(
        "--env", action="store", default='test', choices=['dev', 'test', 'prod'], help="set env"
    )


# 获取命令行参数的fixture
@pytest.fixture(scope='session')
def get_env(request):
    # print("fixutre..................")
    return request.config.getoption('--env')

# 声明一个返回http请求对象的fixture，所有用例在一个session中
# @pytest.fixture(scope='module', autouse=True)
@pytest.fixture(autouse=True)
def http(request):
    env = request.getfixturevalue("get_env")
    url_mapping = URLConf.url_mapping.value
    url = url_mapping.get(f'{env}')
    http = HTTPRequests(url)

    return http


@pytest.fixture(scope='session')
def get_token_head(request):
    env = request.getfixturevalue("get_env")
    url_mapping = URLConf.url_mapping.value
    url = url_mapping.get(f'{env}')
    http = HTTPRequests(url)

    user = URLConf.email_user.value
    user_list = user.get(f'{env}').split("/")
    username = user_list[0]
    password = user_list[1]

    param = {'clientType': 2,
             'language': 'en',
             'loginId': username,
             'loginPassword': password}

    logger.info("请求的url=={}".format(url))
    response = http.post(uri=r'/api/auth/login/account/v1', data=param)
    logger.info("获取的返回值是:".format(response.text))
    token = None
    if response.status_code == 200:
        token = response.json().get('result')['token']
    else:
        token = 'get token fail'

    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept': 'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, '
                  'application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, '
                  'application/msword, */*',
        'Accept-Language': 'zh-CN',
        'Authorization': token}

    yield head
