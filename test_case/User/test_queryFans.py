from tools.api import request_tool
import pytest
import allure


@allure.title("粉丝列表")
def test_queryFans(token):
    url = "https://api.hnyoujin.cn/api/sns/attention/queryFans"
    headers = {
        "token": token,
        "Content-Type": "application/json"
    }
    req = {
        "page": "0",
        "size": "20"
    }

    resp = request_tool.post_json(url=url, headers=headers, json=req)
    resp_json = resp.json()
    success = resp_json["success"]
    assert success == True
