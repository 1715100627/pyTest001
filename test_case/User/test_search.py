from tools.api import request_tool
import pytest
import allure


@allure.title("搜索用户")
def test_search(token):
    url = "https://api.hnyoujin.cn/api/sns/attention/findUserByAccountOrPhone0"
    headers = {
        "Content-Type": "application/json",
        "token": token
    }
    req = {
        "id": "17396240733"
    }

    resp = request_tool.post_json(url=url, headers=headers, json=req)
    resp_json = resp.json()
    success = resp_json['success']
    assert success == True