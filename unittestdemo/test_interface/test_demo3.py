"""
实现mapremote
官网拷贝的代码 https://docs.mitmproxy.org/stable/addons-events/
做了少量修改，用mapremote实现对访问模拟器雪球页面的篡改
"""
import json

def response(flow):
    if "/v5/stock/batch/quote.json" in flow.request.pretty_url:
        res = json.loads(flow.response.content)
        # 定位元素方法类似于jq,定位到返回结果的第一个股票name进行篡改
        res["data"]["items"][0]["quote"]["name"]="hogwarts2020!!!!"
        # 记住返回值就是flow.response.text，返回结果的2次修改
        flow.response.text = json.dumps(res)