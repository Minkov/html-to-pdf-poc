from datetime import datetime

from flask import Flask, request, send_file

app = Flask(__name__)

import pdfkit

# from wkhtmltopdf import wkhtmltopdf

config = pdfkit.configuration()


def get_name():
    return f'export-{datetime.today().strftime("%Y-%m-%d__ %H-%M-%S")}'


options = {
    '--debug-javascript': None,
    'debug': None,
}


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    if request.method == 'GET':
        url = request.args.get('url')

        # file_name = f'/app/pdfs/{get_name()}.pdf'
        file_name = f'./pdfs/{get_name()}.pdf'

        pdfkit.from_url(
            url,
            file_name
        )

        return send_file(file_name, attachment_filename="certificate.pdf")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
