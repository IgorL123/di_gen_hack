from flask import Flask, render_template, request, send_file
from model import text2text
from config import API_KEY
import os

app = Flask(__name__)
os.environ["OPENAI_API_KEY"] = API_KEY


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        text = request.form
        res = "Null"
        for key, value in text.items():
            successfull_generate = False
            while not successfull_generate:
                try:
                    from exec import generate
                    from parse import parse
                    import settings
                    list_res = []

                    while not list_res:
                        res = text2text(value)
                        print(res)
                        list_res = parse(res)

                    generate(
                                list_res[1],
                                list_res[2],
                                list_res[3],
                                list_res[0],
                                settings.COMPANY_NAME,
                                settings.DIRECTOR
                                )
                    successfull_generate = True
                except Exception as e:
                    print(e)

        return render_template("result.html", result=res)


@app.route('/docx/download')
def load2doc():
    return send_file(
        os.getcwd() + "\\docs\\" + "Result.docx",
        download_name='result.docx',
        as_attachment=True
    )


@app.route('/pdf/download')
def load2pdf():
    return send_file(
        os.getcwd() + "\\docs\\" + "Result.pdf",
        download_name='result.pdf',
        as_attachment=True
    )


if __name__ == '__main__':
    app.run()
