from tools.api import request_tool
import allure
import pytest


@allure.title("关注列表")
def test_Attention(token):
    url = "https://api.hnyoujin.cn/api/sns/attention/queryAttention"
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
