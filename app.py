from flask import Flask, request, render_template, send_file
from fpdf import FPDF

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/anketa', methods=['GET', 'POST'])
def handle_data():
    fio = request.form['FIO']
    dob = request.form['DOB']
    pol = request.form['POL']
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_font('Times', '', 'times.ttf', uni=True)
    pdf.add_font('Times', 'B', 'timesbd.ttf', uni=True)
    pdf.set_font('Times', '', 14)
    pdf.add_page()
    pdf.cell(100, 5, txt=fio, ln=1)
    pdf.cell(100, 5, txt=dob, ln=1)
    pdf.cell(100, 5, txt=pol, ln=1)
    pdf.output("static/pdf/anketa.pdf")
    return send_file('static/pdf/anketa.pdf', attachment_filename='anketa.pdf')


if __name__ == '__main__':
    app.run(port=5001)
