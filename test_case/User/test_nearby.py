from tools.api import request_tool
import allure
import pytest


@allure.title("附近动态")
@allure.feature('test_balance')
def test_balance(token):
    url = 'https://api.hnyoujin.cn/api/sns/circle/queryNearby'
    headers = {
        'token': token,
        "Content-Type": "application/json"
    }
    req = {
        "page": 0,
        "size": 20,
        "latitude": 30.57664852016058,
        "longitude": 104.0654955195855,
        "regionNo": "028"
    }
    resp = request_tool.post_json(url=url, headers=headers, json=req)
    resp_json = resp.json()
    # 提取响应内容进行断言；验证是否修改成功；
    success = resp_json['success']
    assert success == True