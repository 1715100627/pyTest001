from tools.api import request_tool
import allure


@allure.title("验证码登录")
@allure.feature('test_login_01')
def test_login_yzm():
    url = 'https://api.hnyoujin.cn/api/pass/login/v1/loginMobileCodeVerification'
    headers = {
        "Content-Type": "application/json"
    }
    req = {
        "account": "17396240733",
        "code": "964921",
        "deviceModel": "ELE-AL00",
        "mac": "02:00:00:00:00:02",
        "imei": "865166020414713",
        "center": "104.06549581016573,30.576648460590466",
        "softwareVersion": "5.1.1",
        "machineVersion": "Other",
        "netType": "WIFI",
        "cityCode": "028",
        "appVersion": "1.0.1",
        "deviceId": "20200903185703dabf12e1be271324194be12019f51f4301a4ddb69bd33ae9",
        "deviceTypeSkyEnum": "android"
    }
    resp = request_tool.post_json(url=url, headers=headers, json=req)
    resp_json = resp.json()
    # 提取响应内容进行断言；验证是否修改成功；
    success = resp_json['success']
    assert success == True
