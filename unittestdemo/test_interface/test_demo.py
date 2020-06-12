"""
get与post区别
该脚本执行成功后可开启一个服务：http://0.0.0.0:9091/
"""
from flask import Flask, session, request, Request, make_response

app = Flask(__name__)
request: Request
app.secret_key = "key"


@app.route("/request", methods=['POST', 'GET'])
def hello():
    query = request.args
    post = request.form
    return f"quest:{query}\n" \
           f"post:{post}"


@app.route("/session")
def session_handle():
    for k, v in request.args.item():
        session[k] = v
    resp = make_response({k: v for k, v in session.item()})
    for k, v in request.args.item():
        resp.set_cookie(f"cookie_{k}", v)
        return resp

# 替代录播中
if __name__ == '__main__':
    app.run(port=9091, debug=True, host='0.0.0.0')
