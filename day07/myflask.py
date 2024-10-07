from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask!'

@app.route('/param', methods=['GET'])
def param():
    # menu = request.args.get('menu', default = '탕수육', type = str)
    menu = request.args['menu']
    print(menu)
    return 'PARAM : ' + menu

@app.route('/post', methods=['POST'])
def post():
    # menu = request.form['menu']
    menu = request.form.get('menu', default = '탕수육')
    return 'POST : ' + menu

@app.route('/forw')
def forw():
    return render_template('forw.html')

if __name__ == '__main__':
    app.run(debug=True)