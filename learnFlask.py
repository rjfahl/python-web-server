import json
from flask import Flask
from flask import Response
from flask import request
from flask import send_file

app = Flask(__name__)

@app.route('/')
def default_route():
    names = { "names": request.args.getlist('name') or "Hello World!"}
    return Response(json.dumps(names), mimetype='application/json')

@app.route('/favicon.ico')
def get_favicon():
    return send_file('favicon.ico', mimetype='image/ico')

if __name__ == '__main__':
    app.run(port=3000)