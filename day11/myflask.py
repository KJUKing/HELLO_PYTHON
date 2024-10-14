from flask import jsonify
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return "HELLO MVVM"

@app.route('/hello.ajax')
def ajax_hello():
    #data = request.get_json()
    #print(data)

    return jsonify(message = "ok")

if __name__ == '__main__':
    app.run()

