# encoding: utf-8

"""

Account Api模块
"""
import logging
import os

import allure
import pytest

from common.get_data_url import get_data_url
from common.parse_excel import ParseExcel

datadir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test_data")
data_url = get_data_url()
# 获取到test_data\test的目录，如果是prod环境，那么就是获取test_data\prod目录
authBaseDir = os.path.join(datadir, data_url)

logger = logging.getLogger("Account Api模块日志")


@allure.feature("AccountApi模块")
@pytest.mark.webtest
class TestAccountApi(object):
    """Query Related Achievements: /api/auth/account/achievement/related/query/v1

    """
    Query_Related_Achievements_dir = os.path.join(authBaseDir, 'Query_Related_Achievements.xlsx')
    logger.info("Query_Related_Achievements测试数据的路径是:{}".format(Query_Related_Achievements_dir))
    parse = ParseExcel(Query_Related_Achievements_dir, 'Sheet1')
    Query_Related_Achievements_params = parse.getDataFromSheet(5)

    @allure.story("Query Related Achievements(查询用户成就信息)")
    @pytest.mark.parametrize("clientType,language,retCode,istoken,result", Query_Related_Achievements_params)
    def test_001_Query_Related_Achievements(self, get_token_head, http, clientType, language, retCode, istoken, result):
        uri = '/api/auth/account/achievement/related/query/v1'
        params = {"clientType": clientType, "language": language}

        if istoken == 'yes':
            header = get_token_head
            response = http.get(uri=uri, params=params, headers=header)
            json_req = response.json()
            logger.info("Query_Related_Achievements有token的返回值是:{}".format(json_req))

            assert json_req.get('retCode') == 200
            assert json_req.get('result')[0]['smallImg'] == result
        else:
            response = http.get(uri=uri, params=params)
            json_req = response.json()
            logger.info("Query_Related_Achievements没有token的返回值是:{}".format(json_req))

            assert json_req.get('retCode') == 401
            assert json_req.get('message') == result　