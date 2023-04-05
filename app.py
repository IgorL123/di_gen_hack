from flask import Flask, render_template, request
from model import text2text

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        text = request.form
        res = "Null"
        for key, value in text.items():
            res = text2text(value)
        return render_template("result.html", result=res)


if __name__ == '__main__':
    app.run(debug=True)
