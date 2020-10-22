from tools.api import request_tool
import pytest
import allure


@allure.title("群组列表")
def test_TeamList(token):
    url = "https://api.hnyoujin.cn/api/im/team/queryTeamList"
    headers = {
        "token": token,
        "Content-Type": "application/json"
    }

    resp = request_tool.post_json(url=url, headers=headers)
    resp_json = resp.json()
    success = resp_json["success"]
    assert success == True
