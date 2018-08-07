import pprint
from flask import Flask, request, render_template, redirect, make_response

app = Flask(__name__)
app.config['DEBUG'] = True

pprint.PrettyPrinter(depth=4, width=10)

@app.route("/")
def http_dump():
    return render_template('dump.html', data=pprint.pformat(request.headers))

@app.route("/logout")
def logout():
    resp = make_response(render_template('logout.html'))
    resp.set_cookie('AWSELBAuthSessionCookie-0', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
