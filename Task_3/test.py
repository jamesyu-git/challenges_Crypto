import pytest
import requests
import json
import pprint


def szse_get(url):
    jsonFile = open('./header.json','r')
    headers =json.load(jsonFile)
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    return response

def test_API_verification():
    response = szse_get('https://www.szse.cn/api/market/ssjjhq/getTimeData?random=0.017976275997469315&marketId=1&code=000001&language=EN')
    response_data = response.json()
    pprint.pprint(response_data)
    assert response_data['data']['high'] > response_data['data']['low']