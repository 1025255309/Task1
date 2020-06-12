"""
官网拷贝的代码 https://docs.mitmproxy.org/stable/addons-scripting/
做了少量修改，用maplocal实现了对访问百度页面的篡改
This example shows how to send a reply from the proxy immediately
without sending any data to the remote server.
"""
from mitmproxy import http

# request是不能被改变的，定义一个方法并传递一个参数flow
def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.

    # 当我们访问百度连接时，就mock到mitmproxy指定的8090端口，并且篡改了页面内容，输出Hello World!!!!!!!!!
    if flow.request.pretty_url == "https://www.baidu.com/":
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World!!!!!!!!!",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )