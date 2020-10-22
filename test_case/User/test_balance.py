from tools.api import request_tool
import allure
import pytest


@allure.title("余额查看")
@allure.feature('test_balance')
def test_balance(token):
    url = 'https://api.hnyoujin.cn/api/platform/userInfo/viewAccount'
    headers = {
        'token': token,
        "Content-Type": "application/json"
    }
    req = {
        "content": "balance"
    }
    resp = request_tool.post_json(url=url, headers=headers, json=req)
    resp_json = resp.json()
    # 提取响应内容进行断言；验证是否修改成功；
    success = resp_json['success']
    assert success == True
