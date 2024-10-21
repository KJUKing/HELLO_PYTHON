from flask import jsonify
from flask import Flask, request, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def main():
    return "HELLO MVVM"

@app.route('/hello.ajax', methods=['POST'])
def ajax_hello():
    data = request.get_json()
    print(data['menu'])
    return jsonify(message = "ok")

@app.route('/fetch.ajax', methods=['POST'])
def ajax_fetch():
    data = request.get_json()
    print(data['menu'])
    return jsonify(message = "ok")

@app.route('/axios.ajax', methods=['POST'])
def ajax_axios():
    data = request.get_json()
    print(data['menu'])
    return jsonify(message = "ok")


if __name__ == '__main__':
    app.run()

