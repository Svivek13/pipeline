from flask import Flask
from gevent.pywsgi import WSGIServer
app = Flask(__name__)
app.debug = True

# @app.route('/<int:number>,<string:name>/')
# def incrementer(number,name):
#     total = 0
#     for i in range(number+1):
#         total = total+i
#     return "Hello Mr.{}. The total sum upto {} is {}.".format(name,str(number),str(total))

@app.route('/')
def Hello():
    return "Hello ! Working fine."


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 2021), app)
    http_server.serve_forever()
