from flask import jsonify
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return "HELLO MVVM"

@app.route('/ans1.ajax', methods=['POST'])
def ajax_ans1():
    return jsonify(ans = 1)

@app.route('/ans2.ajax', methods=['POST'])
def ajax_ans2():
    return jsonify(ans = 2)

@app.route('/ans3.ajax', methods=['POST'])
def ajax_ans3():
    return jsonify(ans = 3)


if __name__ == '__main__':
    app.run()

