"""
官网拷贝的代码 https://docs.mitmproxy.org/stable/addons-scripting/
做了少量修改，用maplocal实现对访问模拟器雪球页面的篡改
This example shows how to send a reply from the proxy immediately
without sending any data to the remote server.
"""
from mitmproxy import http

# request是不能被改变的，定义一个方法并传递一个参数flow
def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.

    # 当我们访问模拟器雪球（判断url中存在queto.json）连接时，就mock到mitmproxy指定的8090端口，并且篡改雪球页面的内容
    if "quote.json" in flow.request.pretty_url:
        # 打开本地文件
        with open("D:\\proiect\\tmp-data\\xueqiu.json", encoding="utf-8") as f: # 注意使用反斜杠或者双斜杠，防止转意
            # 将json文件内容加载到返回结果
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )