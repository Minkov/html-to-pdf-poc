from datetime import datetime

from flask import Flask, request, send_file
import weasyprint

app = Flask(__name__)


def get_name():
    return f'export-{datetime.today().strftime("%Y-%m-%d__ %H-%M-%S")}'


@app.route('/convert', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'GET':
        url = request.args.get('url')

        pdf = weasyprint.HTML(url, media_type="screen") \
            .write_pdf()

        # file_name = f'/app/pdfs/{get_name()}.pdf'
        file_name = f'./pdfs/{get_name()}.pdf'
        with open(file_name, 'wb') as file:
            file.write(pdf)
        return send_file(file_name, attachment_filename="certificate.pdf")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
