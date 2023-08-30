"""Create portfolio with flask."""
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home_page():
    """Home page."""
    return render_template('index.html')

@app.route('/<string:name>')
def render_page(name):
    """Render page."""
    return render_template(name)

def write_to_file(data):
    """Write form information to txt file."""
    with open('database.txt', 'a', encoding='UTF-8') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f"\n{email} | {subject} | {message}")

def write_to_csv(data):
    """Write form information to csv file."""
    with open('database.csv', 'a', encoding='UTF-8') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,
                                delimiter='|',
                                quotechar='"',
                                lineterminator='',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Submit contact form."""
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, please try again!'

if __name__ == '__main__':
    app.run(debug=True)
