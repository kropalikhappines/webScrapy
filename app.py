from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html')


@app.route('/post_input', methods=['POST'])
def post_input():
    print(url_for('post_input'))
    if request.method == 'POST':
        print(request.form)
    return render_template('load.html')


@app.route('/about')
def about():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
