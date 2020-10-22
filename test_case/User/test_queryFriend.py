from tools.api import request_tool
import pytest
import allure


@allure.title("好友列表")
def test_queryFriend(token):
    url = "https://api.hnyoujin.cn/api/sns/attention/queryFriend"
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
    success = resp_json['success']
    assert success == True
