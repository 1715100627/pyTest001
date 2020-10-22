import pytest
from tools.api import request_tool
@pytest.fixture(scope='session')
def token():
    url='https://api.hnyoujin.cn/api/pass/login/v1/in'
    req={
          "account":"17396240733",
          "pass":"123456",
          "deviceModel":"ELEAL00",
          "mac":"02:00:00:00:00:02",
          "imei":"865166020414713",
          "center":"104.066353,30.57489",
          "softwareVersion":"5.1.1",
          "machineVersion":"Other",
          "netType":"WIFI",
          "cityCode":"028",
          "appVersion":"1.0.1",
          "deviceId":"20200903185703dabf12e1be271324194be12019f51f4301a4ddb69bd33ae9",
          "deviceTypeSkyEnum":"android"
        }
    resp = request_tool.post_json(url, json=req)
    print(resp)
    resp_json=resp.json()
    token = resp_json['data']['token']
    print(token)
    return token


