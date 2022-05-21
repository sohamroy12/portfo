import email
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')  # !!!Accepting Dynamic page request !!!
def html_pages(page_name):
    return render_template(page_name)

# @app.route('/works.html')
# def Works():
#     return render_template('works.html')
# @app.route("/about.html")
# def About():
#     return render_template('about.html')
# @app.route("/contact.html")
# def Contact():
#     return render_template('contact.html')
# @app.route("/components.html")
# def Components():
#     return render_template('components.html')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database"
    else:
        return 'Something went Wrong. Kindly check again'
